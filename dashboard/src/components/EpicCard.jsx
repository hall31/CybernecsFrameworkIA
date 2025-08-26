import React from "react";

export default function EpicCard({ id, name, enabled, status, toggleEpic, runEpic }) {
  const statusConfig = {
    running: { color: "bg-blue-100 text-blue-700", icon: "🔄", label: "En cours" },
    done: { color: "bg-green-100 text-green-700", icon: "✅", label: "Terminé" },
    disabled: { color: "bg-yellow-100 text-yellow-700", icon: "⏸️", label: "Désactivé" },
    failed: { color: "bg-red-100 text-red-700", icon: "❌", label: "Échec" },
    pending: { color: "bg-gray-100 text-gray-700", icon: "⏳", label: "En attente" }
  };

  const currentStatus = statusConfig[status] || statusConfig.disabled;

  return (
    <div className="p-6 bg-white rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow duration-200">
      <div className="flex-1 mb-4">
        <h3 className="font-semibold text-gray-900 text-lg mb-2">{name}</h3>
        <div className="flex items-center space-x-2">
          <span className={`px-3 py-1 text-xs font-medium rounded-full ${currentStatus.color}`}>
            {currentStatus.icon} {currentStatus.label}
          </span>
        </div>
      </div>
      
      <div className="flex justify-between items-center">
        <label className="flex items-center cursor-pointer">
          <input
            type="checkbox"
            checked={enabled}
            onChange={() => toggleEpic(id)}
            className="hidden"
          />
          <div className={`relative inline-flex w-11 h-6 items-center rounded-full transition-colors duration-200 ease-in-out ${
            enabled ? "bg-blue-600" : "bg-gray-300"
          }`}>
            <span className={`inline-block w-4 h-4 transform transition-transform duration-200 ease-in-out bg-white rounded-full shadow-sm ${
              enabled ? "translate-x-6" : "translate-x-1"
            }`} />
          </div>
        </label>
        
        <button
          onClick={() => runEpic(id)}
          disabled={!enabled}
          className={`px-4 py-2 text-sm font-medium rounded-lg transition-all duration-200 ${
            enabled 
              ? "bg-blue-600 text-white hover:bg-blue-700 hover:shadow-md transform hover:scale-105" 
              : "bg-gray-300 text-gray-500 cursor-not-allowed"
          }`}
        >
          {enabled ? "▶️ Run" : "⏸️ Disabled"}
        </button>
      </div>
    </div>
  );
}