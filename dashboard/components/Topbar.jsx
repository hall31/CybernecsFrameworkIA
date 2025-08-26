import React from 'react';
import { BellIcon, CogIcon } from '@heroicons/react/24/outline';

const Topbar = () => {
  return (
    <div className="bg-white shadow-md h-16 flex items-center justify-between px-6 fixed top-0 left-64 right-0 z-10">
      <div className="flex items-center">
        <h2 className="text-xl font-semibold text-gray-900">Dashboard</h2>
      </div>
      
      <div className="flex items-center space-x-4">
        <button className="p-2 text-gray-400 hover:text-gray-600 transition-colors duration-200">
          <BellIcon className="w-5 h-5" />
        </button>
        
        <button className="p-2 text-gray-400 hover:text-gray-600 transition-colors duration-200">
          <CogIcon className="w-5 h-5" />
        </button>
        
        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 bg-accent rounded-full flex items-center justify-center">
            <span className="text-white text-sm font-medium">A</span>
          </div>
          <div className="hidden md:block">
            <p className="text-sm font-medium text-gray-900">Admin User</p>
            <p className="text-xs text-gray-500">admin@shipfast.com</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Topbar;