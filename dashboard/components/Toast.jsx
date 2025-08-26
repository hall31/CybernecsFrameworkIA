import React, { useEffect, useState } from 'react';
import { CheckCircleIcon, XCircleIcon, XMarkIcon } from '@heroicons/react/24/outline';

const Toast = ({ message, type = 'success', duration = 5000, onClose }) => {
  const [isVisible, setIsVisible] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsVisible(false);
      setTimeout(() => onClose(), 300);
    }, duration);

    return () => clearTimeout(timer);
  }, [duration, onClose]);

  const handleClose = () => {
    setIsVisible(false);
    setTimeout(() => onClose(), 300);
  };

  const icons = {
    success: CheckCircleIcon,
    error: XCircleIcon,
  };

  const colors = {
    success: 'bg-green-50 border-green-200 text-green-800',
    error: 'bg-red-50 border-red-200 text-red-800',
  };

  const Icon = icons[type];

  if (!isVisible) return null;

  return (
    <div className={`fixed top-20 right-6 z-50 animate-slide-up`}>
      <div className={`flex items-center p-4 border rounded-lg shadow-lg ${colors[type]}`}>
        <Icon className="w-5 h-5 mr-3 flex-shrink-0" />
        <span className="text-sm font-medium">{message}</span>
        <button
          onClick={handleClose}
          className="ml-4 text-gray-400 hover:text-gray-600 transition-colors duration-200"
        >
          <XMarkIcon className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};

export default Toast;