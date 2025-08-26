import React from 'react'
import './App.css'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>🚀 Startup Creator - Epic2</h1>
        <p>Votre startup a été créée avec succès !</p>
      </header>
      
      <main className="App-main">
        <section className="tech-stack">
          <h2>🔧 Stack Technique</h2>
          <div className="stack-grid">
            <div className="stack-item">
              <h3>Backend</h3>
              <p>Laravel (PHP 8.2)</p>
              <p>Port: 9000</p>
            </div>
            <div className="stack-item">
              <h3>Frontend</h3>
              <p>React + Vite</p>
              <p>Port: 3000</p>
            </div>
            <div className="stack-item">
              <h3>Base de données</h3>
              <p>PostgreSQL 15</p>
              <p>Port: 5432</p>
            </div>
          </div>
        </section>
        
        <section className="next-steps">
          <h2>🚀 Prochaines étapes</h2>
          <ol>
            <li>Développer les fonctionnalités métier</li>
            <li>Configurer l'authentification</li>
            <li>Implémenter la logique de paiement</li>
            <li>Déployer en production</li>
          </ol>
        </section>
      </main>
      
      <footer className="App-footer">
        <p>Généré automatiquement par Epic2 - Startup Creator</p>
      </footer>
    </div>
  )
}

export default App