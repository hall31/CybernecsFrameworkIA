import React from "react";
import { FaHome, FaTasks, FaCogs, FaNetworkWired } from "react-icons/fa";

const Sidebar = ({ currentPage, setCurrentPage }) => {
  const navItems = [
    { id: 'home', label: 'Home', icon: <FaHome /> },
    { id: 'roadmap', label: 'Roadmap', icon: <FaTasks /> },
    { id: 'orchestration', label: 'Orchestration', icon: <FaNetworkWired /> },
    { id: 'logs', label: 'Logs', icon: <FaCogs /> }
  ];

  return (
    <div className="w-64 bg-white shadow-xl p-6 flex flex-col">
      <h1 className="text-xl font-bold text-blue-600 mb-8">⚡ Startup Factory</h1>
      <nav className="flex flex-col gap-4">
        {navItems.map((item) => (
          <button
            key={item.id}
            onClick={() => setCurrentPage(item.id)}
            className={`flex items-center gap-2 p-2 rounded-lg transition-colors ${
              currentPage === item.id 
                ? 'bg-blue-100 text-blue-600' 
                : 'hover:text-blue-600 hover:bg-gray-50'
            }`}
          >
            {item.icon} {item.label}
          </button>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;