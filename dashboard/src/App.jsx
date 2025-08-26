import React, { useState } from "react";
import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";
import RoadmapCard from "./components/RoadmapCard";
import LogStream from "./components/LogStream";
import GlobalMarket from "./components/GlobalMarket";
import ApiStatus from "./components/ApiStatus";

function App() {
  const [idea, setIdea] = useState("");
  const [roadmap, setRoadmap] = useState(null);
  const [activePage, setActivePage] = useState('home');

  const handleLaunch = async () => {
    const res = await fetch("http://localhost:8000/create-startup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ idea }),
    });
    const data = await res.json();
    setRoadmap(data.roadmap);
  };

  const renderPage = () => {
    switch (activePage) {
      case 'home':
        return (
          <>
            <h1 className="text-2xl font-bold mb-4">🚀 Startup Factory Dashboard</h1>

            <div className="bg-white shadow-md rounded-2xl p-6 mb-6">
              <h2 className="text-lg font-semibold mb-2">Nouvelle idée</h2>
              <div className="flex gap-2">
                <input
                  value={idea}
                  onChange={(e) => setIdea(e.target.value)}
                  placeholder="Ex: SaaS de facturation"
                  className="flex-1 p-2 border rounded-xl"
                />
                <button
                  onClick={handleLaunch}
                  className="px-4 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition"
                >
                  Lancer
                </button>
              </div>
            </div>

            {roadmap && (
              <div className="grid gap-4 md:grid-cols-2">
                {roadmap.epics.map((epic, idx) => (
                  <RoadmapCard key={idx} epic={epic} />
                ))}
              </div>
            )}

            <div className="mt-6">
              <ApiStatus />
            </div>
          </>
        );
      
      case 'roadmap':
        return (
          <>
            <h1 className="text-2xl font-bold mb-4">🗺️ Roadmap des Startups</h1>
            {roadmap ? (
              <div className="grid gap-4 md:grid-cols-2">
                {roadmap.epics.map((epic, idx) => (
                  <RoadmapCard key={idx} epic={epic} />
                ))}
              </div>
            ) : (
              <div className="text-center text-gray-500 py-12">
                <p className="text-lg mb-2">Aucune roadmap disponible</p>
                <p>Créez une nouvelle startup depuis la page d'accueil</p>
              </div>
            )}
          </>
        );
      
      case 'market':
        return <GlobalMarket />;
      
      case 'logs':
        return (
          <>
            <h1 className="text-2xl font-bold mb-4">📋 Logs du Système</h1>
            <LogStream />
          </>
        );
      
      default:
        return null;
    }
  };

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar activePage={activePage} setActivePage={setActivePage} />
      <div className="flex-1 flex flex-col">
        <Topbar />
        <div className="p-6 overflow-auto">
          {renderPage()}
        </div>
      </div>
    </div>
  );
}

export default App;