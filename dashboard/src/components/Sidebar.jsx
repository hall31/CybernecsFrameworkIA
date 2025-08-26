import React from "react";
import { FaHome, FaTasks, FaCogs, FaChartLine, FaCoins } from "react-icons/fa";

const Sidebar = ({ activePage, setActivePage }) => {
  return (
    <div className="w-64 bg-white shadow-xl p-6 flex flex-col">
      <h1 className="text-xl font-bold text-blue-600 mb-8">⚡ Startup Factory</h1>
      <nav className="flex flex-col gap-4">
        <button 
          onClick={() => setActivePage('home')}
          className={`flex items-center gap-2 hover:text-blue-600 transition ${
            activePage === 'home' ? 'text-blue-600 font-medium' : 'text-gray-600'
          }`}
        >
          <FaHome /> Home
        </button>
        <button 
          onClick={() => setActivePage('roadmap')}
          className={`flex items-center gap-2 hover:text-blue-600 transition ${
            activePage === 'roadmap' ? 'text-blue-600 font-medium' : 'text-gray-600'
          }`}
        >
          <FaTasks /> Roadmap
        </button>
        <button 
          onClick={() => setActivePage('market')}
          className={`flex items-center gap-2 hover:text-blue-600 transition ${
            activePage === 'market' ? 'text-blue-600 font-medium' : 'text-gray-600'
          }`}
        >
          <FaChartLine /> Global Market
        </button>
        <button 
          onClick={() => setActivePage('logs')}
          className={`flex items-center gap-2 hover:text-blue-600 transition ${
            activePage === 'logs' ? 'text-blue-600 font-medium' : 'text-gray-600'
          }`}
        >
          <FaCogs /> Logs
        </button>
      </nav>
    </div>
  );
};

export default Sidebar;