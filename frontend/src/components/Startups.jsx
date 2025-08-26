import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Startups.css';

const Startups = () => {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedProject, setSelectedProject] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [downloading, setDownloading] = useState({});

  const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

  useEffect(() => {
    fetchProjects();
  }, []);

  const fetchProjects = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_BASE_URL}/projects`);
      setProjects(response.data);
    } catch (error) {
      console.error('Error fetching projects:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleViewDetails = async (projectId) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/projects/${projectId}`);
      setSelectedProject(response.data);
      setShowModal(true);
    } catch (error) {
      console.error('Erreur lors de la récupération des détails:', error);
    }
  };

  const handleDownload = async (projectId, projectName) => {
    try {
      setDownloading(prev => ({ ...prev, [projectId]: true }));
      
      const response = await axios.get(`${API_BASE_URL}/projects/${projectId}/download`, {
        responseType: 'blob'
      });

      // Create download link
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `${projectName}_${projectId}.zip`);
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Erreur lors du téléchargement:', error);
      alert('Erreur lors du téléchargement du projet');
    } finally {
      setDownloading(prev => ({ ...prev, [projectId]: false }));
    }
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('fr-FR', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const closeModal = () => {
    setShowModal(false);
    setSelectedProject(null);
  };

  if (loading) {
    return (
      <div className="startups-container">
        <div className="loading">Chargement des projets...</div>
      </div>
    );
  }

  return (
    <div className="startups-container">
      <h1>Startups Créées</h1>
      
      {projects.length === 0 ? (
        <div className="no-projects">
          <p>Aucun projet startup n'a été créé pour le moment.</p>
        </div>
      ) : (
        <div className="projects-table-container">
          <table className="projects-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Idée</th>
                <th>Date de création</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {projects.map((project) => (
                <tr key={project.id} className="project-row">
                  <td className="project-id">{project.id}</td>
                  <td className="project-idea">{project.idea}</td>
                  <td className="project-date">{formatDate(project.created_at)}</td>
                  <td className="project-actions">
                    <button
                      className="btn btn-primary btn-rounded"
                      onClick={() => handleViewDetails(project.id)}
                    >
                      Voir détails
                    </button>
                    <button
                      className="btn btn-primary btn-rounded"
                      onClick={() => handleDownload(project.id, project.idea)}
                      disabled={downloading[project.id]}
                    >
                      {downloading[project.id] ? 'Téléchargement...' : 'Télécharger'}
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Modal pour les détails du projet */}
      {showModal && selectedProject && (
        <div className="modal-overlay" onClick={closeModal}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <h2>Détails du Projet</h2>
              <button className="modal-close" onClick={closeModal}>×</button>
            </div>
            
            <div className="modal-body">
              <div className="project-detail">
                <h3>Idée</h3>
                <p>{selectedProject.idea}</p>
              </div>
              
              {selectedProject.roadmap && (
                <div className="project-detail">
                  <h3>Roadmap</h3>
                  <pre className="json-display">
                    {JSON.stringify(selectedProject.roadmap, null, 2)}
                  </pre>
                </div>
              )}
              
              {selectedProject.stack && (
                <div className="project-detail">
                  <h3>Stack Technique</h3>
                  <pre className="json-display">
                    {JSON.stringify(selectedProject.stack, null, 2)}
                  </pre>
                </div>
              )}
              
              <div className="project-detail">
                <h3>Métadonnées</h3>
                <p><strong>ID:</strong> {selectedProject.id}</p>
                <p><strong>Créé le:</strong> {formatDate(selectedProject.created_at)}</p>
                {selectedProject.path && (
                  <p><strong>Chemin:</strong> {selectedProject.path}</p>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Startups;