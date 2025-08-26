import React from "react";
import { FaHome, FaTasks, FaCogs, FaChartPie } from "react-icons/fa";

const Sidebar = ({ onPageChange }) => {
  const handlePageChange = (page) => {
    onPageChange(page);
  };

  return (
    <div className="w-64 bg-white shadow-xl p-6 flex flex-col">
      <h1 className="text-xl font-bold text-blue-600 mb-8">⚡ Startup Factory</h1>
      <nav className="flex flex-col gap-4">
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