import React from "react";

const Topbar = () => {
  return (
    <div className="bg-white shadow-md h-16 flex items-center justify-between px-6">
      <h2 className="font-semibold text-lg">Admin Dashboard</h2>
      <div className="flex items-center gap-3">
        <span className="text-gray-500">admin@factory.ai</span>
        <img
          src="https://i.pravatar.cc/40"
          alt="avatar"
          className="w-10 h-10 rounded-full border"
        />
      </div>
    </div>
  );
};

export default Topbar;