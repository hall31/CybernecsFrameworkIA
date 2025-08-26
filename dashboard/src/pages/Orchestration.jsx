import React, { useEffect, useState } from "react";
import AgentCard from "../components/AgentCard";
import EpicCard from "../components/EpicCard";
import { mockAgents, mockEpics } from "../mockData";

export default function Orchestration() {
  const [agents, setAgents] = useState([]);
  const [epics, setEpics] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = async () => {
    try {
      setLoading(true);
      setError(null);
      
      // En mode développement, utiliser les données de test
      if (process.env.NODE_ENV === 'development') {
        // Simuler un délai réseau
        await new Promise(resolve => setTimeout(resolve, 500));
        setAgents(mockAgents);
        setEpics(mockEpics);
        return;
      }
      
      // En production, appeler l'API réelle
      const [resAgents, resEpics] = await Promise.all([
        fetch(`${API_BASE_URL}/agents`),
        fetch(`${API_BASE_URL}/epics`)
      ]);

      if (!resAgents.ok || !resEpics.ok) {
        throw new Error("Erreur lors de la récupération des données");
      }

      const agentsData = await resAgents.json();
      const epicsData = await resEpics.json();
      
      setAgents(agentsData);
      setEpics(epicsData);
    } catch (err) {
      setError(err.message);
      console.error("Erreur fetch:", err);
    } finally {
      setLoading(false);
    }
  };

  const toggleAgent = async (name) => {
    try {
      // En mode développement, simuler le toggle
      if (process.env.NODE_ENV === 'development') {
        setAgents(prev => prev.map(agent => 
          agent.name === name 
            ? { ...agent, enabled: !agent.enabled }
            : agent
        ));
        return;
      }
      
      // En production, appeler l'API réelle
      const response = await fetch(`http://localhost:8000/agents/${name}/toggle`, { 
        method: "POST" 
      });
      
      if (response.ok) {
        await fetchData(); // Rafraîchir les données
      } else {
        throw new Error("Erreur lors du toggle de l'agent");
      }
    } catch (err) {
      console.error("Erreur toggle agent:", err);
      setError("Erreur lors de la modification de l'agent");
    }
  };

  const toggleEpic = async (id) => {
    try {
      // En mode développement, simuler le toggle
      if (process.env.NODE_ENV === 'development') {
        setEpics(prev => prev.map(epic => 
          epic.id === id 
            ? { ...epic, enabled: !epic.enabled }
            : epic
        ));
        return;
      }
      
      // En production, appeler l'API réelle
      const response = await fetch(`http://localhost:8000/epics/${id}/toggle`, { 
        method: "POST" 
      });
      
      if (response.ok) {
        await fetchData(); // Rafraîchir les données
      } else {
        throw new Error("Erreur lors du toggle de l'épic");
      }
    } catch (err) {
      console.error("Erreur toggle epic:", err);
      setError("Erreur lors de la modification de l'épic");
    }
  };

  const runEpic = async (id) => {
    try {
      // En mode développement, simuler l'exécution
      if (process.env.NODE_ENV === 'development') {
        setEpics(prev => prev.map(epic => 
          epic.id === id 
            ? { ...epic, status: "running" }
            : epic
        ));
        
        // Simuler la fin de l'exécution après 2 secondes
        setTimeout(() => {
          setEpics(prev => prev.map(epic => 
            epic.id === id 
              ? { ...epic, status: "done" }
              : epic
          ));
        }, 2000);
        return;
      }
      
      // En production, appeler l'API réelle
      const response = await fetch(`http://localhost:8000/epics/${id}/run`, { 
        method: "POST" 
      });
      
      if (response.ok) {
        await fetchData(); // Rafraîchir les données
      } else {
        throw new Error("Erreur lors de l'exécution de l'épic");
      }
    } catch (err) {
      console.error("Erreur run epic:", err);
      setError("Erreur lors de l'exécution de l'épic");
    }
  };

  useEffect(() => { 
    fetchData(); 
  }, []);

  if (loading) {
    return (
      <div className="p-6 flex items-center justify-center min-h-screen">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Chargement de l'orchestration...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="p-6 space-y-8 bg-gray-50 min-h-screen">
      {/* Header avec titre et bouton rafraîchir */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">⚙️ Orchestration Admin</h1>
          <p className="text-gray-600 mt-2">Gérez vos agents et épics en temps réel</p>
        </div>
        
        <button
          onClick={fetchData}
          className="px-6 py-3 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition-colors duration-200 flex items-center space-x-2 hover:shadow-md"
        >
          <span>🔄</span>
          <span>Rafraîchir</span>
        </button>
      </div>

      {/* Message d'erreur */}
      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4">
          <div className="flex">
            <div className="flex-shrink-0">
              <span className="text-red-400">⚠️</span>
            </div>
            <div className="ml-3">
              <p className="text-sm text-red-800">{error}</p>
            </div>
          </div>
        </div>
      )}

      {/* Section Agents */}
      <section className="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xl font-semibold text-gray-900">🤖 Agents</h2>
          <span className="px-3 py-1 bg-blue-100 text-blue-800 text-sm font-medium rounded-full">
            {agents.length} agent{agents.length > 1 ? 's' : ''}
          </span>
        </div>
        
        {agents.length === 0 ? (
          <div className="text-center py-8 text-gray-500">
            <span className="text-4xl mb-4 block">🤖</span>
            <p>Aucun agent configuré</p>
          </div>
        ) : (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
            {agents.map((agent) => (
              <AgentCard 
                key={agent.name} 
                {...agent} 
                toggleAgent={toggleAgent} 
              />
            ))}
          </div>
        )}
      </section>

      {/* Section Épics */}
      <section className="bg-white rounded-xl p-6 shadow-sm border border-gray-100">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-xl font-semibold text-gray-900">📋 Épics</h2>
          <span className="px-3 py-1 bg-green-100 text-green-800 text-sm font-medium rounded-full">
            {epics.length} épic{epics.length > 1 ? 's' : ''}
          </span>
        </div>
        
        {epics.length === 0 ? (
          <div className="text-center py-8 text-gray-500">
            <span className="text-4xl mb-4 block">📋</span>
            <p>Aucun épic configuré</p>
          </div>
        ) : (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
            {epics.map((epic) => (
              <EpicCard 
                key={epic.id} 
                {...epic} 
                toggleEpic={toggleEpic} 
                runEpic={runEpic} 
              />
            ))}
          </div>
        )}
      </section>
    </div>
  );
}