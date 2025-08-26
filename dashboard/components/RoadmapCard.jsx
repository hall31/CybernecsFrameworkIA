import React from 'react';
import { CheckCircleIcon, ClockIcon, ExclamationTriangleIcon } from '@heroicons/react/24/outline';

const RoadmapCard = ({ epic }) => {
  const getStatusIcon = (status) => {
    switch (status?.toLowerCase()) {
      case 'completed':
        return <CheckCircleIcon className="w-5 h-5 text-green-500" />;
      case 'in_progress':
        return <ClockIcon className="w-5 h-5 text-blue-500" />;
      case 'pending':
        return <ExclamationTriangleIcon className="w-5 h-5 text-yellow-500" />;
      default:
        return <ClockIcon className="w-5 h-5 text-gray-400" />;
    }
  };

  const getStatusColor = (status) => {
    switch (status?.toLowerCase()) {
      case 'completed':
        return 'bg-green-100 text-green-800';
      case 'in_progress':
        return 'bg-blue-100 text-blue-800';
      case 'pending':
        return 'bg-yellow-100 text-yellow-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="card hover:shadow-xl transition-all duration-200">
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <h3 className="text-lg font-semibold text-accent mb-2">
            {epic.title || 'Epic Title'}
          </h3>
          <p className="text-gray-600 text-sm mb-3">
            {epic.description || 'Epic description goes here...'}
          </p>
        </div>
        <div className="flex items-center space-x-2">
          {getStatusIcon(epic.status)}
          <span className={`px-2 py-1 rounded-full text-xs font-medium ${getStatusColor(epic.status)}`}>
            {epic.status || 'pending'}
          </span>
        </div>
      </div>

      {epic.user_stories && epic.user_stories.length > 0 && (
        <div className="space-y-3">
          <h4 className="text-sm font-medium text-gray-700">User Stories:</h4>
          <div className="space-y-2">
            {epic.user_stories.map((story, index) => (
              <div key={index} className="flex items-start space-x-3 p-3 bg-gray-50 rounded-lg">
                <div className="w-2 h-2 bg-accent rounded-full mt-2 flex-shrink-0"></div>
                <div className="flex-1">
                  <p className="text-sm text-gray-800 font-medium">
                    {story.title || `User Story ${index + 1}`}
                  </p>
                  {story.description && (
                    <p className="text-xs text-gray-600 mt-1">
                      {story.description}
                    </p>
                  )}
                  {story.acceptance_criteria && (
                    <div className="mt-2">
                      <p className="text-xs font-medium text-gray-700 mb-1">Acceptance Criteria:</p>
                      <ul className="text-xs text-gray-600 space-y-1">
                        {story.acceptance_criteria.map((criteria, idx) => (
                          <li key={idx} className="flex items-center space-x-2">
                            <span className="w-1 h-1 bg-gray-400 rounded-full"></span>
                            <span>{criteria}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {epic.estimated_hours && (
        <div className="mt-4 pt-4 border-t border-gray-200">
          <div className="flex items-center justify-between text-sm">
            <span className="text-gray-600">Estimated Hours:</span>
            <span className="font-medium text-gray-900">{epic.estimated_hours}h</span>
          </div>
        </div>
      )}
    </div>
  );
};

export default RoadmapCard;