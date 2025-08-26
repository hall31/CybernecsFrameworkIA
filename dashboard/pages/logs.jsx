import React from 'react';
import Layout from '../components/Layout';
import LogStream from '../components/LogStream';

const Logs = () => {
  return (
    <Layout>
      <div className="mb-6">
        <h1 className="text-3xl font-bold text-gray-900">Logs en Temps Réel</h1>
        <p className="text-gray-600 mt-2">
          Surveillez l'activité de vos agents IA en direct
        </p>
      </div>
      
      <div className="h-full">
        <LogStream />
      </div>
    </Layout>
  );
};

export default Logs;