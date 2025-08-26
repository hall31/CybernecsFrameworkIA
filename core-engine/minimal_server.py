#!/usr/bin/env python3

from fastapi import FastAPI
from agents.constitution_agent import ConstitutionAgent

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Constitution Server Running"}

@app.get("/constitution")
async def get_constitution():
    """Récupère la Constitution IA Globale"""
    try:
        # Initialize Constitution Agent
        constitution_agent = ConstitutionAgent()
        
        # Generate constitution
        result = constitution_agent.run()
        
        return {
            "constitution": result["constitution"],
            "markdown": result["markdown"],
            "summary": result["summary"]
        }
        
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    print("🚀 Démarrage du serveur minimal sur le port 8080...")
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")