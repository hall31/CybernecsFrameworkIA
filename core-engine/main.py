#!/usr/bin/env python3
"""
Main Orchestrator - Cybernecs Framework IA
Système de Co-Governance hybride IA+Humains
"""
import logging
import json
from typing import Dict, Any, Optional
from datetime import datetime
import uuid

# Import du système de co-gouvernance
from agents.cogov_agent import CoGovAgent
from agents.codao import CoDAO

# Import des utilitaires
from utils.logger import log_event

from flask import Flask, jsonify, request
from flask_cors import CORS

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Instances du système de co-gouvernance
cogov_agent = CoGovAgent()
codao = CoDAO("Global Co-Governance DAO")

# Routes principales
@app.route("/")
def home():
    """Route d'accueil"""
    return jsonify({
        "message": "Cybernecs Framework IA - Main Orchestrator",
        "version": "1.0.0",
        "status": "operational",
        "features": [
            "Co-Governance System",
            "AI Agents Integration",
            "DAO Management"
        ]
    })

# Routes du système de co-gouvernance
@app.route("/cogov/decision", methods=["POST"])
def create_cogov_decision():
    """Création d'une décision de co-gouvernance"""
    try:
        data = request.get_json()
        topic = data.get("topic")
        ai_vote = data.get("ai_vote")
        human_vote = data.get("human_vote")
        
        if not topic:
            return jsonify({"error": "Le sujet de la décision est requis"}), 400
        
        # Génération de la décision
        decision = cogov_agent.run(
            decision_topic=topic,
            ai_vote=ai_vote,
            human_vote=human_vote
        )
        
        log_event("main", f"Décision de co-gouvernance générée: {decision['final_decision']}")
        
        return jsonify({
            "decision": decision,
            "message": f"Décision générée avec succès pour: {topic}"
        }), 200
        
    except Exception as e:
        logger.error(f"Erreur lors de la génération de la décision: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/cogov/history", methods=["GET"])
def get_decision_history():
    """Récupération de l'historique des décisions"""
    try:
        history = cogov_agent.get_decision_history()
        return jsonify({"decisions": history}), 200
    except Exception as e:
        logger.error(f"Erreur lors de la récupération de l'historique: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/cogov/board-members", methods=["GET"])
def get_board_members():
    """Récupération des membres du conseil"""
    try:
        members = cogov_agent.get_board_members()
        return jsonify(members), 200
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des membres: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/codao/proposal", methods=["POST"])
def create_proposal():
    """Création d'une nouvelle proposition DAO"""
    try:
        data = request.get_json()
        topic = data.get("topic")
        description = data.get("description")
        creator = data.get("creator")
        ai_weighting = data.get("ai_weighting", 50.0)
        human_weighting = data.get("human_weighting", 50.0)
        
        if not all([topic, description, creator]):
            return jsonify({"error": "Topic, description et creator sont requis"}), 400
        
        proposal = codao.create_proposal(
            topic=topic,
            description=description,
            creator=creator,
            ai_weighting=ai_weighting,
            human_weighting=human_weighting
        )
        
        log_event("main", f"Proposition DAO créée: {topic}")
        
        return jsonify({
            "proposal": proposal,
            "message": "Proposition créée avec succès"
        }), 201
        
    except Exception as e:
        logger.error(f"Erreur lors de la création de la proposition: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/codao/vote", methods=["POST"])
def submit_vote():
    """Soumission d'un vote pour une proposition"""
    try:
        data = request.get_json()
        proposal_id = data.get("proposal_id")
        voter = data.get("voter")
        vote = data.get("vote")
        stake_amount = data.get("stake_amount", 100.0)
        
        if not all([proposal_id, voter, vote]):
            return jsonify({"error": "Proposal ID, voter et vote sont requis"}), 400
        
        # Déterminer si c'est un vote IA ou humain
        if any(ai_agent in voter for ai_agent in ["Agent", "AI", "Bot"]):
            result = codao.submit_ai_vote(
                proposal_id=proposal_id,
                ai_agent=voter,
                vote=vote
            )
        else:
            result = codao.submit_human_vote(
                proposal_id=proposal_id,
                voter=voter,
                vote=vote,
                stake_amount=stake_amount
            )
        
        log_event("main", f"Vote soumis pour la proposition: {proposal_id}")
        
        return jsonify(result), 200
        
    except Exception as e:
        logger.error(f"Erreur lors de la soumission du vote: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/codao/proposals", methods=["GET"])
def get_proposals():
    """Récupération de toutes les propositions"""
    try:
        active_proposals = codao.get_active_proposals()
        executed_decisions = codao.get_executed_decisions()
        
        return jsonify({
            "active_proposals": active_proposals,
            "executed_decisions": executed_decisions
        }), 200
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération des propositions: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/codao/execute/<proposal_id>", methods=["POST"])
def execute_proposal(proposal_id):
    """Exécution d'une proposition"""
    try:
        log_event("main", f"Exécution de la proposition: {proposal_id}")
        
        result = codao.execute_proposal(proposal_id)
        return jsonify(result), 200
        
    except Exception as e:
        logger.error(f"Erreur lors de l'exécution de la proposition: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Route de statut du système
@app.route("/status", methods=["GET"])
def system_status():
    """Statut du système et des agents"""
    try:
        status = {
            "system": "operational",
            "timestamp": datetime.now().isoformat(),
            "agents": {
                "cogov_agent": "active",
                "codao": "active"
            },
            "features": {
                "co_governance": "enabled",
                "dao_management": "enabled"
            }
        }
        return jsonify(status), 200
        
    except Exception as e:
        logger.error(f"Erreur lors de la récupération du statut: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    logger.info("Démarrage du Main Orchestrator avec système de co-gouvernance")
    logger.info("Système intégré: Co-Governance + DAO Management")
    app.run(host="0.0.0.0", port=8000, debug=True)