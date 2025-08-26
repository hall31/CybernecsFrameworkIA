#!/usr/bin/env python3

import uvicorn
from main import app

if __name__ == "__main__":
    print("🚀 Démarrage du serveur FastAPI...")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")