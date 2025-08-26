import React, { useState } from 'react';

const LegalTab = ({ data }) => {
  const [selectedDoc, setSelectedDoc] = useState(null);
  const [showModal, setShowModal] = useState(false);

  const legalDocs = [
    {
      id: 'cgu',
      name: 'Conditions Générales d\'Utilisation',
      filename: 'cgu.md',
      description: 'Règles d\'utilisation du service',
      icon: '📋',
      color: 'blue'
    },
    {
      id: 'cgv',
      name: 'Conditions Générales de Vente',
      filename: 'cgv.md',
      description: 'Conditions de vente et tarification',
      icon: '💳',
      color: 'green'
    },
    {
      id: 'privacy',
      name: 'Politique de Confidentialité',
      filename: 'privacy.md',
      description: 'Gestion des données personnelles',
      icon: '🔒',
      color: 'purple'
    },
    {
      id: 'mentions',
      name: 'Mentions Légales',
      filename: 'mentions.md',
      description: 'Informations légales de l\'entreprise',
      icon: '⚖️',
      color: 'orange'
    }
  ];

  const openDocument = (doc) => {
    setSelectedDoc(doc);
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
    setSelectedDoc(null);
  };

  if (!data || data.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="text-4xl mb-4">⚖️</div>
        <p className="text-gray-500">Aucun document légal disponible</p>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="text-center">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Documents Légaux</h2>
        <p className="text-gray-600">Tous les documents juridiques nécessaires pour votre startup</p>
      </div>

      {/* Documents Grid */}
      <div className="grid md:grid-cols-2 gap-6">
        {legalDocs.map((doc) => {
          const isGenerated = data.includes(doc.filename);
          return (
            <div
              key={doc.id}
              className={`bg-white rounded-lg shadow-sm border p-6 cursor-pointer transition-all hover:shadow-md ${
                isGenerated ? 'border-green-200 bg-green-50' : 'border-gray-200'
              }`}
              onClick={() => isGenerated && openDocument(doc)}
            >
              <div className="flex items-start space-x-4">
                <div className={`text-3xl ${isGenerated ? 'opacity-100' : 'opacity-30'}`}>
                  {doc.icon}
                </div>
                <div className="flex-1">
                  <h3 className={`text-lg font-semibold mb-2 ${
                    isGenerated ? 'text-gray-900' : 'text-gray-400'
                  }`}>
                    {doc.name}
                  </h3>
                  <p className={`text-sm mb-3 ${
                    isGenerated ? 'text-gray-600' : 'text-gray-400'
                  }`}>
                    {doc.description}
                  </p>
                  <div className="flex items-center justify-between">
                    <span className={`text-xs font-medium px-2 py-1 rounded-full ${
                      isGenerated 
                        ? 'bg-green-100 text-green-800' 
                        : 'bg-gray-100 text-gray-500'
                    }`}>
                      {isGenerated ? 'Généré' : 'En attente'}
                    </span>
                    {isGenerated && (
                      <span className="text-blue-600 text-sm font-medium">
                        Cliquer pour consulter →
                      </span>
                    )}
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Status Summary */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-xl font-semibold text-gray-900 mb-4">Statut des Documents</h3>
        <div className="grid md:grid-cols-2 gap-6">
          <div className="text-center">
            <div className="text-3xl font-bold text-green-600 mb-2">
              {data.length}
            </div>
            <div className="text-sm text-gray-500">Documents générés</div>
          </div>
          <div className="text-center">
            <div className="text-3xl font-bold text-blue-600 mb-2">
              {legalDocs.length - data.length}
            </div>
            <div className="text-sm text-gray-500">Documents en attente</div>
          </div>
        </div>
      </div>

      {/* Legal Compliance Info */}
      <div className="bg-blue-50 rounded-lg border border-blue-200 p-6">
        <div className="text-center">
          <div className="text-2xl font-bold text-blue-900 mb-2">
            Conformité Légale
          </div>
          <p className="text-blue-700 mb-4">
            Tous les documents légaux essentiels sont générés automatiquement pour assurer la conformité RGPD et légale
          </p>
          <div className="grid md:grid-cols-3 gap-4 text-sm">
            <div className="flex items-center justify-center">
              <span className="text-green-500 mr-2">✓</span>
              RGPD Compliant
            </div>
            <div className="flex items-center justify-center">
              <span className="text-green-500 mr-2">✓</span>
              Droit Français
            </div>
            <div className="flex items-center justify-center">
              <span className="text-green-500 mr-2">✓</span>
              Mise à jour automatique
            </div>
          </div>
        </div>
      </div>

      {/* Modal pour afficher le document */}
      {showModal && selectedDoc && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-lg max-w-4xl w-full max-h-[90vh] overflow-hidden">
            <div className="flex items-center justify-between p-6 border-b">
              <h3 className="text-xl font-semibold text-gray-900">
                {selectedDoc.name}
              </h3>
              <button
                onClick={closeModal}
                className="text-gray-400 hover:text-gray-600 text-2xl"
              >
                ×
              </button>
            </div>
            <div className="p-6 overflow-y-auto max-h-[70vh]">
              <div className="prose max-w-none">
                <div className="text-center mb-6">
                  <div className="text-4xl mb-2">{selectedDoc.icon}</div>
                  <h4 className="text-lg font-medium text-gray-700">
                    {selectedDoc.filename}
                  </h4>
                  <p className="text-sm text-gray-500">
                    Document généré automatiquement
                  </p>
                </div>
                <div className="bg-gray-50 rounded-lg p-4 text-sm text-gray-600">
                  <p>
                    Ce document a été généré automatiquement par l'IA Business & Legal Engineer.
                    Il est recommandé de le faire valider par un avocat spécialisé avant utilisation.
                  </p>
                </div>
                <div className="mt-6 text-center">
                  <button
                    onClick={() => window.open(`/generated/legal/${selectedDoc.filename}`, '_blank')}
                    className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors"
                  >
                    Ouvrir le document complet
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default LegalTab;