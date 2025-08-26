import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000';

// Composants stylisés
const DashboardContainer = styled.div`
  min-height: 100vh;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
  color: white;
  padding: 20px;
`;

const Header = styled.div`
  text-align: center;
  margin-bottom: 40px;
`;

const Title = styled.h1`
  font-size: 3rem;
  font-weight: bold;
  margin: 0;
  background: linear-gradient(45deg, #00d4ff, #ff6b6b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
`;

const Subtitle = styled.p`
  font-size: 1.2rem;
  color: #b8c5d6;
  margin: 10px 0;
`;

const GridContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 30px;
  max-width: 1400px;
  margin: 0 auto;
`;

const Card = styled.div`
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 30px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
  }
`;

const ValuationCard = styled(Card)`
  background: linear-gradient(135deg, rgba(0, 212, 255, 0.2), rgba(255, 107, 107, 0.2));
  border: 2px solid rgba(0, 212, 255, 0.3);
`;

const KPICard = styled(Card)`
  background: linear-gradient(135deg, rgba(255, 107, 107, 0.2), rgba(255, 193, 7, 0.2));
  border: 2px solid rgba(255, 107, 107, 0.3);
`;

const DecisionCard = styled(Card)`
  background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(33, 150, 243, 0.2));
  border: 2px solid rgba(76, 175, 80, 0.3);
`;

const CardTitle = styled.h2`
  font-size: 1.8rem;
  margin: 0 0 20px 0;
  color: #ffffff;
  display: flex;
  align-items: center;
  gap: 10px;
`;

const ValuationAmount = styled.div`
  font-size: 4rem;
  font-weight: bold;
  text-align: center;
  margin: 20px 0;
  background: linear-gradient(45deg, #00d4ff, #ff6b6b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
`;

const KPITable = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
`;

const KPIRow = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.2);
`;

const KPILabel = styled.span`
  font-weight: 500;
  color: #b8c5d6;
`;

const KPIValue = styled.span`
  font-weight: bold;
  font-size: 1.1rem;
  color: #ffffff;
`;

const DecisionBadge = styled.div`
  display: inline-block;
  padding: 15px 30px;
  border-radius: 50px;
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
  margin: 20px 0;
  background: ${props => props.decision === 'Investir' ? 
    'linear-gradient(45deg, #4caf50, #45a049)' : 
    props.decision === 'Investir avec conditions' ?
    'linear-gradient(45deg, #ff9800, #f57c00)' :
    'linear-gradient(45deg, #f44336, #d32f2f)'};
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
`;

const FundingPlan = styled.div`
  background: rgba(255, 255, 255, 0.1);
  padding: 20px;
  border-radius: 15px;
  margin-top: 20px;
  border: 1px solid rgba(255, 255, 255, 0.2);
`;

const FundingTitle = styled.h3`
  color: #00d4ff;
  margin: 0 0 15px 0;
  font-size: 1.3rem;
`;

const FundingDetails = styled.p`
  color: #ffffff;
  font-size: 1.1rem;
  line-height: 1.6;
  margin: 0;
`;

const ConfidenceScore = styled.div`
  text-align: center;
  margin-top: 20px;
`;

const ConfidenceLabel = styled.div`
  color: #b8c5d6;
  margin-bottom: 10px;
`;

const ConfidenceBar = styled.div`
  width: 100%;
  height: 8px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  overflow: hidden;
`;

const ConfidenceFill = styled.div`
  height: 100%;
  background: linear-gradient(45deg, #4caf50, #00d4ff);
  width: ${props => props.confidence * 100}%;
  transition: width 0.5s ease;
`;

const LoadingSpinner = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  font-size: 1.2rem;
  color: #b8c5d6;
`;

const InvestorDashboard = () => {
  const [startupData, setStartupData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Données de simulation pour le graphique de valorisation
  const valuationData = [
    { month: 'Jan', value: 1.2 },
    { month: 'Fév', value: 1.4 },
    { month: 'Mar', value: 1.6 },
    { month: 'Avr', value: 1.8 },
    { month: 'Mai', value: 2.0 },
    { month: 'Juin', value: 2.2 },
    { month: 'Juil', value: 2.4 },
    { month: 'Août', value: 2.5 }
  ];

  useEffect(() => {
    const fetchStartupData = async () => {
      try {
        setLoading(true);
        setError(null);

        const response = await axios.post(`${API_BASE}/create-startup`, {
          idea: 'SaaS marketplace'
        });

        const investor = response.data?.agents?.investor || {};

        const normalized = {
          project_id: response.data.project_id,
          idea: response.data.idea,
          valuation: investor.valuation || 'N/A',
          kpis: investor.kpis || { MRR: 'N/A', CAC: 'N/A', LTV: 'N/A', Churn: 'N/A' },
          decision: investor.decision || 'N/A',
          next_funding: investor.next_funding || 'N/A',
          confidence_score: investor.confidence_score ?? 0,
          analysis_date: investor.analysis_date || new Date().toISOString()
        };

        setStartupData(normalized);
      } catch (err) {
        console.error('Erreur API:', err);
        setError('Erreur lors de l\'appel API');
      } finally {
        setLoading(false);
      }
    };

    fetchStartupData();
  }, []);

  if (loading) {
    return (
      <DashboardContainer>
        <Header>
          <Title>💰 Investisseur IA</Title>
          <Subtitle>Dashboard d'évaluation et de décision d'investissement</Subtitle>
        </Header>
        <LoadingSpinner>Chargement des données d'investissement...</LoadingSpinner>
      </DashboardContainer>
    );
  }

  if (error) {
    return (
      <DashboardContainer>
        <Header>
          <Title>💰 Investisseur IA</Title>
          <Subtitle>Dashboard d'évaluation et de décision d'investissement</Subtitle>
        </Header>
        <Card>
          <CardTitle>❌ Erreur</CardTitle>
          <p>{error}</p>
        </Card>
      </DashboardContainer>
    );
  }

  return (
    <DashboardContainer>
      <Header>
        <Title>💰 Investisseur IA</Title>
        <Subtitle>Dashboard d'évaluation et de décision d'investissement</Subtitle>
      </Header>

      <GridContainer>
        {/* Section Valorisation */}
        <ValuationCard>
          <CardTitle>📊 Valorisation</CardTitle>
          <ValuationAmount>{startupData.valuation}</ValuationAmount>
          
          <div style={{ height: '200px', marginTop: '20px' }}>
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={valuationData}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.2)" />
                <XAxis 
                  dataKey="month" 
                  stroke="#b8c5d6"
                  tick={{ fill: '#b8c5d6' }}
                />
                <YAxis 
                  stroke="#b8c5d6"
                  tick={{ fill: '#b8c5d6' }}
                  domain={[0, 3]}
                  tickFormatter={(value) => `${value}M€`}
                />
                <Tooltip 
                  contentStyle={{
                    backgroundColor: 'rgba(0,0,0,0.8)',
                    border: '1px solid rgba(255,255,255,0.2)',
                    borderRadius: '10px'
                  }}
                  labelStyle={{ color: '#ffffff' }}
                />
                <Line 
                  type="monotone" 
                  dataKey="value" 
                  stroke="#00d4ff" 
                  strokeWidth={3}
                  dot={{ fill: '#00d4ff', strokeWidth: 2, r: 6 }}
                  activeDot={{ r: 8, stroke: '#00d4ff', strokeWidth: 2 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </ValuationCard>

        {/* Section KPIs */}
        <KPICard>
          <CardTitle>📈 KPIs Business</CardTitle>
          <KPITable>
            {Object.entries(startupData.kpis).map(([key, value]) => (
              <KPIRow key={key}>
                <KPILabel>{key}</KPILabel>
                <KPIValue>{value}</KPIValue>
              </KPIRow>
            ))}
          </KPITable>
          
          <ConfidenceScore>
            <ConfidenceLabel>Score de confiance</ConfidenceLabel>
            <ConfidenceBar>
              <ConfidenceFill confidence={startupData.confidence_score} />
            </ConfidenceBar>
            <div style={{ marginTop: '10px', color: '#00d4ff', fontWeight: 'bold' }}>
              {Math.round(startupData.confidence_score * 100)}%
            </div>
          </ConfidenceScore>
        </KPICard>

        {/* Section Décision */}
        <DecisionCard>
          <CardTitle>🚀 Décision d'Investissement</CardTitle>
          
          <DecisionBadge decision={startupData.decision}>
            {startupData.decision}
          </DecisionBadge>
          
          <FundingPlan>
            <FundingTitle>💰 Plan de Financement</FundingTitle>
            <FundingDetails>{startupData.next_funding}</FundingDetails>
          </FundingPlan>
          
          <div style={{ marginTop: '20px', textAlign: 'center' }}>
            <div style={{ color: '#b8c5d6', marginBottom: '10px' }}>
              Date d'analyse
            </div>
            <div style={{ color: '#ffffff', fontWeight: 'bold' }}>
              {new Date(startupData.analysis_date).toLocaleDateString('fr-FR', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
              })}
            </div>
          </div>
        </DecisionCard>
      </GridContainer>
    </DashboardContainer>
  );
};

export default InvestorDashboard;