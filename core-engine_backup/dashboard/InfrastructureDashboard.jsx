import React, { useState, useEffect } from 'react';
import { 
  ServerIcon, 
  ChartBarIcon, 
  BellIcon, 
  GlobeAltIcon,
  ExclamationTriangleIcon,
  CheckCircleIcon
} from '@heroicons/react/24/outline';

const InfrastructureDashboard = ({ projectData }) => {
  const [infrastructure, setInfrastructure] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (projectData) {
      setInfrastructure(projectData);
      setLoading(false);
    }
  }, [projectData]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-red-50 border border-red-200 rounded-lg p-6">
        <div className="flex items-center">
          <ExclamationTriangleIcon className="h-6 w-6 text-red-600 mr-2" />
          <h3 className="text-lg font-medium text-red-800">Erreur de chargement</h3>
        </div>
        <p className="mt-2 text-red-700">{error}</p>
      </div>
    );
  }

  if (!infrastructure) {
    return (
      <div className="text-center py-12">
        <ServerIcon className="mx-auto h-12 w-12 text-gray-400" />
        <h3 className="mt-2 text-sm font-medium text-gray-900">Aucune infrastructure</h3>
        <p className="mt-1 text-sm text-gray-500">
          L'infrastructure n'a pas encore été déployée pour ce projet.
        </p>
      </div>
    );
  }

  const { infra, monitoring, alerting } = infrastructure;

  return (
    <div className="space-y-6">
      {/* En-tête du dashboard */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold text-gray-900">Infrastructure</h2>
            <p className="text-gray-600 mt-1">
              Vue d'ensemble de l'infrastructure cloud et du monitoring
            </p>
          </div>
          <div className="flex items-center space-x-2">
            <CheckCircleIcon className="h-6 w-6 text-green-600" />
            <span className="text-sm font-medium text-green-600">Opérationnel</span>
          </div>
        </div>
      </div>

      {/* Grille des 4 cartes principales */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        {/* Carte 1: Cluster Kubernetes */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center">
              <div className="p-2 bg-blue-100 rounded-lg">
                <ServerIcon className="h-6 w-6 text-blue-600" />
              </div>
              <h3 className="ml-3 text-lg font-semibold text-gray-900">Cluster Kubernetes</h3>
            </div>
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
              GKE
            </span>
          </div>
          
          <div className="space-y-3">
            <div>
              <p className="text-sm text-gray-500">Nom du cluster</p>
              <p className="text-lg font-medium text-gray-900">{infra?.cluster || 'N/A'}</p>
            </div>
            
            <div>
              <p className="text-sm text-gray-500">URL de l'application</p>
              <a 
                href={infra?.url || '#'} 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-blue-600 hover:text-blue-800 text-lg font-medium break-all"
              >
                {infra?.url || 'N/A'}
              </a>
            </div>
            
            <div>
              <p className="text-sm text-gray-500">Configuration SSL</p>
              <div className="flex items-center mt-1">
                <CheckCircleIcon className="h-4 w-4 text-green-600 mr-2" />
                <span className="text-sm text-green-600">Certificat actif</span>
              </div>
            </div>
          </div>
        </div>

        {/* Carte 2: Auto-scaling */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center">
              <div className="p-2 bg-green-100 rounded-lg">
                <ChartBarIcon className="h-6 w-6 text-green-600" />
              </div>
              <h3 className="ml-3 text-lg font-semibold text-gray-900">Auto-scaling</h3>
            </div>
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
              HPA
            </span>
          </div>
          
          <div className="space-y-3">
            <div>
              <p className="text-sm text-gray-500">Configuration des pods</p>
              <p className="text-lg font-medium text-gray-900">{infra?.scaling || 'N/A'}</p>
            </div>
            
            <div>
              <p className="text-sm text-gray-500">Seuil CPU</p>
              <p className="text-lg font-medium text-gray-900">70%</p>
            </div>
            
            <div>
              <p className="text-sm text-gray-500">Seuil mémoire</p>
              <p className="text-lg font-medium text-gray-900">80%</p>
            </div>
            
            <div className="pt-2">
              <div className="flex items-center justify-between text-sm">
                <span className="text-gray-500">Pods actifs</span>
                <span className="font-medium text-gray-900">3/20</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2 mt-1">
                <div className="bg-green-600 h-2 rounded-full" style={{ width: '15%' }}></div>
              </div>
            </div>
          </div>
        </div>

        {/* Carte 3: Monitoring */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center">
              <div className="p-2 bg-orange-100 rounded-lg">
                <ChartBarIcon className="h-6 w-6 text-orange-600" />
              </div>
              <h3 className="ml-3 text-lg font-semibold text-gray-900">Monitoring</h3>
            </div>
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-orange-100 text-orange-800">
              Grafana
            </span>
          </div>
          
          <div className="space-y-3">
            <div>
              <p className="text-sm text-gray-500">Dashboard Grafana</p>
              <a 
                href={monitoring?.grafana_url || '#'} 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-orange-600 hover:text-orange-800 text-lg font-medium break-all"
              >
                {monitoring?.grafana_url || 'N/A'}
              </a>
            </div>
            
            <div>
              <p className="text-sm text-gray-500">Dashboards disponibles</p>
              <div className="flex flex-wrap gap-2 mt-1">
                {monitoring?.dashboards?.map((dashboard, index) => (
                  <span 
                    key={index}
                    className="inline-flex items-center px-2 py-1 rounded-md text-xs font-medium bg-orange-100 text-orange-800"
                  >
                    {dashboard}
                  </span>
                )) || ['N/A']}
              </div>
            </div>
            
            <div>
              <p className="text-sm text-gray-500">Métriques collectées</p>
              <p className="text-lg font-medium text-gray-900">{monitoring?.metrics_count || 'N/A'}</p>
            </div>
          </div>
        </div>

        {/* Carte 4: Alertes */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 hover:shadow-md transition-shadow">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center">
              <div className="p-2 bg-red-100 rounded-lg">
                <BellIcon className="h-6 w-6 text-red-600" />
              </div>
              <h3 className="ml-3 text-lg font-semibold text-gray-900">Alertes</h3>
            </div>
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-100 text-red-800">
              {alerting?.alerts?.length || 0} actives
            </span>
          </div>
          
          <div className="space-y-3">
            <div>
              <p className="text-sm text-gray-500">Règles d'alerte</p>
              <div className="space-y-1 mt-1">
                {alerting?.alerts?.slice(0, 3).map((alert, index) => (
                  <div key={index} className="flex items-center text-sm">
                    <div className="w-2 h-2 bg-red-500 rounded-full mr-2"></div>
                    <span className="text-gray-900">{alert}</span>
                  </div>
                )) || ['Aucune alerte']}
                {alerting?.alerts?.length > 3 && (
                  <p className="text-xs text-gray-500">+{alerting.alerts.length - 3} autres...</p>
                )}
              </div>
            </div>
            
            <div>
              <p className="text-sm text-gray-500">Canaux de notification</p>
              <div className="flex flex-wrap gap-2 mt-1">
                {alerting?.channels?.map((channel, index) => (
                  <span 
                    key={index}
                    className="inline-flex items-center px-2 py-1 rounded-md text-xs font-medium bg-red-100 text-red-800"
                  >
                    {channel}
                  </span>
                )) || ['N/A']}
              </div>
            </div>
            
            <div>
              <p className="text-sm text-gray-500">Statut des alertes</p>
              <div className="flex items-center mt-1">
                <CheckCircleIcon className="h-4 w-4 text-green-600 mr-2" />
                <span className="text-sm text-green-600">Système opérationnel</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Section des actions rapides */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Actions rapides</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <button className="flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
            <ServerIcon className="h-4 w-4 mr-2" />
            Redémarrer le cluster
          </button>
          <button className="flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
            <ChartBarIcon className="h-4 w-4 mr-2" />
            Voir les métriques
          </button>
          <button className="flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
            <BellIcon className="h-4 w-4 mr-2" />
            Gérer les alertes
          </button>
        </div>
      </div>
    </div>
  );
};

export default InfrastructureDashboard;