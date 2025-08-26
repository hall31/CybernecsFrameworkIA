#!/usr/bin/env python3
"""
Script de lancement robuste de l'API Admin FastAPI
"""

import sys
import os
import signal
import time

def main():
    """Lancement de l'API"""
    print("🚀 Démarrage de l'API Admin FastAPI...")
    
    try:
        # Test des imports
        print("📦 Vérification des imports...")
        from admin_api import app
        print("✅ API importée avec succès")
        
        # Test de la configuration
        from config import AGENTS_CONFIG, EPICS
        print(f"✅ Configuration chargée: {len(AGENTS_CONFIG)} agents, {len(EPICS)} épics")
        
        # Lancement avec uvicorn
        print("🌐 Lancement du serveur...")
        import uvicorn
        
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8000,
            reload=False,  # Désactivé pour éviter les problèmes
            log_level="info"
        )
        
    except ImportError as e:
        print(f"❌ Erreur d'import: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    # Gestion de l'arrêt propre
    def signal_handler(sig, frame):
        print("\n🛑 Arrêt de l'API...")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    main()