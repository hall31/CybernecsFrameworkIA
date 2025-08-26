// Données de test pour simuler l'API
export const mockAgents = [
  {
    name: "Agent-001",
    enabled: true,
    status: "active"
  },
  {
    name: "Agent-002", 
    enabled: false,
    status: "disabled"
  },
  {
    name: "Agent-003",
    enabled: true,
    status: "error"
  },
  {
    name: "Agent-004",
    enabled: true,
    status: "active"
  },
  {
    name: "Agent-005",
    enabled: false,
    status: "disabled"
  }
];

export const mockEpics = [
  {
    id: "epic-001",
    name: "Création de la base de données",
    enabled: true,
    status: "done"
  },
  {
    id: "epic-002",
    name: "Développement de l'API",
    enabled: true,
    status: "running"
  },
  {
    id: "epic-003",
    name: "Tests d'intégration",
    enabled: false,
    status: "disabled"
  },
  {
    id: "epic-004",
    name: "Déploiement en production",
    enabled: true,
    status: "pending"
  },
  {
    id: "epic-005",
    name: "Monitoring et alertes",
    enabled: true,
    status: "failed"
  },
  {
    id: "epic-006",
    name: "Documentation utilisateur",
    enabled: true,
    status: "done"
  }
];