import React, { useState } from 'react';

const GrowthTab = ({ data }) => {
  const [selectedCategory, setSelectedCategory] = useState('all');

  if (!data) {
    return (
      <div className="text-center py-12">
        <div className="text-4xl mb-4">📈</div>
        <p className="text-gray-500">Aucune stratégie de croissance disponible</p>
      </div>
    );
  }

  const categories = [
    { id: 'all', name: 'Tous', icon: '📊' },
    { id: 'crm', name: 'CRM & Sales', icon: '👥' },
    { id: 'marketing', name: 'Marketing Automation', icon: '📧' },
    { id: 'analytics', name: 'Analytics & Tracking', icon: '📊' },
    { id: 'advertising', name: 'Advertising', icon: '📢' }
  ];

  const getPriorityColor = (priority) => {
    switch (priority?.toLowerCase()) {
      case 'high': return 'bg-red-100 text-red-800';
      case 'medium': return 'bg-yellow-100 text-yellow-800';
      case 'low': return 'bg-green-100 text-green-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  const getChannelTypeColor = (type) => {
    switch (type) {
      case 'Paid Social': return 'bg-blue-100 text-blue-800';
      case 'Paid Search': return 'bg-green-100 text-green-800';
      case 'Outbound': return 'bg-purple-100 text-purple-800';
      case 'Organic': return 'bg-orange-100 text-orange-800';
      case 'Strategic': return 'bg-indigo-100 text-indigo-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="text-center">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Stratégie de Croissance</h2>
        <p className="text-gray-600">Plan complet d'acquisition et de rétention utilisateurs</p>
      </div>

      {/* Growth Overview */}
      <div className="grid md:grid-cols-3 gap-6">
        <div className="bg-white rounded-lg shadow-sm border p-6 text-center">
          <div className="text-3xl font-bold text-blue-600 mb-2">
            {data.total_budget}
          </div>
          <div className="text-sm text-gray-500">Budget mensuel total</div>
        </div>
        <div className="bg-white rounded-lg shadow-sm border p-6 text-center">
          <div className="text-3xl font-bold text-green-600 mb-2">
            {data.expected_growth}
          </div>
          <div className="text-sm text-gray-500">Croissance attendue</div>
        </div>
        <div className="bg-white rounded-lg shadow-sm border p-6 text-center">
          <div className="text-3xl font-bold text-purple-600 mb-2">
            {data.channels?.length || 0}
          </div>
          <div className="text-sm text-gray-500">Canaux d'acquisition</div>
        </div>
      </div>

      {/* Acquisition Channels */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Canaux d'Acquisition</h3>
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-gray-200">
            <thead className="bg-gray-50">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Canal
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Type
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Budget
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  CAC Attendu
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Priorité
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {data.channels?.map((channel, index) => (
                <tr key={index} className="hover:bg-gray-50">
                  <td className="px-6 py-4 whitespace-nowrap">
                    <div className="text-sm font-medium text-gray-900">{channel.name}</div>
                    <div className="text-sm text-gray-500">{channel.target}</div>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getChannelTypeColor(channel.type)}`}>
                      {channel.type}
                    </span>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                    {channel.budget}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                    {channel.expected_cac}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getPriorityColor(channel.priority)}`}>
                      {channel.priority}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* KPIs */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">KPIs de Croissance</h3>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {data.kpis?.map((kpi, index) => (
            <div key={index} className="border rounded-lg p-4">
              <div className="flex items-start justify-between mb-3">
                <h4 className="text-sm font-medium text-gray-900">{kpi.metric}</h4>
                <span className="text-xs text-gray-500">{kpi.frequency}</span>
              </div>
              <div className="text-2xl font-bold text-blue-600 mb-2">{kpi.target}</div>
              <div className="text-xs text-gray-500 mb-2">Formule: {kpi.formula}</div>
              <div className="text-xs text-gray-400">Valeur actuelle: {kpi.current}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Tools by Category */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Outils Recommandés</h3>
        
        {/* Category Filter */}
        <div className="flex space-x-2 mb-6 overflow-x-auto">
          {categories.map((category) => (
            <button
              key={category.id}
              onClick={() => setSelectedCategory(category.id)}
              className={`flex items-center space-x-2 px-4 py-2 rounded-lg text-sm font-medium whitespace-nowrap transition-colors ${
                selectedCategory === category.id
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              <span>{category.icon}</span>
              <span>{category.name}</span>
            </button>
          ))}
        </div>

        {/* Tools Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {data.suggested_tools?.map((category) => {
            if (selectedCategory !== 'all' && category.category.toLowerCase().includes(selectedCategory)) {
              return null;
            }
            return (
              <div key={category.category} className="border rounded-lg p-4">
                <h4 className="text-lg font-medium text-gray-900 mb-3">{category.category}</h4>
                <div className="space-y-3">
                  {category.tools.map((tool, index) => (
                    <div key={index} className="border-l-4 border-blue-500 pl-3">
                      <div className="flex items-center justify-between mb-1">
                        <span className="text-sm font-medium text-gray-900">{tool.name}</span>
                        <span className="text-xs text-gray-500">{tool.price}</span>
                      </div>
                      <p className="text-xs text-gray-600">{tool.use_case}</p>
                    </div>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Retention Strategy */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Stratégie de Rétention</h3>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {Object.entries(data.retention_strategy || {}).map(([key, value]) => (
            <div key={key} className="text-center">
              <div className="text-2xl mb-2">🎯</div>
              <h4 className="text-sm font-medium text-gray-900 mb-2 capitalize">
                {key.replace(/_/g, ' ')}
              </h4>
              <p className="text-xs text-gray-600">{value}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Growth Roadmap */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Roadmap de Croissance</h3>
        <div className="space-y-4">
          {Object.entries(data.growth_roadmap || {}).map(([period, description]) => (
            <div key={period} className="flex items-start space-x-4">
              <div className="flex-shrink-0 w-24 text-sm font-medium text-blue-600">
                {period.replace(/_/g, ' ')}
              </div>
              <div className="flex-1 text-sm text-gray-700">{description}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Summary */}
      <div className="bg-green-50 rounded-lg border border-green-200 p-6">
        <div className="text-center">
          <div className="text-2xl font-bold text-green-900 mb-2">
            Stratégie de Croissance Complète
          </div>
          <p className="text-green-700">
            Plan d'acquisition utilisateurs optimisé avec {data.channels?.length || 0} canaux, 
            {data.kpis?.length || 0} KPIs de suivi et {data.suggested_tools?.reduce((acc, cat) => acc + cat.tools.length, 0) || 0} outils recommandés
          </p>
        </div>
      </div>
    </div>
  );
};

export default GrowthTab;