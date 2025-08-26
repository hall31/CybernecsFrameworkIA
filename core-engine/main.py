from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
from datetime import datetime
import json

# Import des agents
from agents.portfolio_agent import PortfolioAgent

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialisation de Flask
app = Flask(__name__)
CORS(app)

# Initialisation des agents
portfolio_agent = PortfolioAgent()

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de santé de l'API"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "AI Portfolio Manager API"
    })

@app.route('/portfolio', methods=['GET'])
def get_portfolio():
    """Endpoint principal pour récupérer le tableau de bord du portefeuille"""
    try:
        logger.info("Demande d'analyse du portefeuille reçue")
        
        # Appel du PortfolioAgent
        portfolio_data = portfolio_agent.run()
        
        if "error" in portfolio_data:
            logger.error(f"Erreur lors de l'analyse: {portfolio_data['error']}")
            return jsonify({
                "success": False,
                "error": portfolio_data["error"],
                "timestamp": datetime.now().isoformat()
            }), 500
        
        logger.info("Analyse du portefeuille terminée avec succès")
        
        return jsonify({
            "success": True,
            "data": portfolio_data,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        error_msg = f"Erreur inattendue: {str(e)}"
        logger.error(error_msg)
        return jsonify({
            "success": False,
            "error": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/portfolio/summary', methods=['GET'])
def get_portfolio_summary():
    """Endpoint pour récupérer un résumé du portefeuille (sans nouvelle analyse)"""
    try:
        summary = portfolio_agent.get_portfolio_summary()
        return jsonify({
            "success": True,
            "data": summary,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        error_msg = f"Erreur lors de la récupération du résumé: {str(e)}"
        logger.error(error_msg)
        return jsonify({
            "success": False,
            "error": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/portfolio/startups', methods=['GET'])
def get_startups():
    """Endpoint pour récupérer la liste des startups"""
    try:
        startups = portfolio_agent.get_all_startups()
        return jsonify({
            "success": True,
            "data": {
                "startups": startups,
                "total": len(startups),
                "timestamp": datetime.now().isoformat()
            }
        })
        
    except Exception as e:
        error_msg = f"Erreur lors de la récupération des startups: {str(e)}"
        logger.error(error_msg)
        return jsonify({
            "success": False,
            "error": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/portfolio/startup/<startup_id>', methods=['GET'])
def get_startup(startup_id):
    """Endpoint pour récupérer une startup spécifique"""
    try:
        startups = portfolio_agent.get_all_startups()
        startup = next((s for s in startups if s["id"] == startup_id), None)
        
        if not startup:
            return jsonify({
                "success": False,
                "error": f"Startup {startup_id} non trouvée",
                "timestamp": datetime.now().isoformat()
            }), 404
        
        # Évaluation de la startup
        evaluated_startup = portfolio_agent.evaluate_startup(startup)
        
        return jsonify({
            "success": True,
            "data": evaluated_startup,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        error_msg = f"Erreur lors de la récupération de la startup: {str(e)}"
        logger.error(error_msg)
        return jsonify({
            "success": False,
            "error": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/portfolio/analysis', methods=['POST'])
def analyze_portfolio():
    """Endpoint pour forcer une nouvelle analyse du portefeuille"""
    try:
        logger.info("Demande de nouvelle analyse du portefeuille")
        
        # Force une nouvelle analyse
        portfolio_data = portfolio_agent.run()
        
        if "error" in portfolio_data:
            logger.error(f"Erreur lors de l'analyse: {portfolio_data['error']}")
            return jsonify({
                "success": False,
                "error": portfolio_data["error"],
                "timestamp": datetime.now().isoformat()
            }), 500
        
        logger.info("Nouvelle analyse du portefeuille terminée avec succès")
        
        return jsonify({
            "success": True,
            "data": portfolio_data,
            "message": "Analyse du portefeuille mise à jour",
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        error_msg = f"Erreur lors de l'analyse: {str(e)}"
        logger.error(error_msg)
        return jsonify({
            "success": False,
            "error": error_msg,
            "timestamp": datetime.now().isoformat()
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Gestionnaire d'erreur 404"""
    return jsonify({
        "success": False,
        "error": "Endpoint non trouvé",
        "timestamp": datetime.now().isoformat()
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Gestionnaire d'erreur 500"""
    return jsonify({
        "success": False,
        "error": "Erreur interne du serveur",
        "timestamp": datetime.now().isoformat()
    }), 500

if __name__ == '__main__':
    logger.info("Démarrage de l'AI Portfolio Manager API")
    logger.info("Endpoints disponibles:")
    logger.info("  GET  /health - Vérification de santé")
    logger.info("  GET  /portfolio - Tableau de bord complet")
    logger.info("  GET  /portfolio/summary - Résumé du portefeuille")
    logger.info("  GET  /portfolio/startups - Liste des startups")
    logger.info("  GET  /portfolio/startup/<id> - Détails d'une startup")
    logger.info("  POST /portfolio/analysis - Force une nouvelle analyse")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )