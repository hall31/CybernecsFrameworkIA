import React from "react";
import { FaHome, FaTasks, FaCogs } from "react-icons/fa";

const Sidebar = () => {
  return (
    <div className="w-64 bg-white shadow-xl p-6 flex flex-col">
      <h1 className="text-xl font-bold text-blue-600 mb-8">⚡ Startup Factory</h1>
      <nav className="flex flex-col gap-4">
        <a href="#" className="flex items-center gap-2 hover:text-blue-600">
          <FaHome /> Home
        </a>
        <a href="#" className="flex items-center gap-2 hover:text-blue-600">
          <FaTasks /> Roadmap
        </a>
        <a href="#" className="flex items-center gap-2 hover:text-blue-600">
          <FaCogs /> Logs
        </a>
      </nav>
    </div>
  );
};

export default Sidebar;