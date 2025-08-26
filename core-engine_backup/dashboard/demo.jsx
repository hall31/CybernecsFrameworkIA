import React, { useState } from 'react';
import InfrastructureDashboard from './InfrastructureDashboard';

const DemoInfrastructure = () => {
  const [demoData, setDemoData] = useState({
    infra: {
      cluster: "gke-startup123-1234567890",
      url: "https://startup123.app",
      scaling: "2-20 pods",
      ssl: "active",
      loadbalancer: "Nginx Ingress"
    },
    monitoring: {
      grafana_url: "https://monitoring.startup123.app",
      dashboards: ["performance", "errors", "uptime"],
      prometheus_url: "https://prometheus.startup123.app",
      metrics_count: 15
    },
    alerting: {
      alerts: ["CPU High", "API Errors", "Downtime", "Memory High", "Response Time"],
      channels: ["Slack", "Email"],
      rules_count: 5,
      thresholds: {
        cpu_warning: 70,
        cpu_critical: 80,
        memory_warning: 75,
        memory_critical: 85,
        error_rate_warning: 2,
        error_rate_critical: 5,
        response_time_warning: 1.5,
        response_time_critical: 2.0,
        uptime_critical: 99.9
      }
    }
  });

  const [showDashboard, setShowDashboard] = useState(true);

  const updateDemoData = () => {
    // Simulation de mise à jour des données
    const newData = {
      ...demoData,
      infra: {
        ...demoData.infra,
        cluster: `gke-startup123-${Math.floor(Math.random() * 10000)}`,
        url: `https://startup${Math.floor(Math.random() * 1000)}.app`
      },
      monitoring: {
        ...demoData.monitoring,
        metrics_count: Math.floor(Math.random() * 20) + 10
      }
    };
    setDemoData(newData);
  };

  const simulateAlert = () => {
    const newAlert = `Alert ${Math.floor(Math.random() * 1000)}`;
    setDemoData({
      ...demoData,
      alerting: {
        ...demoData.alerting,
        alerts: [...demoData.alerting.alerts, newAlert]
      }
    });
  };

  const simulateScaling = () => {
    const currentPods = Math.floor(Math.random() * 18) + 2; // 2-20
    setDemoData({
      ...demoData,
      infra: {
        ...demoData.infra,
        scaling: `${currentPods}-20 pods`
      }
    });
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* En-tête de démonstration */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">
                🚀 Epic 9 - Démonstration Infrastructure DevOps
              </h1>
              <p className="text-gray-600 mt-2">
                Dashboard d'infrastructure avec auto-scaling, monitoring et alerting
              </p>
            </div>
            <div className="flex space-x-3">
              <button
                onClick={updateDemoData}
                className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
              >
                🔄 Actualiser
              </button>
              <button
                onClick={simulateAlert}
                className="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 transition-colors"
              >
                🚨 Simuler Alerte
              </button>
              <button
                onClick={simulateScaling}
                className="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 transition-colors"
              >
                📈 Simuler Scaling
              </button>
              <button
                onClick={() => setShowDashboard(!showDashboard)}
                className="px-4 py-2 bg-gray-600 text-white rounded-md hover:bg-gray-700 transition-colors"
              >
                {showDashboard ? '👁️ Masquer' : '👁️ Afficher'} Dashboard
              </button>
            </div>
          </div>
        </div>

        {/* Informations de démonstration */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
          <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
            <h3 className="font-semibold text-blue-900 mb-2">🔧 Infrastructure</h3>
            <p className="text-blue-700 text-sm">
              Cluster: {demoData.infra.cluster}<br/>
              URL: {demoData.infra.url}<br/>
              Scaling: {demoData.infra.scaling}
            </p>
          </div>
          
          <div className="bg-orange-50 border border-orange-200 rounded-lg p-4">
            <h3 className="font-semibold text-orange-900 mb-2">📊 Monitoring</h3>
            <p className="text-orange-700 text-sm">
              Grafana: {demoData.monitoring.grafana_url}<br/>
              Dashboards: {demoData.monitoring.dashboards.join(', ')}<br/>
              Métriques: {demoData.monitoring.metrics_count}
            </p>
          </div>
          
          <div className="bg-red-50 border border-red-200 rounded-lg p-4">
            <h3 className="font-semibold text-red-900 mb-2">🚨 Alertes</h3>
            <p className="text-red-700 text-sm">
              Règles: {demoData.alerting.alerts.length}<br/>
              Canaux: {demoData.alerting.channels.join(', ')}<br/>
              Seuils: {Object.keys(demoData.alerting.thresholds).length}
            </p>
          </div>
        </div>

        {/* Dashboard d'infrastructure */}
        {showDashboard && (
          <InfrastructureDashboard projectData={demoData} />
        )}

        {/* Instructions d'utilisation */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mt-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">
            📖 Instructions d'utilisation
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h3 className="font-medium text-gray-900 mb-2">🎯 Fonctionnalités</h3>
              <ul className="text-sm text-gray-600 space-y-1">
                <li>• Auto-scaling Kubernetes (2-20 pods)</li>
                <li>• Monitoring Prometheus + Grafana</li>
                <li>• Alertes vers Slack/Email</li>
                <li>• LoadBalancer Nginx Ingress</li>
                <li>• Certificats SSL automatiques</li>
              </ul>
            </div>
            
            <div>
              <h3 className="font-medium text-gray-900 mb-2">🔧 Actions disponibles</h3>
              <ul className="text-sm text-gray-600 space-y-1">
                <li>• 🔄 Actualiser les données</li>
                <li>• 🚨 Simuler une nouvelle alerte</li>
                <li>• 📈 Simuler le scaling des pods</li>
                <li>• 👁️ Masquer/Afficher le dashboard</li>
              </ul>
            </div>
          </div>
          
          <div className="mt-6 p-4 bg-gray-50 rounded-lg">
            <h3 className="font-medium text-gray-900 mb-2">💡 Utilisation en production</h3>
            <p className="text-sm text-gray-600">
              Ce dashboard peut être intégré dans votre application React en important le composant 
              <code className="bg-gray-200 px-1 rounded">InfrastructureDashboard</code> et en lui passant 
              les données d'infrastructure via la prop <code className="bg-gray-200 px-1 rounded">projectData</code>.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DemoInfrastructure;