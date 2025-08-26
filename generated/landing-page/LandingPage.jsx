import React from 'react';

const LandingPage = () => {
  const marketingData = {
  "headline": "L'outil SaaS qui simplifie votre quotidien",
  "tagline": "Simplicité et efficacité au service de votre business",
  "features": [
    "Interface intuitive et moderne",
    "Performance et rapidité garanties",
    "Support client 24/7",
    "Intégrations multiples"
  ],
  "pricing": [
    {
      "plan": "Starter",
      "price": "€19/mois",
      "desc": "Parfait pour démarrer",
      "features": [
        "Fonctionnalités de base",
        "Support email",
        "1 utilisateur"
      ]
    },
    {
      "plan": "Pro",
      "price": "€49/mois",
      "desc": "Pour les équipes en croissance",
      "features": [
        "Toutes les fonctionnalités",
        "Support prioritaire",
        "5 utilisateurs",
        "Analytics avancés"
      ]
    },
    {
      "plan": "Enterprise",
      "price": "Contactez-nous",
      "desc": "Solutions sur mesure",
      "features": [
        "Personnalisation complète",
        "Support dédié",
        "Utilisateurs illimités",
        "API personnalisée"
      ]
    }
  ]
};

  return (
    <div className="min-h-screen bg-white">
      <!-- Hero Section -->
      <section className="bg-gradient-to-br from-blue-50 to-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <div className="flex justify-center mb-8">
              <img 
                src="generated/branding/logo.svg" 
                alt="Logo" 
                className="w-24 h-24"
              />
            </div>
            <h1 className="text-5xl font-bold text-gray-900 mb-6">
              {marketingData.headline}
            </h1>
            <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
              {marketingData.tagline}
            </p>
            <button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-4 px-8 rounded-lg text-lg transition duration-300 transform hover:scale-105">
              Commencer maintenant
            </button>
          </div>
        </div>
      </section>

      <!-- Features Section -->
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              Pourquoi nous choisir ?
            </h2>
            <p className="text-lg text-gray-600">
              Découvrez ce qui nous rend uniques
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {marketingData.features.map((feature, index) => (
              <div key={index} className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition duration-300 border border-gray-100">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4 mx-auto">
                  <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <h3 className="text-lg font-semibold text-gray-900 mb-2">
                  {feature}
                </h3>
                <p className="text-gray-600">
                  Une fonctionnalité exceptionnelle qui vous fera gagner du temps.
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <!-- Pricing Section -->
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold text-gray-900 mb-4">
              Choisissez votre plan
            </h2>
            <p className="text-lg text-gray-600">
              Des options flexibles pour tous les besoins
            </p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {marketingData.pricing.map((plan, index) => (
              <div key={index} className={`bg-white rounded-xl shadow-lg p-8 ${plan.plan === 'Pro' ? 'ring-2 ring-blue-500 transform scale-105' : ''}`}>
                <div className="text-center">
                  <h3 className="text-2xl font-bold text-gray-900 mb-2">
                    {plan.plan}
                  </h3>
                  <div className="text-4xl font-bold text-blue-600 mb-4">
                    {plan.price}
                  </div>
                  <p className="text-gray-600 mb-6">
                    {plan.desc}
                  </p>
                  
                  <ul className="text-left space-y-3 mb-8">
                    {plan.features.map((feature, fIndex) => (
                      <li key={fIndex} className="flex items-center">
                        <svg className="w-5 h-5 text-green-500 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                        </svg>
                        {feature}
                      </li>
                    ))}
                  </ul>
                  
                  <button className={`w-full py-3 px-6 rounded-lg font-semibold transition duration-300 ${plan.plan === 'Pro' 
                    ? 'bg-blue-600 hover:bg-blue-700 text-white' 
                    : 'bg-gray-100 hover:bg-gray-200 text-gray-800'}`}>
                    {plan.plan === 'Enterprise' ? 'Nous contacter' : 'Choisir ce plan'}
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <div className="flex justify-center mb-6">
              <img 
                src="generated/branding/logo.svg" 
                alt="Logo" 
                className="w-16 h-16 filter brightness-0 invert"
              />
            </div>
            <p className="text-lg mb-4">
              Prêt à transformer votre business ?
            </p>
            <p className="text-gray-400 mb-6">
              contact@startup.com
            </p>
            <div className="border-t border-gray-800 pt-6">
              <p className="text-gray-400">
                © 2024 Startup. Tous droits réservés.
              </p>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;