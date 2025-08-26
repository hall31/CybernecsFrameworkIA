import React from 'react';

const MarketingTab = ({ data }) => {
  if (!data) {
    return (
      <div className="text-center py-12">
        <div className="text-4xl mb-4">📢</div>
        <p className="text-gray-500">Aucune stratégie marketing disponible</p>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="text-center">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Stratégie Marketing</h2>
        <p className="text-gray-600">Plan d'acquisition et de croissance des utilisateurs</p>
      </div>

      {/* Positioning */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Positionnement</h3>
        <div className="text-center">
          <div className="text-4xl mb-4">🎯</div>
          <div className="text-xl font-medium text-gray-900 mb-2">{data.positioning}</div>
          <p className="text-gray-600">Proposition de valeur claire et différenciante</p>
        </div>
      </div>

      {/* Target Audience */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Audience Cible</h3>
        <div className="text-center">
          <div className="text-4xl mb-4">👥</div>
          <div className="text-xl font-medium text-gray-900 mb-2">{data.target_audience}</div>
          <p className="text-gray-600">Segment d'utilisateurs prioritaire</p>
        </div>
      </div>

      {/* Channels */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Canaux Marketing</h3>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
          {data.channels?.map((channel, index) => (
            <div key={index} className="text-center p-4 bg-gray-50 rounded-lg">
              <div className="text-2xl mb-2">
                {channel.includes('Content') ? '📝' : 
                 channel.includes('SEO') ? '🔍' : 
                 channel.includes('Social') ? '📱' : 
                 channel.includes('Email') ? '📧' : '📢'}
              </div>
              <div className="font-medium text-gray-900">{channel}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Budget */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Budget Marketing</h3>
        <div className="text-center">
          <div className="text-4xl mb-4">💰</div>
          <div className="text-3xl font-bold text-blue-600 mb-2">{data.budget}</div>
          <p className="text-gray-600">Budget mensuel alloué au marketing</p>
        </div>
      </div>

      {/* Goals */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Objectifs Marketing</h3>
        <div className="grid md:grid-cols-3 gap-4">
          {data.goals?.map((goal, index) => (
            <div key={index} className="text-center p-4 bg-gray-50 rounded-lg">
              <div className="text-2xl mb-2">
                {goal.includes('Brand') ? '🏷️' : 
                 goal.includes('Lead') ? '🎯' : 
                 goal.includes('Conversion') ? '💎' : '📈'}
              </div>
              <div className="font-medium text-gray-900">{goal}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Marketing Strategy Details */}
      <div className="bg-blue-50 rounded-lg border border-blue-200 p-6">
        <h3 className="text-xl font-semibold text-blue-900 mb-4">Détails de la Stratégie</h3>
        <div className="grid md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-medium text-blue-900 mb-2">Content Marketing</h4>
            <ul className="text-sm text-blue-700 space-y-1">
              <li>• Blog technique et business</li>
              <li>• Webinaires et formations</li>
              <li>• Études de cas et témoignages</li>
              <li>• Infographies et vidéos</li>
            </ul>
          </div>
          <div>
            <h4 className="font-medium text-blue-900 mb-2">SEO & Acquisition</h4>
            <ul className="text-sm text-blue-700 space-y-1">
              <li>• Optimisation on-page</li>
              <li>• Création de contenu long-form</li>
              <li>• Link building stratégique</li>
              <li>• Optimisation technique</li>
            </ul>
          </div>
        </div>
      </div>

      {/* Social Media Strategy */}
      <div className="bg-green-50 rounded-lg border border-green-200 p-6">
        <h3 className="text-xl font-semibold text-green-900 mb-4">Stratégie Réseaux Sociaux</h3>
        <div className="grid md:grid-cols-3 gap-4">
          <div className="text-center">
            <div className="text-2xl mb-2">💼</div>
            <div className="font-medium text-green-900">LinkedIn</div>
            <div className="text-sm text-green-700">B2B et professionnels</div>
          </div>
          <div className="text-center">
            <div className="text-2xl mb-2">🐦</div>
            <div className="font-medium text-green-900">Twitter</div>
            <div className="text-sm text-green-700">Actualités et communauté</div>
          </div>
          <div className="text-center">
            <div className="text-2xl mb-2">📘</div>
            <div className="font-medium text-green-900">Facebook</div>
            <div className="text-sm text-green-700">Awareness et engagement</div>
          </div>
        </div>
      </div>

      {/* Email Marketing */}
      <div className="bg-purple-50 rounded-lg border border-purple-200 p-6">
        <h3 className="text-xl font-semibold text-purple-900 mb-4">Email Marketing</h3>
        <div className="grid md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-medium text-purple-900 mb-2">Séquences d'Onboarding</h4>
            <ul className="text-sm text-purple-700 space-y-1">
              <li>• Email de bienvenue</li>
              <li>• Tutoriels et guides</li>
              <li>• Premiers succès</li>
              <li>• Feedback et amélioration</li>
            </ul>
          </div>
          <div>
            <h4 className="font-medium text-purple-900 mb-2">Campagnes de Rétention</h4>
            <ul className="text-sm text-purple-700 space-y-1">
              <li>• Nouvelles fonctionnalités</li>
              <li>• Conseils et bonnes pratiques</li>
              <li>• Événements et webinaires</li>
              <li>• Offres spéciales</li>
            </ul>
          </div>
        </div>
      </div>

      {/* Success Metrics */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Métriques de Succès</h3>
        <div className="grid md:grid-cols-4 gap-4">
          <div className="text-center p-4 bg-gray-50 rounded-lg">
            <div className="text-2xl font-bold text-blue-600 mb-1">+25%</div>
            <div className="text-sm text-gray-600">Trafic organique</div>
          </div>
          <div className="text-center p-4 bg-gray-50 rounded-lg">
            <div className="text-2xl font-bold text-green-600 mb-1">+40%</div>
            <div className="text-sm text-gray-600">Leads qualifiés</div>
          </div>
          <div className="text-center p-4 bg-gray-50 rounded-lg">
            <div className="text-2xl font-bold text-purple-600 mb-1">+15%</div>
            <div className="text-sm text-gray-600">Taux de conversion</div>
          </div>
          <div className="text-center p-4 bg-gray-50 rounded-lg">
            <div className="text-2xl font-bold text-orange-600 mb-1">+30%</div>
            <div className="text-sm text-gray-600">Brand awareness</div>
          </div>
        </div>
      </div>

      {/* Summary */}
      <div className="bg-blue-50 rounded-lg border border-blue-200 p-6">
        <div className="text-center">
          <div className="text-2xl font-bold text-blue-900 mb-2">
            Stratégie Marketing Complète
          </div>
          <p className="text-blue-700">
            {data.channels?.length || 0} canaux, {data.goals?.length || 0} objectifs clairs et budget de {data.budget} pour une croissance mesurable
          </p>
        </div>
      </div>
    </div>
  );
};

export default MarketingTab;