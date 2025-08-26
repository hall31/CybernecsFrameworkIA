import React from 'react';
import { 
  HomeIcon, 
  DocumentTextIcon, 
  MapIcon, 
  BuildingOfficeIcon 
} from '@heroicons/react/24/outline';
import Link from 'next/link';
import { useRouter } from 'next/router';

const navigation = [
  { name: 'Home', href: '/', icon: HomeIcon },
  { name: 'Logs', href: '/logs', icon: DocumentTextIcon },
  { name: 'Roadmap', href: '/roadmap', icon: MapIcon },
  { name: 'Startups', href: '/startups', icon: BuildingOfficeIcon },
];

const Sidebar = () => {
  const router = useRouter();

  return (
    <div className="bg-white shadow-xl h-screen p-6 w-64 fixed left-0 top-0">
      <div className="flex items-center mb-8">
        <div className="w-8 h-8 bg-accent rounded-lg flex items-center justify-center">
          <span className="text-white font-bold text-lg">S</span>
        </div>
        <h1 className="ml-3 text-xl font-bold text-gray-900">ShipFast</h1>
      </div>
      
      <nav className="space-y-2">
        {navigation.map((item) => {
          const isActive = router.pathname === item.href;
          return (
            <Link
              key={item.name}
              href={item.href}
              className={`flex items-center px-4 py-3 text-sm font-medium rounded-lg transition-all duration-200 ${
                isActive
                  ? 'bg-accent text-white shadow-md'
                  : 'text-gray-600 hover:text-accent hover:bg-gray-50'
              }`}
            >
              <item.icon className="w-5 h-5 mr-3" />
              {item.name}
            </Link>
          );
        })}
      </nav>
      
      <div className="absolute bottom-6 left-6 right-6">
        <div className="bg-gray-50 rounded-lg p-4">
          <div className="flex items-center">
            <div className="w-8 h-8 bg-gray-300 rounded-full"></div>
            <div className="ml-3">
              <p className="text-sm font-medium text-gray-900">Admin User</p>
              <p className="text-xs text-gray-500">admin@shipfast.com</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;