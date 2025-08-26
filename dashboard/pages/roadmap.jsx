import React, { useState, useEffect } from 'react';
import Layout from '../components/Layout';
import RoadmapCard from '../components/RoadmapCard';
import Toast from '../components/Toast';
import { MapIcon, ArrowPathIcon } from '@heroicons/react/24/outline';

const Roadmap = () => {
  const [epics, setEpics] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [showToast, setShowToast] = useState(false);
  const [toastMessage, setToastMessage] = useState('');
  const [toastType, setToastType] = useState('success');

  // Mock data pour la démo - à remplacer par un vrai appel API
  const mockEpics = [
    {
      id: 1,
      title: "Architecture Technique",
      description: "Mise en place de l'infrastructure technique de base",
      status: "completed",
      estimated_hours: 40,
      user_stories: [
        {
          title: "Setup de l'environnement de développement",
          description: "Configuration de l'environnement local avec Docker et dépendances",
          acceptance_criteria: [
            "Docker Compose fonctionne localement",
            "Toutes les dépendances sont installées",
            "Tests unitaires passent"
          ]
        },
        {
          title: "Configuration de la base de données",
          description: "Mise en place de Supabase avec schémas et migrations",
          acceptance_criteria: [
            "Base de données accessible",
            "Tables créées selon le schéma",
            "Index et contraintes configurés"
          ]
        }
      ]
    },
    {
      id: 2,
      title: "Authentification et Sécurité",
      description: "Système d'authentification complet avec gestion des rôles",
      status: "in_progress",
      estimated_hours: 32,
      user_stories: [
        {
          title: "Intégration Supabase Auth",
          description: "Configuration de l'authentification avec Supabase",
          acceptance_criteria: [
            "Inscription/connexion fonctionne",
            "Gestion des sessions JWT",
            "Protection des routes API"
          ]
        }
      ]
    },
    {
      id: 3,
      title: "Interface Utilisateur",
      description: "Développement de l'interface utilisateur responsive",
      status: "pending",
      estimated_hours: 48,
      user_stories: [
        {
          title: "Design System",
          description: "Création d'un système de design cohérent",
          acceptance_criteria: [
            "Composants réutilisables",
            "Thème cohérent avec la charte",
            "Responsive sur tous les écrans"
          ]
        }
      ]
    }
  ];

  useEffect(() => {
    // Simuler un chargement
    const timer = setTimeout(() => {
      setEpics(mockEpics);
      setIsLoading(false);
    }, 1000);

    return () => clearTimeout(timer);
  }, []);

  const refreshRoadmap = async () => {
    setIsLoading(true);
    try {
      // Ici vous feriez un appel API pour rafraîchir la roadmap
      await new Promise(resolve => setTimeout(resolve, 1000));
      setToastMessage('Roadmap mise à jour avec succès!');
      setToastType('success');
      setShowToast(true);
    } catch (error) {
      setToastMessage('Erreur lors de la mise à jour');
      setToastType('error');
      setShowToast(true);
    } finally {
      setIsLoading(false);
    }
  };

  if (isLoading) {
    return (
      <Layout>
        <div className="flex items-center justify-center h-64">
          <div className="text-center">
            <div className="w-8 h-8 border-4 border-accent border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
            <p className="text-gray-600">Chargement de la roadmap...</p>
          </div>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="mb-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Roadmap du Projet</h1>
            <p className="text-gray-600 mt-2">
              Vue d'ensemble des épics et user stories générés par l'IA
            </p>
          </div>
          <button
            onClick={refreshRoadmap}
            disabled={isLoading}
            className="btn-secondary flex items-center space-x-2"
          >
            <ArrowPathIcon className="w-4 h-4" />
            <span>Actualiser</span>
          </button>
        </div>
      </div>

      {epics.length === 0 ? (
        <div className="text-center py-12">
          <MapIcon className="w-16 h-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">Aucune roadmap disponible</h3>
          <p className="text-gray-600">
            Générez votre première startup depuis la page d'accueil pour voir la roadmap ici.
          </p>
        </div>
      ) : (
        <div className="grid gap-6">
          {epics.map((epic) => (
            <RoadmapCard key={epic.id} epic={epic} />
          ))}
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

export default Roadmap;