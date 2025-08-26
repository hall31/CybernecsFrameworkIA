import React from 'react';

const RoadmapTab = ({ data }) => {
  if (!data) {
    return (
      <div className="text-center py-12">
        <div className="text-4xl mb-4">🗺️</div>
        <p className="text-gray-500">Aucune roadmap disponible</p>
      </div>
    );
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="text-center">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Roadmap de Développement</h2>
        <p className="text-gray-600">Plan de développement en 3 phases</p>
      </div>

      {/* Roadmap Timeline */}
      <div className="relative">
        {/* Timeline Line */}
        <div className="absolute left-8 top-0 bottom-0 w-0.5 bg-gray-200"></div>
        
        <div className="space-y-12">
          {Object.entries(data).map(([phase, details], index) => (
            <div key={phase} className="relative">
              {/* Phase Dot */}
              <div className="absolute left-6 w-4 h-4 bg-blue-600 rounded-full border-4 border-white shadow-lg transform -translate-x-1/2"></div>
              
              {/* Phase Content */}
              <div className="ml-16">
                <div className="bg-white rounded-lg shadow-sm border p-6">
                  <div className="flex items-center justify-between mb-4">
                    <h3 className="text-xl font-semibold text-gray-900 capitalize">
                      {phase.replace(/([A-Z])/g, ' $1').trim()}
                    </h3>
                    <span className="text-sm font-medium text-blue-600 bg-blue-50 px-3 py-1 rounded-full">
                      {details.duration}
                    </span>
                  </div>
                  
                  {/* Objectives */}
                  <div className="mb-6">
                    <h4 className="text-sm font-medium text-gray-700 mb-3">Objectifs</h4>
                    <div className="grid md:grid-cols-2 gap-3">
                      {details.objectives.map((objective, idx) => (
                        <div key={idx} className="flex items-center space-x-2">
                          <span className="text-green-500">✓</span>
                          <span className="text-sm text-gray-600">{objective}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                  
                  {/* Deliverables */}
                  <div>
                    <h4 className="text-sm font-medium text-gray-700 mb-3">Livrables</h4>
                    <div className="grid md:grid-cols-2 gap-3">
                      {details.deliverables.map((deliverable, idx) => (
                        <div key={idx} className="flex items-center space-x-2">
                          <span className="text-blue-500">📦</span>
                          <span className="text-sm text-gray-600">{deliverable}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Summary */}
      <div className="bg-blue-50 rounded-lg border border-blue-200 p-6">
        <div className="text-center">
          <div className="text-2xl font-bold text-blue-900 mb-2">
            Développement Structuré
          </div>
          <p className="text-blue-700">
            Roadmap en 3 phases avec objectifs clairs et livrables mesurables pour un développement efficace
          </p>
        </div>
      </div>
    </div>
  );
};

export default RoadmapTab;