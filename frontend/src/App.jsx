import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './components/Navigation';
import DAOAndTokenisation from './pages/DAOAndTokenisation';

// Pages de démonstration
const Home = () => (
  <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white flex items-center justify-center">
    <div className="text-center">
      <h1 className="text-6xl font-bold bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent mb-6">
        🚀 StartupDAO
      </h1>
      <p className="text-xl text-gray-300 mb-8">
        Plateforme de tokenisation et gouvernance décentralisée pour startups
      </p>
      <div className="space-x-4">
        <button className="bg-gradient-to-r from-purple-600 to-cyan-600 hover:from-purple-700 hover:to-cyan-700 text-white px-8 py-3 rounded-lg font-medium transition-all duration-200">
          Créer une Startup
        </button>
        <button className="bg-transparent border-2 border-purple-500 text-purple-400 hover:bg-purple-500 hover:text-white px-8 py-3 rounded-lg font-medium transition-all duration-200">
          Explorer les DAOs
        </button>
      </div>
    </div>
  </div>
);

const Startups = () => (
  <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white flex items-center justify-center">
    <div className="text-center">
      <h1 className="text-4xl font-bold text-white mb-4">🚀 Startups</h1>
      <p className="text-gray-300">Liste des startups tokenisées</p>
    </div>
  </div>
);

const Investors = () => (
  <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white flex items-center justify-center">
    <div className="text-center">
      <h1 className="text-4xl font-bold text-white mb-4">👥 Investisseurs</h1>
      <p className="text-gray-300">Portail des investisseurs</p>
    </div>
  </div>
);

const Analytics = () => (
  <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white flex items-center justify-center">
    <div className="text-center">
      <h1 className="text-4xl font-bold text-white mb-4">📊 Analytics</h1>
      <p className="text-gray-300">Tableaux de bord et analyses</p>
    </div>
  </div>
);

function App() {
  return (
    <Router>
      <div className="App">
        <Navigation />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/startups" element={<Startups />} />
          <Route path="/investors" element={<Investors />} />
          <Route path="/dao" element={<DAOAndTokenisation />} />
          <Route path="/analytics" element={<Analytics />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;