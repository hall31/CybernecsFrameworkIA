import React from 'react';

const FrontendTab = ({ data }) => {
  if (!data) {
    return (
      <div className="text-center py-12">
        <div className="text-4xl mb-4">🎨</div>
        <p className="text-gray-500">Aucune architecture frontend disponible</p>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="text-center">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Architecture Frontend</h2>
        <p className="text-gray-600">Technologies et outils côté client</p>
      </div>

      {/* Framework */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Framework Principal</h3>
        <div className="text-center">
          <div className="text-4xl mb-4">⚛️</div>
          <div className="text-2xl font-bold text-blue-600 mb-2">{data.framework}</div>
          <p className="text-gray-600">Framework moderne et performant</p>
        </div>
      </div>

      {/* State Management */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Gestion d'État</h3>
        <div className="text-center">
          <div className="text-4xl mb-4">🔄</div>
          <div className="text-xl font-medium text-gray-900 mb-2">{data.state_management}</div>
          <p className="text-gray-600">Gestion centralisée de l'état de l'application</p>
        </div>
      </div>

      {/* Styling */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Styling et Design</h3>
        <div className="grid md:grid-cols-2 gap-6">
          {data.styling?.split(' + ').map((style, index) => (
            <div key={index} className="text-center p-4 bg-gray-50 rounded-lg">
              <div className="text-2xl mb-2">🎨</div>
              <div className="font-medium text-gray-900">{style}</div>
              <div className="text-sm text-gray-500">
                {style.includes('Tailwind') ? 'Framework CSS utilitaire' : 'Composants UI accessibles'}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Testing */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Tests</h3>
        <div className="grid md:grid-cols-2 gap-6">
          {data.testing?.split(' + ').map((test, index) => (
            <div key={index} className="text-center p-4 bg-gray-50 rounded-lg">
              <div className="text-2xl mb-2">🧪</div>
              <div className="font-medium text-gray-900">{test}</div>
              <div className="text-sm text-gray-500">
                {test.includes('Jest') ? 'Framework de tests unitaires' : 'Tests de composants React'}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Build Tool */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Outil de Build</h3>
        <div className="text-center">
          <div className="text-4xl mb-4">⚡</div>
          <div className="text-xl font-medium text-gray-900 mb-2">{data.build_tool}</div>
          <p className="text-gray-600">Build tool ultra-rapide et moderne</p>
        </div>
      </div>

      {/* Benefits */}
      <div className="bg-green-50 rounded-lg border border-green-200 p-6">
        <h3 className="text-xl font-semibold text-green-900 mb-4">Avantages de cette Architecture</h3>
        <div className="grid md:grid-cols-2 gap-6">
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-green-900">Performance</h4>
              <p className="text-sm text-green-700">Rendu optimisé et chargement rapide</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-green-900">Maintenance</h4>
              <p className="text-sm text-green-700">Code modulaire et réutilisable</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-green-900">UX</h4>
              <p className="text-sm text-green-700">Interface utilisateur moderne et accessible</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-green-900">SEO</h4>
              <p className="text-sm text-green-700">Rendu côté serveur pour le référencement</p>
            </div>
          </div>
        </div>
      </div>

      {/* Development Experience */}
      <div className="bg-blue-50 rounded-lg border border-blue-200 p-6">
        <h3 className="text-xl font-semibold text-blue-900 mb-4">Expérience Développeur</h3>
        <div className="grid md:grid-cols-3 gap-4 text-center">
          <div>
            <div className="text-2xl mb-2">🚀</div>
            <div className="font-medium text-blue-900">Hot Reload</div>
            <div className="text-sm text-blue-700">Rechargement instantané</div>
          </div>
          <div>
            <div className="text-2xl mb-2">🔧</div>
            <div className="font-medium text-blue-900">DevTools</div>
            <div className="text-sm text-blue-700">Outils de développement</div>
          </div>
          <div>
            <div className="text-2xl mb-2">📚</div>
            <div className="font-medium text-blue-900">Documentation</div>
            <div className="text-sm text-blue-700">Ressources complètes</div>
          </div>
        </div>
      </div>

      {/* Summary */}
      <div className="bg-blue-50 rounded-lg border border-blue-200 p-6">
        <div className="text-center">
          <div className="text-2xl font-bold text-blue-900 mb-2">
            Frontend Moderne et Performant
          </div>
          <p className="text-blue-700">
            {data.framework} avec {data.state_management} et {data.build_tool} pour une expérience utilisateur optimale
          </p>
        </div>
      </div>
    </div>
  );
};

export default FrontendTab;