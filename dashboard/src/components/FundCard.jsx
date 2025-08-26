import React from "react";
import { FaChartPie, FaExternalLinkAlt, FaEye, FaEuroSign } from "react-icons/fa";

const FundCard = ({ fund, onSelect }) => {
  const getStatusColor = (status) => {
    switch (status) {
      case "active":
        return "bg-green-100 text-green-800";
      case "inactive":
        return "bg-gray-100 text-gray-800";
      default:
        return "bg-blue-100 text-blue-800";
    }
  };

  const getStatusIcon = (status) => {
    switch (status) {
      case "active":
        return "🟢";
      case "inactive":
        return "⚫";
      default:
        return "🔵";
    }
  };

  return (
    <div className="bg-white rounded-2xl shadow-lg hover:shadow-xl transition-all duration-200 border border-gray-100 overflow-hidden group">
      {/* Header */}
      <div className="p-6 border-b border-gray-100">
        <div className="flex justify-between items-start mb-3">
          <div>
            <h3 className="text-xl font-bold text-gray-900 group-hover:text-blue-600 transition-colors">
              {fund.fund_symbol}
            </h3>
            <p className="text-sm text-gray-600">Fonds IA Startup</p>
          </div>
          <span className={`px-3 py-1 rounded-full text-xs font-medium ${getStatusColor(fund.status)}`}>
            {getStatusIcon(fund.status)} {fund.status}
          </span>
        </div>
        
        {/* NAV */}
        <div className="flex items-center gap-2">
          <FaEuroSign className="text-green-600" />
          <span className="text-2xl font-bold text-gray-900">{fund.nav}</span>
        </div>
      </div>

      {/* Composition Preview */}
      <div className="p-6">
        <div className="flex items-center gap-2 mb-3">
          <FaChartPie className="text-blue-600" />
          <span className="text-sm font-medium text-gray-700">Composition</span>
        </div>
        
        <div className="space-y-2">
          {fund.composition.slice(0, 3).map((item, index) => (
            <div key={index} className="flex justify-between items-center text-sm">
              <span className="text-gray-600">{item.token}</span>
              <span className="font-medium text-gray-900">{item.weight}</span>
            </div>
          ))}
          
          {fund.composition.length > 3 && (
            <div className="text-xs text-gray-500 text-center pt-2 border-t border-gray-100">
              +{fund.composition.length - 3} autres tokens
            </div>
          )}
        </div>
      </div>

      {/* Actions */}
      <div className="p-6 pt-0">
        <div className="flex gap-2">
          <button
            onClick={() => onSelect(fund)}
            className="flex-1 flex items-center justify-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition-colors text-sm font-medium"
          >
            <FaEye className="text-xs" />
            Détails
          </button>
          
          <button className="px-4 py-2 bg-green-600 text-white rounded-xl hover:bg-green-700 transition-colors text-sm font-medium">
            Investir
          </button>
        </div>
        
        {/* Contract Address */}
        <div className="mt-4 pt-4 border-t border-gray-100">
          <div className="flex items-center justify-between text-xs">
            <span className="text-gray-500">Contrat:</span>
            <a
              href={`https://etherscan.io/address/${fund.fund_address}`}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-1 text-blue-600 hover:text-blue-700 transition-colors"
            >
              {fund.fund_address.slice(0, 8)}...{fund.fund_address.slice(-6)}
              <FaExternalLinkAlt className="text-xs" />
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FundCard;