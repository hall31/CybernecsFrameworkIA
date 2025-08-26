import React from 'react';

const FinanceTab = ({ data }) => {
  if (!data) {
    return (
      <div className="text-center py-12">
        <div className="text-4xl mb-4">💰</div>
        <p className="text-gray-500">Aucune donnée financière disponible</p>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="text-center">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Modèle Financier</h2>
        <p className="text-gray-600">Analyse complète de la viabilité économique</p>
      </div>

      {/* Pricing Models */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Modèles de Pricing</h3>
        <div className="grid md:grid-cols-3 gap-6">
          {data.pricing_models?.map((plan, index) => (
            <div
              key={index}
              className={`border rounded-lg p-6 ${
                plan.plan === 'Pro' 
                  ? 'border-blue-500 bg-blue-50' 
                  : 'border-gray-200 bg-white'
              }`}
            >
              <div className="text-center">
                <h4 className="text-lg font-semibold text-gray-900 mb-2">
                  {plan.plan}
                </h4>
                {plan.price && (
                  <div className="text-3xl font-bold text-blue-600 mb-2">
                    {plan.price}
                  </div>
                )}
                <p className="text-gray-600 mb-4">{plan.desc}</p>
                {plan.features && (
                  <ul className="text-sm text-gray-600 space-y-1">
                    {plan.features.map((feature, idx) => (
                      <li key={idx} className="flex items-center">
                        <span className="text-green-500 mr-2">✓</span>
                        {feature}
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Revenue Projection */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Projections de Revenus</h3>
        <div className="grid md:grid-cols-3 gap-6 mb-6">
          {Object.entries(data.revenue_projection || {}).map(([year, value]) => {
            if (year === 'breakdown') return null;
            return (
              <div key={year} className="text-center">
                <div className="text-2xl font-bold text-blue-600 mb-1">{value}</div>
                <div className="text-sm text-gray-500 uppercase">{year}</div>
              </div>
            );
          })}
        </div>
        
        {/* Breakdown détaillé */}
        {data.revenue_projection?.breakdown && (
          <div className="mt-6">
            <h4 className="text-lg font-medium text-gray-900 mb-3">Répartition par plan</h4>
            <div className="overflow-x-auto">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Plan
                    </th>
                    {Object.keys(data.revenue_projection.breakdown).map((year) => (
                      <th key={year} className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        {year}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {['freemium', 'pro', 'enterprise'].map((plan) => (
                    <tr key={plan}>
                      <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900 capitalize">
                        {plan}
                      </td>
                      {Object.keys(data.revenue_projection.breakdown).map((year) => (
                        <td key={year} className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                          {data.revenue_projection.breakdown[year][plan]}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>

      {/* Financial Metrics */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Métriques Financières</h3>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {Object.entries(data.financial_metrics || {}).map(([key, value]) => (
            <div key={key} className="text-center">
              <div className="text-2xl font-bold text-blue-600 mb-1">{value}</div>
              <div className="text-sm text-gray-500">
                {key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase())}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Cost Structure */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Structure des Coûts</h3>
        <div className="space-y-4">
          {Object.entries(data.cost_structure || {}).map(([category, percentage]) => (
            <div key={category} className="flex items-center justify-between">
              <span className="text-gray-700 capitalize">
                {category.replace(/_/g, ' ')}
              </span>
              <div className="flex items-center space-x-3">
                <div className="w-32 bg-gray-200 rounded-full h-2">
                  <div
                    className="bg-blue-600 h-2 rounded-full"
                    style={{ width: percentage }}
                  ></div>
                </div>
                <span className="text-sm font-medium text-gray-900 w-12 text-right">
                  {percentage}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Summary */}
      <div className="bg-blue-50 rounded-lg border border-blue-200 p-6">
        <div className="text-center">
          <div className="text-2xl font-bold text-blue-900 mb-2">
            Résumé Financier
          </div>
          <p className="text-blue-700">
            Modèle économique viable avec un ROI attendu sous 18 mois et une structure de coûts équilibrée
          </p>
        </div>
      </div>
    </div>
  );
};

export default FinanceTab;