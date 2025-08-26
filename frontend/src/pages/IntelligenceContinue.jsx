import React, { useState, useEffect } from 'react';
import {
  BarChart, Bar, PieChart, Pie, Cell, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
  Area, AreaChart
} from 'recharts';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Button } from '../components/ui/button';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { Progress } from '../components/ui/progress';

const IntelligenceContinue = () => {
  const [epic10Data, setEpic10Data] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('feedback');

  // Données simulées pour la démonstration
  const mockEpic10Data = {
    feedback: {
      issues: ["Bug checkout", "UI lente", "Erreur 500 sur paiement", "Mode sombre manquant"],
      features_requested: ["Mode sombre", "Intégration PayPal", "Notifications push", "API webhook"],
      sentiment: "78% positif",
      priority_issues: ["Erreur 500 sur paiement"],
      user_satisfaction_score: 7.8
    },
    iteration: {
      user_stories: [
        { id: "bug_1", type: "bug_fix", title: "Corriger: Erreur 500 sur paiement", priority: "high", effort_days: 1 },
        { id: "feature_1", type: "new_feature", title: "Implémenter: Mode sombre", priority: "medium", effort_days: 3 },
        { id: "feature_2", type: "new_feature", title: "Implémenter: Intégration PayPal", priority: "medium", effort_days: 5 }
      ],
      roadmap: {
        sprints: [
          { sprint_number: 1, total_effort: 4, estimated_duration: "2 semaines" },
          { sprint_number: 2, total_effort: 5, estimated_duration: "2 semaines" }
        ]
      }
    },
    optimizer: {
      pricing_changes: ["Pro passe à 91€/mois (+15%)", "Starter passe à 30€/mois (+20%)"],
      ads_budget_shift: ["+20% LinkedIn, budget: 1500€ → 1800€", "-10% Google, budget: 3000€ → 2700€"],
      roi_projection: "ROI +15.2% attendu"
    }
  };

  useEffect(() => {
    // Simulation du chargement des données
    setTimeout(() => {
      setEpic10Data(mockEpic10Data);
      setLoading(false);
    }, 1500);
  }, []);

  // Données pour les graphiques
  const sentimentData = [
    { name: 'Positif', value: 78, color: '#10b981' },
    { name: 'Neutre', value: 15, color: '#6b7280' },
    { name: 'Négatif', value: 7, color: '#ef4444' }
  ];

  const issuesData = [
    { name: 'Bugs', count: 2, color: '#ef4444' },
    { name: 'UX', count: 1, color: '#f59e0b' },
    { name: 'Fonctionnalités', count: 4, color: '#3b82f6' }
  ];

  const sprintProgressData = [
    { name: 'Sprint 1', completed: 4, total: 4, progress: 100 },
    { name: 'Sprint 2', completed: 2, total: 5, progress: 40 }
  ];

  const budgetData = [
    { name: 'Google Ads', current: 3000, recommended: 2700, change: -10 },
    { name: 'LinkedIn Ads', current: 1500, recommended: 1800, change: 20 },
    { name: 'Facebook Ads', current: 1000, recommended: 1000, change: 0 }
  ];

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-lg text-gray-600">Chargement de l'Intelligence Continue...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            🧠 Intelligence Continue
          </h1>
          <p className="text-lg text-gray-600">
            Dashboard temps réel des agents d'IA autonomes - Epic10
          </p>
        </div>

        {/* Métriques principales */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <Card className="bg-gradient-to-r from-blue-500 to-blue-600 text-white">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-blue-100 text-sm">Issues Identifiées</p>
                  <p className="text-3xl font-bold">{epic10Data.feedback.issues.length}</p>
                </div>
                <div className="text-4xl">🐛</div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-r from-green-500 to-green-600 text-white">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-green-100 text-sm">User Stories</p>
                  <p className="text-3xl font-bold">{epic10Data.iteration.user_stories.length}</p>
                </div>
                <div className="text-4xl">📋</div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-r from-purple-500 to-purple-600 text-white">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-purple-100 text-sm">Optimisations</p>
                  <p className="text-3xl font-bold">
                    {epic10Data.optimizer.pricing_changes.length + epic10Data.optimizer.ads_budget_shift.length}
                  </p>
                </div>
                <div className="text-4xl">📈</div>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-r from-orange-500 to-orange-600 text-white">
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-orange-100 text-sm">Satisfaction</p>
                  <p className="text-3xl font-bold">{epic10Data.feedback.user_satisfaction_score}/10</p>
                </div>
                <div className="text-4xl">😊</div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Tabs principaux */}
        <Tabs value={activeTab} onValueChange={setActiveTab} className="space-y-6">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="feedback" className="flex items-center gap-2">
              💬 Feedback Client
            </TabsTrigger>
            <TabsTrigger value="iteration" className="flex items-center gap-2">
              🔄 Itération Produit
            </TabsTrigger>
            <TabsTrigger value="optimizer" className="flex items-center gap-2">
              📈 Optimisation Business
            </TabsTrigger>
          </TabsList>

          {/* Tab Feedback Client */}
          <TabsContent value="feedback" className="space-y-6">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* Graphique sentiment */}
              <Card>
                <CardHeader>
                  <CardTitle>Sentiment Utilisateur</CardTitle>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={300}>
                    <PieChart>
                      <Pie
                        data={sentimentData}
                        cx="50%"
                        cy="50%"
                        labelLine={false}
                        label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                        outerRadius={80}
                        fill="#8884d8"
                        dataKey="value"
                      >
                        {sentimentData.map((entry, index) => (
                          <Cell key={`cell-${index}`} fill={entry.color} />
                        ))}
                      </Pie>
                      <Tooltip />
                    </PieChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>

              {/* Graphique types d'issues */}
              <Card>
                <CardHeader>
                  <CardTitle>Types d'Issues</CardTitle>
                </CardHeader>
                <CardContent>
                  <ResponsiveContainer width="100%" height={300}>
                    <BarChart data={issuesData}>
                      <CartesianGrid strokeDasharray="3 3" />
                      <XAxis dataKey="name" />
                      <YAxis />
                      <Tooltip />
                      <Bar dataKey="count" fill="#3b82f6" />
                    </BarChart>
                  </ResponsiveContainer>
                </CardContent>
              </Card>
            </div>

            {/* Liste des issues et demandes */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    🚨 Issues Prioritaires
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {epic10Data.feedback.issues.map((issue, index) => (
                      <div key={index} className="flex items-center gap-3 p-3 bg-red-50 rounded-lg">
                        <Badge variant="destructive">Bug</Badge>
                        <span className="text-sm">{issue}</span>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle className="flex items-center gap-2">
                    ✨ Fonctionnalités Demandées
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    {epic10Data.feedback.features_requested.map((feature, index) => (
                      <div key={index} className="flex items-center gap-3 p-3 bg-blue-50 rounded-lg">
                        <Badge variant="secondary">Feature</Badge>
                        <span className="text-sm">{feature}</span>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>
            </div>
          </TabsContent>

          {/* Tab Itération Produit */}
          <TabsContent value="iteration" className="space-y-6">
            {/* Progression des sprints */}
            <Card>
              <CardHeader>
                <CardTitle>📅 Progression des Sprints</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-6">
                  {epic10Data.iteration.roadmap.sprints.map((sprint, index) => (
                    <div key={index} className="space-y-2">
                      <div className="flex items-center justify-between">
                        <span className="font-medium">{sprint.name}</span>
                        <span className="text-sm text-gray-500">
                          {(sprint.completed_effort || 0)}/{sprint.total_effort} jours
                        </span>
                      </div>
                      <Progress value={sprint.total_effort ? ((sprint.completed_effort || 0) / sprint.total_effort) * 100 : 0} className="h-2" />
                      <p className="text-sm text-gray-500">{sprint.estimated_duration}</p>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* User Stories */}
            <Card>
              <CardHeader>
                <CardTitle>📋 User Stories Générées</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-4">
                  {epic10Data.iteration.user_stories.map((story) => (
                    <div key={story.id} className="border rounded-lg p-4">
                      <div className="flex items-start justify-between">
                        <div className="flex-1">
                          <h4 className="font-medium">{story.title}</h4>
                          <p className="text-sm text-gray-600 mt-1">
                            Type: {story.type === 'bug_fix' ? '🐛 Bug Fix' : '✨ Nouvelle Feature'}
                          </p>
                          <p className="text-sm text-gray-600">
                            Effort estimé: {story.effort_days} jour(s)
                          </p>
                        </div>
                        <Badge 
                          variant={story.priority === 'high' ? 'destructive' : 'secondary'}
                        >
                          {story.priority}
                        </Badge>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Tab Optimisation Business */}
          <TabsContent value="optimizer" className="space-y-6">
            {/* Optimisations de pricing */}
            <Card>
              <CardHeader>
                <CardTitle>💰 Optimisations de Pricing</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {epic10Data.optimizer.pricing_changes.map((change, index) => (
                    <div key={index} className="flex items-center gap-3 p-3 bg-green-50 rounded-lg">
                      <Badge variant="default" className="bg-green-600">Pricing</Badge>
                      <span className="text-sm">{change}</span>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>

            {/* Réallocation budgétaire */}
            <Card>
              <CardHeader>
                <CardTitle>📊 Réallocation Budgétaire</CardTitle>
              </CardHeader>
              <CardContent>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={budgetData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="current" fill="#6b7280" name="Budget Actuel" />
                    <Bar dataKey="recommended" fill="#3b82f6" name="Budget Recommandé" />
                  </BarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>

            {/* Projection ROI */}
            <Card>
              <CardHeader>
                <CardTitle>🎯 Projection ROI</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="text-center p-6">
                  <div className="text-4xl font-bold text-green-600 mb-2">
                    {epic10Data.optimizer.roi_projection}
                  </div>
                  <p className="text-gray-600">
                    Basé sur les optimisations de pricing et de budget publicitaire
                  </p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>

        {/* Actions rapides */}
        <Card className="mt-8">
          <CardHeader>
            <CardTitle>⚡ Actions Rapides</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex flex-wrap gap-4">
              <Button variant="outline" className="flex items-center gap-2">
                🔄 Rafraîchir les données
              </Button>
              <Button variant="outline" className="flex items-center gap-2">
                📧 Exporter rapport
              </Button>
              <Button variant="outline" className="flex items-center gap-2">
                ⚙️ Configurer alertes
              </Button>
              <Button className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700">
                🚀 Déclencher nouvelle itération
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default IntelligenceContinue;