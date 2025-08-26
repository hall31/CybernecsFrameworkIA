import React, { useEffect, useRef, useState } from 'react';
import { PlayIcon, PauseIcon, TrashIcon } from '@heroicons/react/24/outline';

const LogStream = () => {
  const [logs, setLogs] = useState([]);
  const [isConnected, setIsConnected] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const [ws, setWs] = useState(null);
  const logsEndRef = useRef(null);
  const wsRef = useRef(null);

  const scrollToBottom = () => {
    logsEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [logs]);

  useEffect(() => {
    const connectWebSocket = () => {
      try {
        const wsUrl = process.env.NEXT_PUBLIC_WS_LOGS_URL || 'ws://localhost:8000/ws/logs';
        if (!process.env.NEXT_PUBLIC_WS_LOGS_URL) {
          console.warn('NEXT_PUBLIC_WS_LOGS_URL is not set. Falling back to ws://localhost:8000/ws/logs');
        }
        const websocket = new WebSocket(wsUrl);
        
        websocket.onopen = () => {
          setIsConnected(true);
          console.log('WebSocket connected');
        };

        websocket.onmessage = (event) => {
          if (!isPaused) {
            const logData = JSON.parse(event.data);
            setLogs(prev => [...prev, logData]);
          }
        };

        websocket.onclose = () => {
          setIsConnected(false);
          console.log('WebSocket disconnected');
          // Reconnect after 3 seconds
          setTimeout(connectWebSocket, 3000);
        };

        websocket.onerror = (error) => {
          console.error('WebSocket error:', error);
          setIsConnected(false);
        };

        wsRef.current = websocket;
        setWs(websocket);
      } catch (error) {
        console.error('Failed to connect WebSocket:', error);
        setIsConnected(false);
      }
    };

    connectWebSocket();

    return () => {
      if (wsRef.current) {
        wsRef.current.close();
      }
    };
  }, []);

  const clearLogs = () => {
    setLogs([]);
  };

  const togglePause = () => {
    setIsPaused(!isPaused);
  };

  const formatTimestamp = (timestamp) => {
    return new Date(timestamp).toLocaleTimeString();
  };

  return (
    <div className="card h-full">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-900">Live Logs</h3>
        <div className="flex items-center space-x-2">
          <div className={`w-2 h-2 rounded-full ${isConnected ? 'bg-green-500' : 'bg-red-500'}`}></div>
          <span className="text-sm text-gray-500">
            {isConnected ? 'Connected' : 'Disconnected'}
          </span>
          <button
            onClick={togglePause}
            className="p-2 text-gray-400 hover:text-gray-600 transition-colors duration-200"
            title={isPaused ? 'Resume' : 'Pause'}
          >
            {isPaused ? (
              <PlayIcon className="w-4 h-4" />
            ) : (
              <PauseIcon className="w-4 h-4" />
            )}
          </button>
          <button
            onClick={clearLogs}
            className="p-2 text-gray-400 hover:text-red-600 transition-colors duration-200"
            title="Clear logs"
          >
            <TrashIcon className="w-4 h-4" />
          </button>
        </div>
      </div>

      <div className="bg-black rounded-lg p-4 h-96 overflow-y-auto font-mono text-sm">
        {logs.length === 0 ? (
          <div className="text-gray-400 text-center py-8">
            {isConnected ? 'Waiting for logs...' : 'Connecting to log stream...'}
          </div>
        ) : (
          logs.map((log, index) => (
            <div key={index} className="mb-1">
              <span className="text-gray-400">[{formatTimestamp(log.timestamp)}]</span>
              <span className="text-green-400 ml-2">{log.message}</span>
            </div>
          ))
        )}
        <div ref={logsEndRef} />
      </div>
    </div>
  );
};

export default LogStream;