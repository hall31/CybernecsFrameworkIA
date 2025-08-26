import React, { useState, useEffect } from 'react';
import Layout from '../components/Layout';
import Toast from '../components/Toast';
import { BuildingOfficeIcon, ArrowDownTrayIcon, CalendarIcon, EyeIcon } from '@heroicons/react/24/outline';

const Startups = () => {
  const [startups, setStartups] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [showToast, setShowToast] = useState(false);
  const [toastMessage, setToastMessage] = useState('');
  const [toastType, setToastType] = useState('success');

  // Mock data pour la démo - à remplacer par un vrai appel API GET /projects
  const mockStartups = [
    {
      id: 1,
      idea: "Plateforme SaaS pour automatiser la génération de leads B2B avec l'IA",
      created_at: "2024-01-15T10:30:00Z",
      status: "completed",
      estimated_hours: 120
    },
    {
      id: 2,
      idea: "Application mobile de gestion de tâches avec IA prédictive",
      created_at: "2024-01-10T14:20:00Z",
      status: "in_progress",
      estimated_hours: 80
    },
    {
      id: 3,
      idea: "Marketplace de freelances spécialisés en développement web",
      created_at: "2024-01-05T09:15:00Z",
      status: "completed",
      estimated_hours: 200
    },
    {
      id: 4,
      idea: "Outil d'analyse de sentiment pour les réseaux sociaux",
      created_at: "2024-01-01T16:45:00Z",
      status: "pending",
      estimated_hours: 60
    }
  ];

  useEffect(() => {
    fetchStartups();
  }, []);

  const fetchStartups = async () => {
    setIsLoading(true);
    try {
      // Ici vous feriez un vrai appel API: GET /projects
      // const response = await fetch('/projects');
      // const data = await response.json();
      
      // Simulation d'un délai réseau
      await new Promise(resolve => setTimeout(resolve, 1000));
      setStartups(mockStartups);
    } catch (error) {
      console.error('Error fetching startups:', error);
      setToastMessage('Erreur lors du chargement des startups');
      setToastType('error');
      setShowToast(true);
    } finally {
      setIsLoading(false);
    }
  };

  const downloadZip = async (startupId) => {
    try {
      // Ici vous feriez un appel API pour télécharger le ZIP
      // const response = await fetch(`/download-startup/${startupId}`);
      
      setToastMessage('Téléchargement démarré!');
      setToastType('success');
      setShowToast(true);
      
      // Simulation du téléchargement
      setTimeout(() => {
        const link = document.createElement('a');
        link.href = '#';
        link.download = `startup-${startupId}.zip`;
        link.click();
      }, 1000);
    } catch (error) {
      setToastMessage('Erreur lors du téléchargement');
      setToastType('error');
      setShowToast(true);
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

  const getStatusBadge = (status) => {
    const statusConfig = {
      completed: { color: 'bg-green-100 text-green-800', text: 'Terminé' },
      in_progress: { color: 'bg-blue-100 text-blue-800', text: 'En cours' },
      pending: { color: 'bg-yellow-100 text-yellow-800', text: 'En attente' }
    };
    
    const config = statusConfig[status] || statusConfig.pending;
    
    return (
      <span className={`px-2 py-1 rounded-full text-xs font-medium ${config.color}`}>
        {config.text}
      </span>
    );
  };

  if (isLoading) {
    return (
      <Layout>
        <div className="flex items-center justify-center h-64">
          <div className="text-center">
            <div className="w-8 h-8 border-4 border-accent border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
            <p className="text-gray-600">Chargement des startups...</p>
          </div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="mb-6">
        <h1 className="text-3xl font-bold text-gray-900">Mes Startups</h1>
        <p className="text-gray-600 mt-2">
          Historique de toutes vos startups générées et leurs roadmaps
        </p>
      </div>

      {startups.length === 0 ? (
        <div className="text-center py-12">
          <BuildingOfficeIcon className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">Aucune startup disponible</h3>
          <p className="text-gray-600">
            Générez votre première startup depuis la page d'accueil pour la voir ici.
          </p>
        </div>
      ) : (
        <div className="card overflow-hidden">
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    ID
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Idée
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Date
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Statut
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Estimation
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Actions
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {startups.map((startup) => (
                  <tr key={startup.id} className="hover:bg-gray-50 transition-colors duration-200">
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                      #{startup.id}
                    </td>
                    <td className="px-6 py-4">
                      <div className="max-w-xs">
                        <p className="text-sm text-gray-900 font-medium truncate">
                          {startup.idea}
                        </p>
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      <div className="flex items-center">
                        <CalendarIcon className="w-4 h-4 mr-2" />
                        {formatDate(startup.created_at)}
                      </div>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      {getStatusBadge(startup.status)}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {startup.estimated_hours}h
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                      <div className="flex items-center space-x-2">
                        <button
                          onClick={() => downloadZip(startup.id)}
                          className="text-accent hover:text-blue-700 transition-colors duration-200 flex items-center space-x-1"
                          title="Télécharger ZIP"
                        >
                          <ArrowDownTrayIcon className="w-4 h-4" />
                          <span>ZIP</span>
                        </button>
                        <button
                          className="text-gray-600 hover:text-gray-900 transition-colors duration-200 flex items-center space-x-1"
                          title="Voir la roadmap"
                        >
                          <EyeIcon className="w-4 h-4" />
                          <span>Voir</span>
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {showToast && (
        <Toast
          message={toastMessage}
          type={toastType}
          onClose={() => setShowToast(false)}
        />
      )}
    </Layout>
  );
};

export default Startups;