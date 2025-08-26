from flask import Flask, request, jsonify
from core_engine.agents import CEOAgent, CTOAgent
import logging

app = Flask(__name__)

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialisation des agents
ceo_agent = CEOAgent()
cto_agent = CTOAgent()


@app.route('/create-startup', methods=['POST'])
def create_startup():
    """
    Endpoint principal pour créer une startup
    Orchestre les agents CEO et CTO
    """
    try:
        # Récupération de l'idée depuis la requête
        data = request.get_json()
        idea = data.get('idea', '')
        
        if not idea:
            return jsonify({"error": "L'idée est requise"}), 400
        
        logger.info(f"Création de startup pour l'idée: {idea}")
        
        # Étape 1: Génération de la roadmap business par le CEO
        logger.info("Appel du CEOAgent pour générer la roadmap")
        roadmap = ceo_agent.run(idea)
        
        # Étape 2: Génération de la stack technique par le CTO
        logger.info("Appel du CTOAgent pour générer la stack technique")
        stack_info = cto_agent.run(roadmap)
        
        # Construction de la réponse finale
        response = {
            "success": True,
            "idea": idea,
            "roadmap": roadmap,
            "technical_stack": stack_info,
            "message": "Startup créée avec succès! Consultez le dossier /generated pour le scaffold du projet."
        }
        
        logger.info("Startup créée avec succès")
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Erreur lors de la création de la startup: {str(e)}")
        return jsonify({
            "success": False,
            "error": f"Erreur interne: {str(e)}"
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de vérification de santé"""
    return jsonify({
        "status": "healthy",
        "agents": ["CEOAgent", "CTOAgent"],
        "endpoints": ["/create-startup", "/health"]
    }), 200


if __name__ == '__main__':
    logger.info("Démarrage de l'application Startup Creator")
    logger.info("Agents disponibles: CEOAgent, CTOAgent")
    app.run(debug=True, host='0.0.0.0', port=5000)