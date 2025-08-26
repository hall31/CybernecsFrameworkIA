import React, { useState } from 'react';
import { useRouter } from 'next/router';
import Layout from '../components/Layout';
import Toast from '../components/Toast';
import { RocketLaunchIcon, LightBulbIcon } from '@heroicons/react/24/outline';

const Home = () => {
  const [idea, setIdea] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showToast, setShowToast] = useState(false);
  const [toastMessage, setToastMessage] = useState('');
  const [toastType, setToastType] = useState('success');
  const router = useRouter();

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!idea.trim()) {
      setToastMessage('Veuillez entrer une idée de startup');
      setToastType('error');
      setShowToast(true);
      return;
    }

    setIsLoading(true);

    try {
      const apiBaseUrl = process.env.NEXT_PUBLIC_API_BASE_URL;
      const response = await fetch(`${apiBaseUrl}/create-startup`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ idea: idea.trim() }),
      });

      if (response.ok) {
        const result = await response.json();
        setToastMessage('Startup générée avec succès!');
        setToastType('success');
        setShowToast(true);
        
        // Rediriger vers la roadmap après un délai
        setTimeout(() => {
          router.push('/roadmap');
        }, 1500);
      } else {
        throw new Error('Erreur lors de la création');
      }
    } catch (error) {
      console.error('Error:', error);
      setToastMessage('Erreur lors de la création de la startup');
      setToastType('error');
      setShowToast(true);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Layout>
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-12">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-accent rounded-full mb-6">
            <RocketLaunchIcon className="w-8 h-8 text-white" />
          </div>
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Lancez votre Startup en quelques clics
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Décrivez votre idée et notre IA CEO générera automatiquement une roadmap complète avec des épics, user stories et estimations.
          </p>
        </div>

        <div className="card max-w-2xl mx-auto">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label htmlFor="idea" className="block text-sm font-medium text-gray-700 mb-2">
                Votre idée de startup
              </label>
              <div className="relative">
                <LightBulbIcon className="absolute left-3 top-3 w-5 h-5 text-gray-400" />
                <textarea
                  id="idea"
                  value={idea}
                  onChange={(e) => setIdea(e.target.value)}
                  placeholder="Ex: Une plateforme SaaS pour automatiser la génération de leads B2B avec l'IA..."
                  className="input-field pl-10 resize-none"
                  rows={4}
                  disabled={isLoading}
                />
              </div>
              <p className="mt-2 text-sm text-gray-500">
                Soyez aussi détaillé que possible pour obtenir les meilleurs résultats.
              </p>
            </div>

            <button
              type="submit"
              disabled={isLoading || !idea.trim()}
              className="btn-primary w-full flex items-center justify-center space-x-2 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isLoading ? (
                <>
                  <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                  <span>Génération en cours...</span>
                </>
              ) : (
                <>
                  <RocketLaunchIcon className="w-5 h-5" />
                  <span>Lancer la génération</span>
                </>
              )}
            </button>
          </form>
        </div>

        <div className="mt-12 grid md:grid-cols-3 gap-6">
          <div className="text-center">
            <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">🚀</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">Génération IA</h3>
            <p className="text-gray-600">Notre CEO Agent analyse votre idée et génère une roadmap complète</p>
          </div>
          
          <div className="text-center">
            <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">📋</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">Roadmap Structurée</h3>
            <p className="text-gray-600">Épics, user stories et estimations de temps détaillées</p>
          </div>
          
          <div className="text-center">
            <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">⚡</span>
            </div>
            <h3 className="text-lg font-semibold text-gray-900 mb-2">Déploiement Rapide</h3>
            <p className="text-gray-600">Prêt à développer en quelques minutes, pas en mois</p>
          </div>
        </div>
      </div>

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

export default Home;