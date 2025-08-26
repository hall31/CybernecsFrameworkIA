import React, { useState, useEffect } from 'react';
import {
  PieChart, Pie, Cell, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts';
import './Portfolio.css';

const Portfolio = () => {
  const [portfolioData, setPortfolioData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchPortfolioData();
  }, []);

  const fetchPortfolioData = async () => {
    try {
      setLoading(true);
      const response = await fetch('http://localhost:5000/portfolio');
      const result = await response.json();
      
      if (result.success) {
        setPortfolioData(result.data);
      } else {
        setError(result.error || 'Erreur lors de la récupération des données');
      }
    } catch (err) {
      setError('Erreur de connexion au serveur');
      console.error('Erreur:', err);
    } finally {
      setLoading(false);
    }
  };

  const refreshData = () => {
    fetchPortfolioData();
  };

  if (loading) {
    return (
      <div className="portfolio-loading">
        <div className="loading-spinner"></div>
        <p>Analyse du portefeuille en cours...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="portfolio-error">
        <h2>Erreur</h2>
        <p>{error}</p>
        <button onClick={refreshData} className="refresh-btn">
          Réessayer
        </button>
      </div>
    );
  }

  if (!portfolioData) {
    return <div>Aucune donnée disponible</div>;
  }

  // Préparation des données pour les graphiques
  const statusData = [
    { name: 'Investir', value: portfolioData.startups_summary.invest, color: '#10B981' },
    { name: 'Hold', value: portfolioData.startups_summary.hold, color: '#F59E0B' },
    { name: 'Drop', value: portfolioData.startups_summary.drop, color: '#EF4444' }
  ];

    value: parseFloat(percentage),
    color: '#3B82F6'
  }));

  return (
    <div className="portfolio-container">
      {/* Header */}
      <div className="portfolio-header">
        <h1>Portfolio Dashboard</h1>
        <button onClick={refreshData} className="refresh-btn">
          🔄 Actualiser
        </button>
      </div>

      {/* Section Résumé */}
      <div className="portfolio-summary">
        <div className="summary-card total-startups">
          <h3>Total Startups</h3>
          <div className="metric-value">{portfolioData.total_startups}</div>
        </div>
        
        <div className="summary-card portfolio-value">
          <h3>Valeur Portefeuille</h3>
          <div className="metric-value">{portfolioData.portfolio_value}</div>
        </div>
        
        <div className="summary-card best-startup">
          <h3>Best Startup</h3>
          <div className="startup-info">
            <div className="startup-name">{portfolioData.best_startup.name}</div>
            <div className="startup-valuation">{portfolioData.best_startup.valuation}</div>
            <div className="startup-score">Score: {portfolioData.best_startup.score}</div>
          </div>
        </div>
      </div>

      {/* Section Graphiques */}
      <div className="portfolio-charts">
        <div className="chart-container">
          <h3>Répartition par Status</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={statusData}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                outerRadius={80}
                fill="#8884d8"
                dataKey="value"
              >
                {statusData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.color} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-container">
          <h3>Allocation Cloud Credits</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={resourceData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="value" fill="#3B82F6" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Section Startups */}
      <div className="portfolio-startups">
        <h3>Détail des Startups</h3>
        <div className="startups-table-container">
          <table className="startups-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nom</th>
                <th>Idea</th>
                <th>Valuation</th>
                <th>Status</th>
                <th>MRR</th>
                <th>Churn</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
              {portfolioData.startups && portfolioData.startups.map((startup) => (
                <tr key={startup.id} className={`startup-row status-${startup.status.toLowerCase()}`}>
                  <td>{startup.id}</td>
                  <td>{startup.name}</td>
                  <td className="startup-idea">{startup.idea}</td>
                  <td className="startup-valuation">{startup.valuation}</td>
                  <td>
                    <span className={`status-badge status-${startup.status.toLowerCase()}`}>
                      {startup.status}
                    </span>
                  </td>
                  <td>{startup.mrr?.toLocaleString()} €</td>
                  <td>{(startup.churn * 100).toFixed(1)}%</td>
                  <td className="startup-score">{startup.evaluation_score || 'N/A'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Section Recommandations */}
      <div className="portfolio-recommendations">
        <h3>Recommandations</h3>
        <div className="recommendations-list">
          {portfolioData.recommendations?.map((rec, index) => (
            <div key={index} className="recommendation-item">
              💡 {rec}
            </div>
          ))}
        </div>
      </div>

      {/* Section Underperformers */}
      {portfolioData.underperformers && portfolioData.underperformers.length > 0 && (
        <div className="portfolio-underperformers">
          <h3>Startups Sous-Performantes</h3>
          <div className="underperformers-list">
            {portfolioData.underperformers.map((startup) => (
              <div key={startup.id} className="underperformer-item">
                <div className="startup-id">{startup.id}</div>
                <div className="startup-idea">{startup.idea}</div>
                <div className="startup-churn">Churn: {(startup.churn * 100).toFixed(1)}%</div>
                <div className="startup-score">Score: {startup.score}</div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default Portfolio;