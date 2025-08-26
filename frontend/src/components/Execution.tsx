'use client'

import { useState, useEffect } from 'react'
import { 
  Github, 
  CreditCard, 
  TrendingUp,
  ExternalLink,
  CheckCircle,
  Clock,
  AlertCircle,
  RefreshCw
} from 'lucide-react'

interface ExecutionData {
  gitops?: {
    repo_url: string
    status: string
    repo_name?: string
    deployment_status?: string
  }
  payments?: {
    stripe_plans: Array<{
      name: string
      price: string
      features?: string[]
    }>
    checkout_url: string
    status?: string
  }
  ads?: {
    ads_platform: string
    campaign_id: string
    status: string
    budget?: string
    targeting?: any
  }
}

interface ExecutionProps {
  projectId?: string
  idea?: string
}

export default function Execution({ projectId, idea }: ExecutionProps) {
  const [executionData, setExecutionData] = useState<ExecutionData>({})
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  // Simuler le chargement des données d'exécution
  useEffect(() => {
    if (projectId) {
      loadExecutionData()
    }
  }, [projectId])

  const loadExecutionData = async () => {
    setLoading(true)
    setError(null)
    
    try {
      // Appel API réel à /startup/{projectId}
      const response = await fetch(`/startup/${projectId}`);
      if (!response.ok) {
        throw new Error(`Erreur HTTP: ${response.status}`);
      }
      const data: ExecutionData = await response.json();
      setExecutionData(data);
    } catch (err) {
      setError("Erreur lors du chargement des données d'exécution")
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const generateStripePlans = (ideaType: string) => {
    if (ideaType.toLowerCase().includes("marketplace")) {
      return [
        { name: "Starter", price: "29€/mois", features: ["100 utilisateurs", "Support email"] },
        { name: "Pro", price: "79€/mois", features: ["Utilisateurs illimités", "Support prioritaire"] },
        { name: "Enterprise", price: "199€/mois", features: ["Support dédié", "SLA garanti"] }
      ]
    } else if (ideaType.toLowerCase().includes("ai")) {
      return [
        { name: "Starter", price: "39€/mois", features: ["100 requêtes/mois", "Modèles de base"] },
        { name: "Pro", price: "99€/mois", features: ["1000 requêtes/mois", "Modèles avancés"] },
        { name: "Enterprise", price: "299€/mois", features: ["Requêtes illimitées", "Modèles personnalisés"] }
      ]
    } else {
      return [
        { name: "Starter", price: "19€/mois", features: ["Fonctionnalités de base", "1 utilisateur"] },
        { name: "Pro", price: "49€/mois", features: ["Toutes les fonctionnalités", "5 utilisateurs"] },
        { name: "Enterprise", price: "149€/mois", features: ["Support dédié", "Utilisateurs illimités"] }
      ]
    }
  }

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'configured':
      case 'active':
      case 'deployed':
        return <CheckCircle className="w-5 h-5 text-green-500" />
      case 'pending':
      case 'processing':
        return <Clock className="w-5 h-5 text-yellow-500" />
      case 'error':
      case 'failed':
        return <AlertCircle className="w-5 h-5 text-red-500" />
      default:
        return <Clock className="w-5 h-5 text-gray-400" />
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'configured':
      case 'active':
      case 'deployed':
        return 'text-green-600'
      case 'pending':
      case 'processing':
        return 'text-yellow-600'
      case 'error':
      case 'failed':
        return 'text-red-600'
      default:
        return 'text-gray-600'
    }
  }

  const getStatusText = (status: string) => {
    switch (status) {
      case 'configured':
        return 'Configuré'
      case 'active':
        return 'Actif'
      case 'deployed':
        return 'Déployé'
      case 'pending':
        return 'En attente'
      case 'processing':
        return 'En cours'
      case 'error':
        return 'Erreur'
      case 'failed':
        return 'Échec'
      default:
        return status
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="flex items-center space-x-2">
          <RefreshCw className="w-5 h-5 animate-spin text-blue-500" />
          <span className="text-gray-600">Chargement de l'exécution...</span>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="bg-red-50 border border-red-200 rounded-lg p-6">
        <div className="flex items-center space-x-2 text-red-600">
          <AlertCircle className="w-5 h-5" />
          <span className="font-medium">{error}</span>
        </div>
        <button
          onClick={loadExecutionData}
          className="mt-3 text-sm text-red-600 hover:text-red-700 underline"
        >
          Réessayer
        </button>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-semibold text-gray-800">
          🎯 Exécution Automatique
        </h2>
        <button
          onClick={loadExecutionData}
          className="flex items-center space-x-2 text-sm text-gray-600 hover:text-gray-800 transition-colors"
        >
          <RefreshCw className="w-4 h-4" />
          <span>Actualiser</span>
        </button>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Déploiement - Bleu */}
        <div className="bg-white rounded-lg shadow-md border-l-4 border-l-blue-500 p-6">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center space-x-2">
              <Github className="w-6 h-6 text-blue-500" />
              <h3 className="text-lg font-semibold text-gray-800">Déploiement</h3>
            </div>
            {getStatusIcon(executionData.gitops?.status || '')}
          </div>
          
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-sm text-gray-600">Status GitHub:</span>
              <span className={`text-sm font-medium ${getStatusColor(executionData.gitops?.status || '')}`}>
                {getStatusText(executionData.gitops?.status || '')}
              </span>
            </div>
            
            {executionData.gitops?.deployment_status && (
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">Déploiement:</span>
                <span className={`text-sm font-medium ${getStatusColor(executionData.gitops.deployment_status)}`}>
                  {getStatusText(executionData.gitops.deployment_status)}
                </span>
              </div>
            )}
            
            <div className="text-sm text-gray-600 truncate">
              Repo: {executionData.gitops?.repo_name || 'N/A'}
            </div>
            
            <a
              href={executionData.gitops?.repo_url || '#'}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center space-x-2 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-md text-sm font-medium transition-colors"
            >
              <span>Ouvrir sur GitHub</span>
              <ExternalLink className="w-4 h-4" />
            </a>
          </div>
        </div>

        {/* Monétisation - Vert */}
        <div className="bg-white rounded-lg shadow-md border-l-4 border-l-green-500 p-6">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center space-x-2">
              <CreditCard className="w-6 h-6 text-green-500" />
              <h3 className="text-lg font-semibold text-gray-800">Monétisation</h3>
            </div>
            {getStatusIcon(executionData.payments?.status || 'active')}
          </div>
          
          <div className="space-y-3">
            <div className="text-sm text-gray-600">
              Plans Stripe créés: {executionData.payments?.stripe_plans?.length || 0}
            </div>
            
            <div className="space-y-1">
              {executionData.payments?.stripe_plans?.map((plan, index) => (
                <div key={index} className="text-xs text-gray-500">
                  • {plan.name}: {plan.price}
                </div>
              ))}
            </div>
            
            <a
              href={executionData.payments?.checkout_url || '#'}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center space-x-2 bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded-md text-sm font-medium transition-colors"
            >
              <span>Ouvrir checkout</span>
              <ExternalLink className="w-4 h-4" />
            </a>
          </div>
        </div>

        {/* Acquisition - Violet */}
        <div className="bg-white rounded-lg shadow-md border-l-4 border-l-purple-500 p-6">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center space-x-2">
              <TrendingUp className="w-6 h-6 text-purple-500" />
              <h3 className="text-lg font-semibold text-gray-800">Acquisition</h3>
            </div>
            {getStatusIcon(executionData.ads?.status || '')}
          </div>
          
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <span className="text-sm text-gray-600">Plateforme:</span>
              <span className="text-sm font-medium text-gray-800">
                {executionData.ads?.ads_platform || 'N/A'}
              </span>
            </div>
            
            <div className="flex items-center justify-between">
              <span className="text-sm text-gray-600">Status:</span>
              <span className={`text-sm font-medium ${getStatusColor(executionData.ads?.status || '')}`}>
                {getStatusText(executionData.ads?.status || '')}
              </span>
            </div>
            
            {executionData.ads?.budget && (
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-600">Budget:</span>
                <span className="text-sm font-medium text-gray-800">
                  {executionData.ads.budget}
                </span>
              </div>
            )}
            
            <a
              href="#"
              className="inline-flex items-center space-x-2 bg-purple-500 hover:bg-purple-600 text-white px-4 py-2 rounded-md text-sm font-medium transition-colors"
            >
              <span>Voir campagne</span>
              <ExternalLink className="w-4 h-4" />
            </a>
          </div>
        </div>
      </div>

      {/* Résumé de l'exécution */}
      {Object.keys(executionData).length > 0 && (
        <div className="bg-gray-50 rounded-lg p-4">
          <h4 className="font-medium text-gray-800 mb-2">📊 Résumé de l'exécution</h4>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm text-gray-600">
            <div>
              <span className="font-medium">Déploiement:</span> {getStatusText(executionData.gitops?.status || 'N/A')}
            </div>
            <div>
              <span className="font-medium">Monétisation:</span> {getStatusText(executionData.payments?.status || 'N/A')}
            </div>
            <div>
              <span className="font-medium">Acquisition:</span> {getStatusText(executionData.ads?.status || 'N/A')}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}