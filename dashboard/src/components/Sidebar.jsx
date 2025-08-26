import React from "react";
import { FaHome, FaTasks, FaCogs, FaBalanceScale } from "react-icons/fa";

const Sidebar = ({ onPageChange, currentPage }) => {
  const menuItems = [
    { id: "home", name: "Home", icon: <FaHome /> },
    { id: "roadmap", name: "Roadmap", icon: <FaTasks /> },
    { id: "constitution", name: "Constitution", icon: <FaBalanceScale /> },
    { id: "logs", name: "Logs", icon: <FaCogs /> }
  ];

  return (
    <div className="w-64 bg-white shadow-xl p-6 flex flex-col">
      <h1 className="text-xl font-bold text-blue-600 mb-8">⚡ Startup Factory</h1>
      <nav className="flex flex-col gap-4">
        {menuItems.map((item) => (
          <button
            key={item.id}
            onClick={() => onPageChange(item.id)}
            className={`flex items-center gap-2 p-2 rounded-lg transition-colors ${
              currentPage === item.id
                ? "bg-blue-100 text-blue-600"
                : "hover:text-blue-600 hover:bg-gray-50"
            }`}
          >
            {item.icon} {item.name}
          </button>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;