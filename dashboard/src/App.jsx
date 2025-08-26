import React, { useState } from "react";
import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";
import RoadmapCard from "./components/RoadmapCard";
import LogStream from "./components/LogStream";
import GlobalMarket from "./components/GlobalMarket";
import ApiStatus from "./components/ApiStatus";
import Orchestration from "./pages/Orchestration";
import FundsPage from "./components/FundsPage";
import CoGovernanceBoard from "./components/CoGovernanceBoard";

function App() {
  const [currentPage, setCurrentPage] = useState("home");
  const [idea, setIdea] = useState("");
  const [roadmap, setRoadmap] = useState(null);

  const handleLaunch = async () => {
    try {
      const res = await fetch("http://localhost:8000/create-startup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ idea }),
      });
      const data = await res.json();
      setRoadmap(data.roadmap);
    } catch (error) {
      console.error("Erreur lors de la création de la startup:", error);
    }
  };

  const renderPage = () => {
    switch (currentPage) {
      case "home":
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

      case "roadmap":
        return (
          <>
            <h1 className="text-2xl font-bold mb-4">📋 Roadmap</h1>
            {roadmap ? (
              <div className="grid gap-4 md:grid-cols-2">
                {roadmap.epics.map((epic, idx) => (
                  <RoadmapCard key={idx} epic={epic} />
                ))}
              </div>
            ) : (
              <div className="text-center py-12 text-gray-500">
                <p className="text-lg mb-2">Aucune roadmap disponible</p>
                <p>Créez une nouvelle startup depuis la page d'accueil</p>
              </div>
            )}
          </>
        );

      case "market":
        return <GlobalMarket />;

      case "orchestration":
        return <Orchestration />;

      case "funds":
        return <FundsPage />;

      case "cogov":
        return <CoGovernanceBoard />;

      case "logs":
        return (
          <>
            <h1 className="text-2xl font-bold mb-4">📊 Logs et Monitoring</h1>
            <LogStream />
          </>
        );

      default:
        return (
          <>
            <h1 className="text-2xl font-bold mb-4">🚀 Startup Factory Dashboard</h1>
            <div className="text-center py-12 text-gray-500">
              <p className="text-lg mb-2">Bienvenue dans le Cybernecs Framework IA</p>
              <p>Sélectionnez une page depuis la barre latérale</p>
            </div>
          </>
        );
    }
  };

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar currentPage={currentPage} setCurrentPage={setCurrentPage} />
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