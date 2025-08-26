import React from "react";
import { FaHome, FaTasks, FaCogs, FaNetworkWired } from "react-icons/fa";

const Sidebar = ({ currentPage, setCurrentPage }) => {
  const navItems = [
    { id: 'home', label: 'Home', icon: <FaHome /> },
    { id: 'roadmap', label: 'Roadmap', icon: <FaTasks /> },
    { id: 'orchestration', label: 'Orchestration', icon: <FaNetworkWired /> },
    { id: 'logs', label: 'Logs', icon: <FaCogs /> }
  ];
import { FaHome, FaTasks, FaCogs, FaChartPie } from "react-icons/fa";

const Sidebar = ({ onPageChange }) => {
  const handlePageChange = (page) => {
    onPageChange(page);
  };
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
        <button
          onClick={() => handlePageChange("home")}
          className="flex items-center gap-2 hover:text-blue-600 text-left w-full p-2 rounded-lg hover:bg-blue-50 transition-colors"
        >
          <FaHome /> Home
        </button>
        <button
          onClick={() => handlePageChange("roadmap")}
          className="flex items-center gap-2 hover:text-blue-600 text-left w-full p-2 rounded-lg hover:bg-blue-50 transition-colors"
        >
          <FaTasks /> Roadmap
        </button>
        <button
          onClick={() => handlePageChange("funds")}
          className="flex items-center gap-2 hover:text-blue-600 text-left w-full p-2 rounded-lg hover:bg-blue-50 transition-colors"
        >
          <FaChartPie /> Fonds IA
        </button>
        <button
          onClick={() => handlePageChange("logs")}
          className="flex items-center gap-2 hover:text-blue-600 text-left w-full p-2 rounded-lg hover:bg-blue-50 transition-colors"
        >
          <FaCogs /> Logs
        </button>
      </nav>
    </div>
  );
};

export default Sidebar;