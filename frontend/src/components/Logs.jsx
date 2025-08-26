import React, { useState, useEffect, useRef } from 'react';
import './Logs.css';

const Logs = ({ projectId }) => {
  const [logs, setLogs] = useState([]);
  const [isConnected, setIsConnected] = useState(false);
  const [error, setError] = useState(null);
  const [autoScroll, setAutoScroll] = useState(true);
  const wsRef = useRef(null);
  const logsEndRef = useRef(null);

  const WS_BASE_URL = process.env.REACT_APP_WS_URL || 'ws://localhost:8000';

  useEffect(() => {
    if (projectId) {
      connectWebSocket();
    }

    return () => {
      if (wsRef.current) {
        wsRef.current.close();
      }
    };
  }, [projectId]);

  useEffect(() => {
    if (autoScroll && logsEndRef.current) {
      logsEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [logs, autoScroll]);

  const connectWebSocket = () => {
    try {
      const ws = new WebSocket(`${WS_BASE_URL}/ws/logs/${projectId}`);
      wsRef.current = ws;

      ws.onopen = () => {
        setIsConnected(true);
        setError(null);
        console.log('WebSocket connecté pour le projet:', projectId);
      };

      ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          handleWebSocketMessage(data);
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      };

      ws.onclose = (event) => {
        setIsConnected(false);
        if (event.code !== 1000) {
          setError('Connexion WebSocket fermée. Tentative de reconnexion...');
          // Tentative de reconnexion après 3 secondes
          setTimeout(() => {
            if (projectId) {
              connectWebSocket();
            }
          }, 3000);
        }
      };

      ws.onerror = (error) => {
        console.error('Erreur WebSocket:', error);
        setError('Erreur de connexion WebSocket');
      };

    } catch (error) {
      console.error('Erreur lors de la connexion WebSocket:', error);
      setError('Impossible de se connecter au WebSocket');
    }
  };

  const handleWebSocketMessage = (data) => {
    switch (data.type) {
      case 'initial_logs':
        setLogs(data.logs || []);
        break;
      case 'new_log':
        if (data.log) {
          setLogs(prevLogs => [...prevLogs, data.log]);
        }
        break;
      case 'pong':
        // Gestion du ping/pong pour maintenir la connexion
        break;
      default:
        console.log('Message WebSocket non reconnu:', data);
    }
  };

  const formatTimestamp = (timestamp) => {
    try {
      return new Date(timestamp).toLocaleTimeString('fr-FR', {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      });
    } catch {
      return timestamp;
    }
  };

  const getLogLevel = (message) => {
    if (message.includes('[ERROR]')) return 'error';
    if (message.includes('[WARNING]')) return 'warning';
    if (message.includes('[DEBUG]')) return 'debug';
    return 'info';
  };

  const clearLogs = () => {
    setLogs([]);
  };

  const toggleAutoScroll = () => {
    setAutoScroll(!autoScroll);
  };

  const scrollToBottom = () => {
    if (logsEndRef.current) {
      logsEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const scrollToTop = () => {
    if (logs.length > 0) {
      const firstLog = document.querySelector('.log-entry');
      if (firstLog) {
        firstLog.scrollIntoView({ behavior: 'smooth' });
      }
    }
  };

  if (!projectId) {
    return (
      <div className="logs-container">
        <div className="no-project-selected">
          <p>Aucun projet sélectionné pour afficher les logs.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="logs-container">
      <div className="logs-header">
        <h2>Logs du Projet</h2>
        <div className="logs-controls">
          <button
            className={`btn btn-sm ${autoScroll ? 'btn-active' : 'btn-secondary'}`}
            onClick={toggleAutoScroll}
            title={autoScroll ? 'Auto-scroll activé' : 'Auto-scroll désactivé'}
          >
            {autoScroll ? '🔒' : '🔓'}
          </button>
          <button
            className="btn btn-sm btn-secondary"
            onClick={scrollToTop}
            title="Aller en haut"
          >
            ⬆️
          </button>
          <button
            className="btn btn-sm btn-secondary"
            onClick={scrollToBottom}
            title="Aller en bas"
          >
            ⬇️
          </button>
          <button
            className="btn btn-sm btn-danger"
            onClick={clearLogs}
            title="Effacer les logs"
          >
            🗑️
          </button>
        </div>
      </div>

      <div className="connection-status">
        <span className={`status-indicator ${isConnected ? 'connected' : 'disconnected'}`}>
          {isConnected ? '🟢' : '🔴'}
        </span>
        <span className="status-text">
          {isConnected ? 'Connecté' : 'Déconnecté'}
        </span>
        {error && <span className="error-message">{error}</span>}
      </div>

      <div className="logs-content">
        {logs.length === 0 ? (
          <div className="no-logs">
            <p>Aucun log disponible pour le moment.</p>
            {!isConnected && (
              <p className="connection-hint">
                Vérifiez la connexion WebSocket pour recevoir les logs en temps réel.
              </p>
            )}
          </div>
        ) : (
          <div className="logs-list">
            {logs.map((log, index) => (
              <div
                key={`${log.id || index}-${log.timestamp}`}
                className={`log-entry log-${getLogLevel(log.message)}`}
              >
                <span className="log-timestamp">
                  {formatTimestamp(log.timestamp)}
                </span>
                <span className="log-message">
                  {log.message.replace(/^\[(ERROR|WARNING|INFO|DEBUG)\] /, '')}
                </span>
              </div>
            ))}
            <div ref={logsEndRef} />
          </div>
        )}
      </div>

      <div className="logs-footer">
        <span className="logs-count">
          {logs.length} log{logs.length !== 1 ? 's' : ''} affiché{logs.length !== 1 ? 's' : ''}
        </span>
        <span className="project-id">
          Projet: {projectId}
        </span>
      </div>
    </div>
  );
};

export default Logs;