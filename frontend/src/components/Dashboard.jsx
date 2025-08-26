import React, { useState } from 'react';
import FinanceTab from './FinanceTab';
import LegalTab from './LegalTab';
import GrowthTab from './GrowthTab';
import RoadmapTab from './RoadmapTab';
import StackTab from './StackTab';
import BackendTab from './BackendTab';
import FrontendTab from './FrontendTab';
import MarketingTab from './MarketingTab';

const Dashboard = ({ startupData }) => {
  const [activeTab, setActiveTab] = useState('roadmap');

  const tabs = [
    { id: 'roadmap', name: 'Roadmap', icon: '🗺️' },
    { id: 'stack', name: 'Stack', icon: '⚙️' },
    { id: 'backend', name: 'Backend', icon: '🔧' },
    { id: 'frontend', name: 'Frontend', icon: '🎨' },
    { id: 'marketing', name: 'Marketing', icon: '📢' },
    { id: 'finance', name: 'Finance', icon: '💰' },
    { id: 'legal', name: 'Legal', icon: '⚖️' },
    { id: 'growth', name: 'Growth', icon: '📈' }
  ];

  const renderTabContent = () => {
    switch (activeTab) {
      case 'roadmap':
        return <RoadmapTab data={startupData?.roadmap} />;
      case 'stack':
        return <StackTab data={startupData?.stack} />;
      case 'backend':
        return <BackendTab data={startupData?.backend} />;
      case 'frontend':
        return <FrontendTab data={startupData?.frontend} />;
      case 'marketing':
        return <MarketingTab data={startupData?.marketing} />;
      case 'finance':
        return <FinanceTab data={startupData?.finance} />;
      case 'legal':
        return <LegalTab data={startupData?.legal} />;
      case 'growth':
        return <GrowthTab data={startupData?.growth} />;
      default:
        return <RoadmapTab data={startupData?.roadmap} />;
    }
  };

  if (!startupData) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-50">
        <div className="text-center">
          <div className="text-6xl mb-4">🚀</div>
          <h2 className="text-2xl font-bold text-gray-700 mb-2">
            Startup Generator
          </h2>
          <p className="text-gray-500">
            Générez votre startup en quelques clics
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center">
              <div className="text-2xl mr-3">🚀</div>
              <h1 className="text-xl font-semibold text-gray-900">
                {startupData.idea}
              </h1>
            </div>
            <div className="text-sm text-gray-500">
              Généré le {startupData.generated_at}
            </div>
          </div>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="bg-white border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <nav className="flex space-x-8 overflow-x-auto">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm transition-colors ${
                  activeTab === tab.id
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                <span className="mr-2">{tab.icon}</span>
                {tab.name}
              </button>
            ))}
          </nav>
        </div>
      </div>

      {/* Tab Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {renderTabContent()}
      </div>
    </div>
  );
};

export default Dashboard;