import React from 'react';

const BackendTab = ({ data }) => {
  if (!data) {
    return (
      <div className="text-center py-12">
        <div className="text-4xl mb-4">🔧</div>
        <p className="text-gray-500">Aucune architecture backend disponible</p>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="text-center">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Architecture Backend</h2>
        <p className="text-gray-600">Infrastructure et technologies côté serveur</p>
      </div>

      {/* Architecture Overview */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Architecture Globale</h3>
        <div className="text-center">
          <div className="text-4xl mb-4">🏗️</div>
          <div className="text-2xl font-bold text-blue-600 mb-2">{data.architecture}</div>
          <p className="text-gray-600">Architecture moderne et scalable</p>
        </div>
      </div>

      {/* Database */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Base de Données</h3>
        <div className="grid md:grid-cols-2 gap-6">
          {data.database?.split(' + ').map((db, index) => (
            <div key={index} className="flex items-center space-x-3 p-4 bg-gray-50 rounded-lg">
              <div className="text-2xl">🗄️</div>
              <div>
                <div className="font-medium text-gray-900">{db}</div>
                <div className="text-sm text-gray-500">
                  {db.includes('PostgreSQL') ? 'Base relationnelle principale' : 'Cache et sessions'}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* API */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">API</h3>
        <div className="grid md:grid-cols-2 gap-6">
          {data.api?.split(' + ').map((api, index) => (
            <div key={index} className="text-center p-4 bg-gray-50 rounded-lg">
              <div className="text-2xl mb-2">🔌</div>
              <div className="font-medium text-gray-900">{api}</div>
              <div className="text-sm text-gray-500">
                {api === 'REST' ? 'API RESTful standard' : 'API GraphQL moderne'}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Security */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Sécurité</h3>
        <div className="grid md:grid-cols-3 gap-4">
          {data.security?.map((security, index) => (
            <div key={index} className="text-center p-4 bg-gray-50 rounded-lg">
              <div className="text-2xl mb-2">🔒</div>
              <div className="font-medium text-gray-900">{security}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Deployment */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Déploiement</h3>
        <div className="text-center">
          <div className="text-4xl mb-4">🚀</div>
          <div className="text-xl font-medium text-gray-900 mb-2">{data.deployment}</div>
          <p className="text-gray-600">Pipeline d'intégration et déploiement continu</p>
        </div>
      </div>

      {/* Benefits */}
      <div className="bg-green-50 rounded-lg border border-green-200 p-6">
        <h3 className="text-xl font-semibold text-green-900 mb-4">Avantages de cette Architecture</h3>
        <div className="grid md:grid-cols-2 gap-6">
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-green-900">Scalabilité</h4>
              <p className="text-sm text-green-700">Architecture microservices extensible</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-green-900">Performance</h4>
              <p className="text-sm text-green-700">Optimisations et cache intégrés</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-green-900">Sécurité</h4>
              <p className="text-sm text-green-700">Standards de sécurité élevés</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-green-900">Maintenance</h4>
              <p className="text-sm text-green-700">Code modulaire et testable</p>
            </div>
          </div>
        </div>
      </div>

      {/* Summary */}
      <div className="bg-blue-50 rounded-lg border border-blue-200 p-6">
        <div className="text-center">
          <div className="text-2xl font-bold text-blue-900 mb-2">
            Backend Robuste et Moderne
          </div>
          <p className="text-blue-700">
            Architecture {data.architecture} avec {data.security?.length || 0} couches de sécurité et déploiement automatisé
          </p>
        </div>
      </div>
    </div>
  );
};

export default BackendTab;