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
=======
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import styled from 'styled-components';
import InvestorDashboard from './components/InvestorDashboard/InvestorDashboard';

// Composants stylisés
const AppContainer = styled.div`
  min-height: 100vh;
  background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%);
  color: white;
`;

const Navigation = styled.nav`
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
`;

const NavContainer = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const Logo = styled.div`
  font-size: 1.5rem;
  font-weight: bold;
  background: linear-gradient(45deg, #00d4ff, #ff6b6b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
`;

const NavLinks = styled.div`
  display: flex;
  gap: 30px;
`;

const NavLink = styled(Link)`
  color: #b8c5d6;
  text-decoration: none;
  padding: 10px 20px;
  border-radius: 25px;
  transition: all 0.3s ease;
  
  &:hover {
    color: #ffffff;
    background: rgba(255, 255, 255, 0.1);
  }
  
  &.active {
    color: #00d4ff;
    background: rgba(0, 212, 255, 0.1);
    border: 1px solid rgba(0, 212, 255, 0.3);
  }
`;

const HomePage = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  padding: 60px 20px;
  text-align: center;
`;

const HomeTitle = styled.h1`
  font-size: 4rem;
  font-weight: bold;
  margin: 0 0 30px 0;
  background: linear-gradient(45deg, #00d4ff, #ff6b6b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
`;

const HomeSubtitle = styled.p`
  font-size: 1.5rem;
  color: #b8c5d6;
  margin: 0 0 50px 0;
  line-height: 1.6;
`;

const FeatureGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin-top: 60px;
`;

const FeatureCard = styled.div`
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 40px 30px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  text-align: center;
  transition: transform 0.3s ease;
  
  &:hover {
    transform: translateY(-10px);
  }
`;

const FeatureIcon = styled.div`
  font-size: 3rem;
  margin-bottom: 20px;
`;

const FeatureTitle = styled.h3`
  font-size: 1.5rem;
  margin: 0 0 15px 0;
  color: #ffffff;
`;

const FeatureDescription = styled.p`
  color: #b8c5d6;
  line-height: 1.6;
  margin: 0;
`;

const CTAButton = styled(Link)`
  display: inline-block;
  background: linear-gradient(45deg, #00d4ff, #ff6b6b);
  color: white;
  text-decoration: none;
  padding: 15px 40px;
  border-radius: 50px;
  font-size: 1.2rem;
  font-weight: bold;
  margin-top: 40px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  
  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0, 212, 255, 0.3);
  }
`;

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
      <AppContainer>
        <Navigation>
          <NavContainer>
            <Logo>🚀 StartupAI</Logo>
            <NavLinks>
              <NavLink to="/">Accueil</NavLink>
              <NavLink to="/investor">Investisseur IA</NavLink>
            </NavLinks>
          </NavContainer>
        </Navigation>

        <Routes>
          <Route path="/" element={
            <HomePage>
              <HomeTitle>Investisseur IA</HomeTitle>
              <HomeSubtitle>
                Évaluez et prenez des décisions d'investissement intelligentes 
                grâce à l'intelligence artificielle
              </HomeSubtitle>
              
              <CTAButton to="/investor">
                Accéder au Dashboard
              </CTAButton>
              
              <FeatureGrid>
                <FeatureCard>
                  <FeatureIcon>📊</FeatureIcon>
                  <FeatureTitle>Valorisation Automatique</FeatureTitle>
                  <FeatureDescription>
                    Calcul intelligent de la valorisation basé sur les métriques 
                    financières et de croissance
                  </FeatureDescription>
                </FeatureCard>
                
                <FeatureCard>
                  <FeatureIcon>📈</FeatureIcon>
                  <FeatureTitle>Analyse des KPIs</FeatureTitle>
                  <FeatureDescription>
                    Suivi en temps réel des métriques clés : MRR, CAC, LTV, Churn
                  </FeatureDescription>
                </FeatureCard>
                
                <FeatureCard>
                  <FeatureIcon>🚀</FeatureIcon>
                  <FeatureTitle>Décision d'Investissement</FeatureTitle>
                  <FeatureDescription>
                    Recommandations d'investissement basées sur l'analyse 
                    complète des données
                  </FeatureDescription>
                </FeatureCard>
                
                <FeatureCard>
                  <FeatureIcon>💰</FeatureIcon>
                  <FeatureTitle>Plan de Financement</FeatureTitle>
                  <FeatureDescription>
                    Proposition détaillée d'allocation des ressources 
                    et du budget d'investissement
                  </FeatureDescription>
                </FeatureCard>
              </FeatureGrid>
            </HomePage>
          } />
          
          <Route path="/investor" element={<InvestorDashboard />} />
        </Routes>
      </AppContainer>
    </Router>
  );
}

export default App;