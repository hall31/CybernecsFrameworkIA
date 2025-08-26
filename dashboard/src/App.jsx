import React, { useState } from "react";
import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";
import RoadmapCard from "./components/RoadmapCard";
import LogStream from "./components/LogStream";
import MacroFund from "./components/MacroFund";

function App() {
  const [idea, setIdea] = useState("");
  const [roadmap, setRoadmap] = useState(null);
  const [currentView, setCurrentView] = useState("startup"); // "startup" ou "macrofund"

  const handleLaunch = async () => {
    const res = await fetch("http://localhost:8000/create-startup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ idea }),
    });
    const data = await res.json();
    setRoadmap(data.roadmap);
  };

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Topbar />
        <div className="p-6 overflow-auto">
          {/* Navigation Tabs */}
          <div className="flex gap-2 mb-6">
            <button
              onClick={() => setCurrentView("startup")}
              className={`px-4 py-2 rounded-lg font-medium transition ${
                currentView === "startup"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-200 text-gray-700 hover:bg-gray-300"
              }`}
            >
              🚀 Startup Factory
            </button>
            <button
              onClick={() => setCurrentView("macrofund")}
              className={`px-4 py-2 rounded-lg font-medium transition ${
                currentView === "macrofund"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-200 text-gray-700 hover:bg-gray-300"
              }`}
            >
              📊 Macro Fund
            </button>
          </div>

          {currentView === "startup" ? (
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
                <LogStream />
              </div>
            </>
          ) : (
            <MacroFund />
          )}
        </div>
      </div>
    </div>
  );
}

export default App;