import React, { useState, useEffect } from "react";

const LogStream = () => {
  const [logs, setLogs] = useState(["[System] Logs démarrés..."]);

  useEffect(() => {
    // TODO: brancher WebSocket plus tard
    const interval = setInterval(() => {
      setLogs((prev) => [...prev, "[CEOAgent] Test log " + new Date().toLocaleTimeString()]);
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="bg-black text-green-400 font-mono text-sm rounded-xl p-4 h-48 overflow-y-auto">
      {logs.map((log, idx) => (
        <div key={idx}>{log}</div>
      ))}
    </div>
  );
};

export default LogStream;