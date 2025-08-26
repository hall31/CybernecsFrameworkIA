import React from "react";
import { FaHome, FaTasks, FaCogs, FaChartLine } from "react-icons/fa";

const Sidebar = ({ onViewChange, currentView }) => {
  const handleViewChange = (view) => {
    onViewChange(view);
  };

  return (
    <div className="w-64 bg-white shadow-xl p-6 flex flex-col">
      <h1 className="text-xl font-bold text-blue-600 mb-8">⚡ Startup Factory</h1>
      <nav className="flex flex-col gap-4">
        <button
          onClick={() => handleViewChange("home")}
          className={`flex items-center gap-2 hover:text-blue-600 text-left w-full p-2 rounded-lg transition ${
            currentView === "home" ? "bg-blue-50 text-blue-600" : ""
          }`}
        >
          <FaHome /> Home
        </button>
        <button
          onClick={() => handleViewChange("hedgefund")}
          className={`flex items-center gap-2 hover:text-blue-600 text-left w-full p-2 rounded-lg transition ${
            currentView === "hedgefund" ? "bg-blue-50 text-blue-600" : ""
          }`}
        >
          <FaChartLine /> Hedge Fund
        </button>
        <button
          onClick={() => handleViewChange("logs")}
          className={`flex items-center gap-2 hover:text-blue-600 text-left w-full p-2 rounded-lg transition ${
            currentView === "logs" ? "bg-blue-50 text-blue-600" : ""
          }`}
        >
          <FaCogs /> Logs
        </button>
      </nav>
    </div>
  );
};

export default Sidebar;