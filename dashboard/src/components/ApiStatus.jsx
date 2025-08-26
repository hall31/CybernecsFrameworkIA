import React, { useState, useEffect } from "react";
import { FaCheckCircle, FaTimesCircle, FaSpinner } from "react-icons/fa";
import { API_CONFIG } from "../config";

const ApiStatus = () => {
  const [status, setStatus] = useState({
    marketplace: 'checking',
    startup: 'checking'
  });

  useEffect(() => {
    checkApiStatus();
  }, []);

  const checkApiStatus = async () => {
    // Vérifier l'API Marketplace
    try {
      const response = await fetch(`${API_CONFIG.MARKETPLACE_API}${API_CONFIG.ENDPOINTS.HEALTH}`);
      const data = await response.json();
      setStatus(prev => ({
        ...prev,
        marketplace: data.status === 'healthy' ? 'connected' : 'error'
      }));
    } catch (error) {
      setStatus(prev => ({
        ...prev,
        marketplace: 'error'
      }));
    }

    // Vérifier l'API Startup (optionnel)
    try {
      const response = await fetch(`${API_CONFIG.STARTUP_API}/health`);
      const data = await response.json();
      setStatus(prev => ({
        ...prev,
        startup: 'connected'
      }));
    } catch (error) {
      setStatus(prev => ({
        ...prev,
        startup: 'error'
      }));
    }
  };

  const getStatusIcon = (status) => {
    switch (status) {
      case 'connected':
        return <FaCheckCircle className="text-green-500" />;
      case 'error':
        return <FaTimesCircle className="text-red-500" />;
      case 'checking':
        return <FaSpinner className="text-blue-500 animate-spin" />;
      default:
        return <FaTimesCircle className="text-gray-500" />;
    }
  };

  const getStatusText = (status) => {
    switch (status) {
      case 'connected':
        return 'Connecté';
      case 'error':
        return 'Erreur';
      case 'checking':
        return 'Vérification...';
      default:
        return 'Inconnu';
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-sm border p-4">
      <h3 className="text-lg font-semibold text-gray-800 mb-3">🔌 Statut des APIs</h3>
      
      <div className="space-y-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="text-sm font-medium text-gray-700">Marketplace API</span>
            <span className="text-xs text-gray-500">({API_CONFIG.MARKETPLACE_API})</span>
          </div>
          <div className="flex items-center gap-2">
            {getStatusIcon(status.marketplace)}
            <span className={`text-sm ${
              status.marketplace === 'connected' ? 'text-green-600' :
              status.marketplace === 'error' ? 'text-red-600' : 'text-blue-600'
            }`}>
              {getStatusText(status.marketplace)}
            </span>
          </div>
        </div>
        
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="text-sm font-medium text-gray-700">Startup API</span>
            <span className="text-xs text-gray-500">({API_CONFIG.STARTUP_API})</span>
          </div>
          <div className="flex items-center gap-2">
            {getStatusIcon(status.startup)}
            <span className={`text-sm ${
              status.startup === 'connected' ? 'text-green-600' :
              status.startup === 'error' ? 'text-red-600' : 'text-blue-600'
            }`}>
              {getStatusText(status.startup)}
            </span>
          </div>
        </div>
      </div>
      
      <button 
        onClick={checkApiStatus}
        className="mt-4 w-full px-3 py-2 bg-blue-600 text-white text-sm rounded-lg hover:bg-blue-700 transition"
      >
        🔄 Actualiser le statut
      </button>
    </div>
  );
};

export default ApiStatus;