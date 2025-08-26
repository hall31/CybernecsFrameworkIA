import React from 'react';

const StackTab = ({ data }) => {
  if (!data) {
    return (
      <div className="text-center py-12">
        <div className="text-4xl mb-4">⚙️</div>
        <p className="text-gray-500">Aucune stack technique disponible</p>
      </div>
    );
  }

  const stackCategories = [
    { key: 'frontend', name: 'Frontend', icon: '🎨', color: 'blue' },
    { key: 'backend', name: 'Backend', icon: '🔧', color: 'green' },
    { key: 'infrastructure', name: 'Infrastructure', icon: '☁️', color: 'purple' },
    { key: 'monitoring', name: 'Monitoring', icon: '📊', color: 'orange' }
  ];

  const getColorClasses = (color) => {
    const colors = {
      blue: 'bg-blue-50 border-blue-200 text-blue-800',
      green: 'bg-green-50 border-green-200 text-green-800',
      purple: 'bg-purple-50 border-purple-200 text-purple-800',
      orange: 'bg-orange-50 border-orange-200 text-orange-800'
    };
    return colors[color] || colors.blue;
  };

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="text-center">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Stack Technique</h2>
        <p className="text-gray-600">Technologies et outils recommandés pour votre startup</p>
      </div>

      {/* Stack Overview */}
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stackCategories.map((category) => (
          <div key={category.key} className="bg-white rounded-lg shadow-sm border p-6 text-center">
            <div className="text-3xl mb-3">{category.icon}</div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">{category.name}</h3>
            <div className="text-2xl font-bold text-blue-600">
              {data[category.key]?.length || 0}
            </div>
            <div className="text-sm text-gray-500">technologies</div>
          </div>
        ))}
      </div>

      {/* Detailed Stack */}
      <div className="grid md:grid-cols-2 gap-8">
        {stackCategories.map((category) => (
          <div key={category.key} className="bg-white rounded-lg shadow-sm border p-6">
            <div className="flex items-center space-x-3 mb-4">
              <div className="text-2xl">{category.icon}</div>
              <h3 className="text-xl font-semibold text-gray-900">{category.name}</h3>
            </div>
            
            <div className="space-y-3">
              {data[category.key]?.map((tech, index) => (
                <div key={index} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                  <span className="text-sm font-medium text-gray-700">{tech}</span>
                    ✔️
                  </span>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* Technology Benefits */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Avantages de cette Stack</h3>
        <div className="grid md:grid-cols-2 gap-6">
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-gray-900">Scalabilité</h4>
              <p className="text-sm text-gray-600">Architecture conçue pour supporter la croissance</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-gray-900">Performance</h4>
              <p className="text-sm text-gray-600">Technologies optimisées pour la vitesse</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-gray-900">Maintenance</h4>
              <p className="text-sm text-gray-600">Code maintenable et évolutif</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <span className="text-green-500 text-xl">✓</span>
            <div>
              <h4 className="font-medium text-gray-900">Sécurité</h4>
              <p className="text-sm text-gray-600">Standards de sécurité élevés</p>
            </div>
          </div>
        </div>
      </div>

      {/* Summary */}
      <div className="bg-blue-50 rounded-lg border border-blue-200 p-6">
        <div className="text-center">
          <div className="text-2xl font-bold text-blue-900 mb-2">
            Stack Technique Complète
          </div>
          <p className="text-blue-700">
            {Object.values(data).flat().length} technologies sélectionnées pour un développement moderne et efficace
          </p>
        </div>
      </div>
    </div>
  );
};

export default StackTab;