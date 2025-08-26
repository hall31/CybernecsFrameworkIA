import React from "react";

export default function AgentCard({ name, enabled, status, toggleAgent }) {
  const statusConfig = {
    active: { color: "bg-green-100 text-green-700", icon: "🟢", label: "Actif" },
    disabled: { color: "bg-yellow-100 text-yellow-700", icon: "🟡", label: "Désactivé" },
    error: { color: "bg-red-100 text-red-700", icon: "🔴", label: "Erreur" }
  };

  const currentStatus = statusConfig[status] || statusConfig.disabled;

  return (
    <div className="p-6 bg-white rounded-xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow duration-200">
      <div className="flex items-center justify-between">
        <div className="flex-1">
          <h3 className="font-semibold text-gray-900 text-lg mb-2">{name}</h3>
          <div className="flex items-center space-x-2">
            <span className={`px-3 py-1 text-xs font-medium rounded-full ${currentStatus.color}`}>
              {currentStatus.icon} {currentStatus.label}
            </span>
          </div>
        </div>
        
        <label className="flex items-center cursor-pointer">
          <input
            type="checkbox"
            checked={enabled}
            onChange={() => toggleAgent(name)}
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
      </div>
    </div>
  );
}