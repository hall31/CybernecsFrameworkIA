#!/usr/bin/env python3
"""
Script de lancement de l'API Admin FastAPI
Usage: python run_admin_api.py
"""

import uvicorn

if __name__ == "__main__":
    print("🚀 Démarrage de l'API Admin FastAPI...")
    print("📍 Host: 0.0.0.0")
    print("🔌 Port: 8000")
    print("📚 Documentation: http://localhost:8000/docs")
    print("🔍 Redoc: http://localhost:8000/redoc")
    print("=" * 50)
    
    try:
        uvicorn.run(
            "admin_api:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n🛑 Arrêt de l'API...")
    except Exception as e:
        print(f"❌ Erreur lors du lancement: {e}")
        import traceback
        traceback.print_exc()