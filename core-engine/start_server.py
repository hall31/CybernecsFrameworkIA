#!/usr/bin/env python3
"""
Script de démarrage du serveur PlanetaryAgent
"""

import uvicorn
from main import app

if __name__ == "__main__":
    print("🚀 Démarrage du serveur PlanetaryAgent...")
    print("📍 API disponible sur: http://localhost:8000")
    print("🌍 Endpoint planétaire: http://localhost:8000/planetary")
    print("📚 Documentation: http://localhost:8000/docs")
    print("=" * 50)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )