import os
import json
import base64
from typing import Dict, Any
from github import Github, GithubException
from agents.base_agent import BaseAgent

class GitOpsAgent(BaseAgent):
    """Agent pour la gestion GitOps et déploiement automatique"""
    
    def __init__(self):
        super().__init__()
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.github_username = os.getenv('GITHUB_USERNAME')
        
            raise ValueError("GitHub credentials missing in environment variables")
        
        self.github = Github(self.github_token)
        self.user = self.github.get_user()
    
    def run(self, project_id: str) -> Dict[str, Any]:
        """Exécute le processus GitOps complet"""
        try:
            self.log_event("GitOpsAgent", "Démarrage du processus GitOps", {"project_id": project_id})
            
            # 1. Créer le repository GitHub
            repo_name = f"startup-{project_id}"
            repo = self._create_github_repo(repo_name)
            
            # 2. Pousser le code généré
            self._push_generated_code(repo, project_id)
            
            # 3. Configurer GitHub Actions pour CI/CD
            self._setup_github_actions(repo)
            
            # 4. Configurer les secrets et variables d'environnement
            self._setup_repo_secrets(repo)
            
            result = {
                "repo_url": repo.html_url,
                "status": "pushed",
                "repo_name": repo_name,
                "clone_url": repo.clone_url,
                "deployment_status": "configured"
            }
            
            self.log_event("GitOpsAgent", "Code poussé sur GitHub", result)
            return result
            
        except Exception as e:
            return self.handle_error(e, f"GitOps pour project_id: {project_id}")
    
    def _create_github_repo(self, repo_name: str):
        """Crée un nouveau repository GitHub"""
        try:
            repo = self.user.create_repo(
                repo_name,
                description=f"Startup SaaS généré automatiquement par Mon ShipFast",
                private=False,
                auto_init=True,
                gitignore_template="Node",
                license_template="mit"
            )
            
            self.log_event("GitOpsAgent", "Repository GitHub créé", {"repo_name": repo_name})
            return repo
            
        except GithubException as e:
            if e.status == 422:  # Repository already exists
                repo = self.user.get_repo(repo_name)
                self.log_event("GitOpsAgent", "Repository existant récupéré", {"repo_name": repo_name})
                return repo
            else:
                raise e
    
    def _push_generated_code(self, repo, project_id: str):
        """Pousse le code généré dans le repository"""
        try:
            # Simuler la structure de code généré
            files_to_create = {
                "README.md": self._generate_readme(project_id),
                ".github/workflows/deploy.yml": self._generate_github_actions(),
                "package.json": self._generate_package_json(),
                "next.config.js": self._generate_next_config(),
                "tailwind.config.js": self._generate_tailwind_config(),
                "src/app/page.tsx": self._generate_main_page(),
                "src/app/layout.tsx": self._generate_layout(),
                "src/components/Dashboard.tsx": self._generate_dashboard(),
                "src/components/Execution.tsx": self._generate_execution_component(),
                ".env.local": self._generate_env_template()
            }
            
            for file_path, content in files_to_create.items():
                try:
                    # Vérifier si le fichier existe déjà
                    try:
                        repo.get_contents(file_path)
                        # Fichier existe, le mettre à jour
                        repo.update_file(
                            file_path,
                            f"Update {file_path}",
                            content,
                            repo.get_contents(file_path).sha
                        )
                    except:
                        # Fichier n'existe pas, le créer
                        repo.create_file(
                            file_path,
                            f"Add {file_path}",
                            content
                        )
                    
                except Exception as e:
                    self.logger.warning(f"Erreur lors de la création/mise à jour de {file_path}: {e}")
            
            self.log_event("GitOpsAgent", "Code généré poussé", {"files_count": len(files_to_create)})
            
        except Exception as e:
            raise Exception(f"Erreur lors du push du code: {e}")
    
    def _setup_github_actions(self, repo):
        """Configure GitHub Actions pour CI/CD"""
        try:
            # Le fichier de workflow est déjà créé dans _push_generated_code
            self.log_event("GitOpsAgent", "GitHub Actions configuré")
        except Exception as e:
            self.logger.warning(f"Erreur lors de la configuration GitHub Actions: {e}")
    
    def _setup_repo_secrets(self, repo):
        """Configure les secrets du repository (simulation)"""
        try:
            # Note: GitHub API ne permet pas de créer des secrets via l'API publique
            # L'utilisateur devra les configurer manuellement
            self.log_event("GitOpsAgent", "Secrets du repository à configurer manuellement")
        except Exception as e:
            self.logger.warning(f"Erreur lors de la configuration des secrets: {e}")
    
    def _generate_readme(self, project_id: str) -> str:
        """Génère un README.md personnalisé"""
        return f"""# Startup {project_id}

Ce projet a été généré automatiquement par Mon ShipFast.

## 🚀 Démarrage rapide

1. Clonez le repository
2. Installez les dépendances: `npm install`
3. Configurez vos variables d'environnement
4. Lancez le projet: `npm run dev`

## 🛠️ Technologies

- Next.js 14
- Tailwind CSS
- Supabase
- Stripe
- TypeScript

## 📱 Fonctionnalités

- Dashboard utilisateur
- Authentification
- Paiements Stripe
- Analytics intégrés

## 🔧 Configuration

Copiez `.env.local.example` vers `.env.local` et configurez vos clés API.

## 📊 Déploiement

Le projet se déploie automatiquement sur Vercel via GitHub Actions.
"""
    
    def _generate_github_actions(self) -> str:
        """Génère le workflow GitHub Actions"""
        return """name: Deploy to Vercel

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test
    
    - name: Build project
      run: npm run build
    
    - name: Deploy to Vercel
      uses: amondnet/vercel-action@v25
      with:
        vercel-token: ${{ secrets.VERCEL_TOKEN }}
        vercel-org-id: ${{ secrets.ORG_ID }}
        vercel-project-id: ${{ secrets.PROJECT_ID }}
        vercel-args: '--prod'
"""
    
    def _generate_package_json(self) -> str:
        """Génère le package.json"""
        return """{
  "name": "mon-shipfast-startup",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "jest"
  },
  "dependencies": {
    "next": "14.0.0",
    "react": "^18",
    "react-dom": "^18",
    "@supabase/supabase-js": "^2.38.0",
    "@stripe/stripe-js": "^2.1.0",
    "tailwindcss": "^3.3.0",
    "autoprefixer": "^10.0.0",
    "postcss": "^8.0.0",
    "lucide-react": "^0.292.0"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "typescript": "^5",
    "eslint": "^8",
    "eslint-config-next": "14.0.0",
    "jest": "^29.0.0",
    "@testing-library/react": "^13.0.0"
  }
}"""
    
    def _generate_next_config(self) -> str:
        """Génère la configuration Next.js"""
        return """/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    appDir: true,
  },
  images: {
    domains: ['localhost', 'vercel.app'],
  },
}

module.exports = nextConfig"""
    
    def _generate_tailwind_config(self) -> str:
        """Génère la configuration Tailwind"""
        return """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
        }
      }
    },
  },
  plugins: [],
}"""
    
    def _generate_main_page(self) -> str:
        """Génère la page principale"""
        return """'use client'

import Dashboard from './components/Dashboard'

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50">
      <Dashboard />
    </main>
  )
}"""
    
    def _generate_layout(self) -> str:
        """Génère le layout principal"""
        return """import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Mon ShipFast - Dashboard',
  description: 'Dashboard pour votre startup SaaS',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="fr">
      <body className={inter.className}>{children}</body>
    </html>
  )
}"""
    
    def _generate_dashboard(self) -> str:
        """Génère le composant Dashboard"""
        return """'use client'

import Execution from './Execution'

export default function Dashboard() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-8">
        🚀 Dashboard Mon ShipFast
      </h1>
      
      <Execution />
    </div>
  )
}"""
    
    def _generate_execution_component(self) -> str:
        """Génère le composant Execution avec les 3 cartes demandées"""
        return """'use client'

import { useState } from 'react'
import { 
  Github, 
  CreditCard, 
  TrendingUp,
  ExternalLink,
  CheckCircle,
  Clock,
  AlertCircle
} from 'lucide-react'

interface ExecutionData {
  gitops?: {
    repo_url: string
    status: string
  }
  payments?: {
    stripe_plans: any[]
    checkout_url: string
  }
  ads?: {
    ads_platform: string
    campaign_id: string
    status: string
  }
}

export default function Execution() {
  const [executionData, setExecutionData] = useState<ExecutionData>({
    gitops: {
      repo_url: "https://github.com/user/startup123",
      status: "configured"
    },
    payments: {
      stripe_plans: [
        { name: "Starter", price: "29€/mois" },
        { name: "Pro", price: "79€/mois" },
        { name: "Enterprise", price: "199€/mois" }
      ],
      checkout_url: "https://checkout.stripe.com/..."
    },
    ads: {
      ads_platform: "LinkedIn",
      campaign_id: "camp_123456",
      status: "active"
    }
  })

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'configured':
      case 'active':
        return <CheckCircle className="w-5 h-5 text-green-500" />
      case 'pending':
        return <Clock className="w-5 h-5 text-yellow-500" />
      default:
        return <AlertCircle className="w-5 h-5 text-red-500" />
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'configured':
      case 'active':
        return 'text-green-600'
      case 'pending':
        return 'text-yellow-600'
      default:
        return 'text-red-600'
    }
  }

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-semibold text-gray-800 mb-6">
        🎯 Exécution Automatique
      </h2>
      
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
                {executionData.gitops?.status || 'N/A'}
              </span>
            </div>
            
            <div className="text-sm text-gray-600 truncate">
              Repo: {executionData.gitops?.repo_url || 'N/A'}
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
            {getStatusIcon('active')}
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
                {executionData.ads?.status || 'N/A'}
              </span>
            </div>
            
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
    </div>
  )
}"""
    
    def _generate_env_template(self) -> str:
        """Génère le template .env.local"""
        return """# Configuration Supabase
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key

# Configuration Stripe
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...

# Configuration LinkedIn Ads
LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret

# Configuration Google Ads
GOOGLE_ADS_CLIENT_ID=your_google_ads_client_id
GOOGLE_ADS_CLIENT_SECRET=your_google_ads_client_secret

# Configuration OpenAI
OPENAI_API_KEY=your_openai_api_key"""