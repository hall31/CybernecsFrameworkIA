import React from "react";
import { FaHome, FaTasks, FaCogs, FaCrown } from "react-icons/fa";

const Sidebar = ({ currentView, setCurrentView }) => {
  return (
    <div className="w-64 bg-white shadow-xl p-6 flex flex-col">
      <h1 className="text-xl font-bold text-blue-600 mb-8">⚡ Startup Factory</h1>
      <nav className="flex flex-col gap-4">
        <button
          onClick={() => setCurrentView("home")}
          className={`flex items-center gap-2 hover:text-blue-600 transition ${
            currentView === "home" ? "text-blue-600 font-semibold" : "text-gray-600"
          }`}
        >
          <FaHome /> Home
        </button>
        <button
          onClick={() => setCurrentView("roadmap")}
          className={`flex items-center gap-2 hover:text-blue-600 transition ${
            currentView === "roadmap" ? "text-blue-600 font-semibold" : "text-gray-600"
          }`}
        >
          <FaTasks /> Roadmap
        </button>
        <button
          onClick={() => setCurrentView("sovereign")}
          className={`flex items-center gap-2 hover:text-blue-600 transition ${
            currentView === "sovereign" ? "text-blue-600 font-semibold" : "text-gray-600"
          }`}
        >
          <FaCrown /> Fonds Souverain
        </button>
        <button
          onClick={() => setCurrentView("logs")}
          className={`flex items-center gap-2 hover:text-blue-600 transition ${
            currentView === "logs" ? "text-blue-600 font-semibold" : "text-gray-600"
          }`}
        >
          <FaCogs /> Logs
        </button>
      </nav>
    </div>
  );
};

export default Sidebar;