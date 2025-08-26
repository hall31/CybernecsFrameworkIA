import os
import json
from pathlib import Path
from typing import Dict, Any
import logging

class DevFrontendAgent:
    """
    Agent responsable du développement frontend React + Tailwind
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.frontend_path = Path("generated/frontend")
        
    def run(self, stack: Dict[str, Any]) -> Dict[str, Any]:
        """
        Exécute le développement frontend React + Tailwind
        
        Args:
            stack: Configuration de la stack technique
            
        Returns:
            Dict contenant les informations du frontend généré
        """
        self.logger.info("🚀 Démarrage du développement frontend React + Tailwind")
        
        try:
            # 1. Initialiser le projet React
            self._init_react_project()
            
            # 2. Configurer Tailwind CSS
            self._setup_tailwind()
            
            # 3. Créer les composants d'authentification
            self._create_auth_components()
            
            # 4. Créer le dashboard et la navigation
            self._create_dashboard_components()
            
            # 5. Créer les composants de gestion des produits
            self._create_product_components()
            
            # 6. Créer les services API
            self._create_api_services()
            
            # 7. Configurer le routing
            self._setup_routing()
            
            self.logger.info("✅ Frontend React + Tailwind généré avec succès")
            
            return {
                "status": "success",
                "frontend_type": "React + Tailwind",
                "path": str(self.frontend_path),
                "features": [
                    "Authentication (Login/Register)",
                    "Dashboard avec Sidebar + Topbar",
                    "Gestion des produits (CRUD)",
                    "Design SaaS moderne avec Tailwind",
                    "Intégration API Laravel"
                ],
                "pages": [
                    "/login",
                    "/register", 
                    "/dashboard",
                    "/products"
                ]
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors du développement frontend: {str(e)}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _init_react_project(self):
        """Initialise le projet React"""
        self.logger.info("📁 Initialisation du projet React")
        
        if not self.frontend_path.exists():
            self.frontend_path.mkdir(parents=True, exist_ok=True)
            
            # Créer package.json
            package_json = {
                "name": "startup-frontend",
                "version": "0.1.0",
                "private": True,
                "dependencies": {
                    "react": "^18.2.0",
                    "react-dom": "^18.2.0",
                    "react-router-dom": "^6.8.0",
                    "react-scripts": "5.0.1",
                    "lucide-react": "^0.263.1"
                },
                "scripts": {
                    "start": "react-scripts start",
                    "build": "react-scripts build",
                    "test": "react-scripts test",
                    "eject": "react-scripts eject"
                },
                "devDependencies": {
                    "tailwindcss": "^3.3.0",
                    "autoprefixer": "^10.4.14",
                    "postcss": "^8.4.24"
                }
            }
            
            with open(self.frontend_path / "package.json", "w") as f:
                json.dump(package_json, f, indent=2)
            
            # Créer la structure des dossiers
            (self.frontend_path / "src").mkdir(exist_ok=True)
            (self.frontend_path / "src/components").mkdir(exist_ok=True)
            (self.frontend_path / "src/pages").mkdir(exist_ok=True)
            (self.frontend_path / "src/services").mkdir(exist_ok=True)
            (self.frontend_path / "src/hooks").mkdir(exist_ok=True)
            (self.frontend_path / "public").mkdir(exist_ok=True)
            
            self.logger.info("✅ Structure React créée")
        else:
            self.logger.info("📁 Projet React déjà existant")
    
    def _setup_tailwind(self):
        """Configure Tailwind CSS"""
        self.logger.info("🎨 Configuration de Tailwind CSS")
        
        # tailwind.config.js
        tailwind_config = '''/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
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
}
'''
        
        with open(self.frontend_path / "tailwind.config.js", "w") as f:
            f.write(tailwind_config)
        
        # postcss.config.js
        postcss_config = '''module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
'''
        
        with open(self.frontend_path / "postcss.config.js", "w") as f:
            f.write(postcss_config)
        
        # src/index.css
        index_css = '''@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn-primary {
    @apply bg-primary-600 hover:bg-primary-700 text-white font-medium py-2 px-4 rounded-lg transition-colors;
  }
  
  .btn-secondary {
    @apply bg-gray-200 hover:bg-gray-300 text-gray-800 font-medium py-2 px-4 rounded-lg transition-colors;
  }
  
  .input-field {
    @apply w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent;
  }
}
'''
        
        with open(self.frontend_path / "src/index.css", "w") as f:
            f.write(index_css)
        
        self.logger.info("✅ Tailwind CSS configuré")
    
    def _create_auth_components(self):
        """Crée les composants d'authentification"""
        self.logger.info("🔐 Création des composants d'authentification")
        
        # LoginPage
        login_page = '''import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Eye, EyeOff, Mail, Lock } from 'lucide-react';

const LoginPage = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      
      if (response.ok) {
        const data = await response.json();
        localStorage.setItem('token', data.token);
        localStorage.setItem('user', JSON.stringify(data.user));
        navigate('/dashboard');
      }
    } catch (error) {
      console.error('Login error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <h2 className="text-center text-3xl font-extrabold text-gray-900">
          Connexion
        </h2>
      </div>
      
      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-gray-700">
                Email
              </label>
              <div className="mt-1 relative">
                <Mail className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                <input
                  type="email"
                  required
                  className="input-field pl-10"
                  placeholder="votre@email.com"
                  value={formData.email}
                  onChange={(e) => setFormData({...formData, email: e.target.value})}
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">
                Mot de passe
              </label>
              <div className="mt-1 relative">
                <Lock className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                <input
                  type={showPassword ? 'text' : 'password'}
                  required
                  className="input-field pl-10 pr-10"
                  placeholder="••••••••"
                  value={formData.password}
                  onChange={(e) => setFormData({...formData, password: e.target.value})}
                />
                <button
                  type="button"
                  className="absolute right-3 top-3 text-gray-400 hover:text-gray-600"
                  onClick={() => setShowPassword(!showPassword)}
                >
                  {showPassword ? <EyeOff className="h-5 w-5" /> : <Eye className="h-5 w-5" />}
                </button>
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="btn-primary w-full flex justify-center"
            >
              {loading ? 'Connexion...' : 'Se connecter'}
            </button>
          </form>
          
          <div className="mt-6">
            <div className="text-center">
              <a href="/register" className="text-primary-600 hover:text-primary-500">
                Pas encore de compte ? S'inscrire
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
'''
        
        with open(self.frontend_path / "src/pages/LoginPage.jsx", "w") as f:
            f.write(login_page)
        
        # RegisterPage
        register_page = '''import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Eye, EyeOff, User, Mail, Lock } from 'lucide-react';

const RegisterPage = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    password_confirmation: ''
  });
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const response = await fetch('/api/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      
      if (response.ok) {
        const data = await response.json();
        localStorage.setItem('token', data.token);
        localStorage.setItem('user', JSON.stringify(data.user));
        navigate('/dashboard');
      }
    } catch (error) {
      console.error('Register error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <h2 className="text-center text-3xl font-extrabold text-gray-900">
          Inscription
        </h2>
      </div>
      
      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label className="block text-sm font-medium text-gray-700">
                Nom complet
              </label>
              <div className="mt-1 relative">
                <User className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                <input
                  type="text"
                  required
                  className="input-field pl-10"
                  placeholder="Votre nom"
                  value={formData.name}
                  onChange={(e) => setFormData({...formData, name: e.target.value})}
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">
                Email
              </label>
              <div className="mt-1 relative">
                <Mail className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                <input
                  type="email"
                  required
                  className="input-field pl-10"
                  placeholder="votre@email.com"
                  value={formData.email}
                  onChange={(e) => setFormData({...formData, email: e.target.value})}
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">
                Mot de passe
              </label>
              <div className="mt-1 relative">
                <Lock className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                <input
                  type={showPassword ? 'text' : 'password'}
                  required
                  className="input-field pl-10 pr-10"
                  placeholder="••••••••"
                  value={formData.password}
                  onChange={(e) => setFormData({...formData, password: e.target.value})}
                />
                <button
                  type="button"
                  className="absolute right-3 top-3 text-gray-400 hover:text-gray-600"
                  onClick={() => setShowPassword(!showPassword)}
                >
                  {showPassword ? <EyeOff className="h-5 w-5" /> : <Eye className="h-5 w-5" />}
                </button>
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">
                Confirmer le mot de passe
              </label>
              <div className="mt-1 relative">
                <Lock className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
                <input
                  type="password"
                  required
                  className="input-field pl-10"
                  placeholder="••••••••"
                  value={formData.password_confirmation}
                  onChange={(e) => setFormData({...formData, password_confirmation: e.target.value})}
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="btn-primary w-full flex justify-center"
            >
              {loading ? 'Inscription...' : 'S\'inscrire'}
            </button>
          </form>
          
          <div className="mt-6">
            <div className="text-center">
              <a href="/login" className="text-primary-600 hover:text-primary-500">
                Déjà un compte ? Se connecter
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RegisterPage;
'''
        
        with open(self.frontend_path / "src/pages/RegisterPage.jsx", "w") as f:
            f.write(register_page)
        
        self.logger.info("✅ Composants d'authentification créés")
    
    def _create_dashboard_components(self):
        """Crée le dashboard et la navigation"""
        self.logger.info("🏠 Création du dashboard et de la navigation")
        
        # Sidebar
        sidebar = '''import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { 
  Home, 
  Package, 
  Users, 
  Settings, 
  BarChart3,
  LogOut 
} from 'lucide-react';

const Sidebar = () => {
  const location = useLocation();
  
  const menuItems = [
    { path: '/dashboard', icon: Home, label: 'Dashboard' },
    { path: '/products', icon: Package, label: 'Produits' },
    { path: '/users', icon: Users, label: 'Utilisateurs' },
    { path: '/analytics', icon: BarChart3, label: 'Analytics' },
    { path: '/settings', icon: Settings, label: 'Paramètres' },
  ];

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    window.location.href = '/login';
  };

  return (
    <div className="bg-white shadow-lg w-64 min-h-screen">
      <div className="p-6">
        <h1 className="text-2xl font-bold text-primary-600">StartupApp</h1>
      </div>
      
      <nav className="mt-6">
        {menuItems.map((item) => {
          const Icon = item.icon;
          const isActive = location.pathname === item.path;
          
          return (
            <Link
              key={item.path}
              to={item.path}
              className={`flex items-center px-6 py-3 text-sm font-medium transition-colors ${
                isActive
                  ? 'bg-primary-50 text-primary-600 border-r-2 border-primary-600'
                  : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
              }`}
            >
              <Icon className="mr-3 h-5 w-5" />
              {item.label}
            </Link>
          );
        })}
      </nav>
      
      <div className="absolute bottom-0 w-full p-6">
        <button
          onClick={handleLogout}
          className="flex items-center w-full px-4 py-2 text-sm font-medium text-gray-600 hover:bg-gray-50 hover:text-gray-900 rounded-lg transition-colors"
        >
          <LogOut className="mr-3 h-5 w-5" />
          Déconnexion
        </button>
      </div>
    </div>
  );
};

export default Sidebar;
'''
        
        with open(self.frontend_path / "src/components/Sidebar.jsx", "w") as f:
            f.write(sidebar)
        
        # Topbar
        topbar = '''import React from 'react';
import { Bell, Search, User } from 'lucide-react';

const Topbar = () => {
  const user = JSON.parse(localStorage.getItem('user') || '{}');

  return (
    <div className="bg-white shadow-sm border-b border-gray-200 px-6 py-4">
      <div className="flex items-center justify-between">
        <div className="flex items-center flex-1 max-w-lg">
          <div className="relative w-full">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
            <input
              type="text"
              placeholder="Rechercher..."
              className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
            />
          </div>
        </div>
        
        <div className="flex items-center space-x-4">
          <button className="relative p-2 text-gray-400 hover:text-gray-600 transition-colors">
            <Bell className="h-6 w-6" />
            <span className="absolute top-1 right-1 h-2 w-2 bg-red-500 rounded-full"></span>
          </button>
          
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 bg-primary-600 rounded-full flex items-center justify-center">
              <User className="h-5 w-5 text-white" />
            </div>
            <div className="hidden md:block">
              <p className="text-sm font-medium text-gray-900">{user.name || 'Utilisateur'}</p>
              <p className="text-xs text-gray-500">{user.email || 'user@example.com'}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Topbar;
'''
        
        with open(self.frontend_path / "src/components/Topbar.jsx", "w") as f:
            f.write(topbar)
        
        # DashboardPage
        dashboard_page = '''import React from 'react';
import { BarChart3, Package, Users, TrendingUp } from 'lucide-react';

const DashboardPage = () => {
  const stats = [
    { name: 'Total Produits', value: '156', icon: Package, change: '+12%', changeType: 'positive' },
    { name: 'Utilisateurs Actifs', value: '2,847', icon: Users, change: '+8%', changeType: 'positive' },
    { name: 'Revenus', value: '€45,231', icon: TrendingUp, change: '+23%', changeType: 'positive' },
    { name: 'Taux de Conversion', value: '3.24%', icon: BarChart3, change: '-1%', changeType: 'negative' },
  ];

  return (
    <div className="p-6">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <p className="text-gray-600 mt-2">Bienvenue dans votre espace de gestion</p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {stats.map((stat) => {
          const Icon = stat.icon;
          return (
            <div key={stat.name} className="bg-white rounded-lg shadow p-6">
              <div className="flex items-center">
                <div className="flex-shrink-0">
                  <Icon className="h-8 w-8 text-primary-600" />
                </div>
                <div className="ml-5 w-0 flex-1">
                  <dl>
                    <dt className="text-sm font-medium text-gray-500 truncate">{stat.name}</dt>
                    <dd className="text-lg font-medium text-gray-900">{stat.value}</dd>
                  </dl>
                </div>
              </div>
              <div className="mt-4">
                <span className={`text-sm font-medium ${
                  stat.changeType === 'positive' ? 'text-green-600' : 'text-red-600'
                }`}>
                  {stat.change}
                </span>
                <span className="text-sm text-gray-500 ml-1">vs mois dernier</span>
              </div>
            </div>
          );
        })}
      </div>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-medium text-gray-900 mb-4">Activité Récente</h3>
          <div className="space-y-4">
            {[1, 2, 3, 4, 5].map((i) => (
              <div key={i} className="flex items-center space-x-3">
                <div className="w-2 h-2 bg-primary-600 rounded-full"></div>
                <div className="flex-1">
                  <p className="text-sm text-gray-900">Nouveau produit ajouté</p>
                  <p className="text-xs text-gray-500">Il y a {i} heure{i > 1 ? 's' : ''}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
        
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-medium text-gray-900 mb-4">Produits Populaires</h3>
          <div className="space-y-4">
            {[1, 2, 3].map((i) => (
              <div key={i} className="flex items-center justify-between">
                <div className="flex items-center space-x-3">
                  <div className="w-10 h-10 bg-gray-200 rounded-lg"></div>
                  <div>
                    <p className="text-sm font-medium text-gray-900">Produit {i}</p>
                    <p className="text-xs text-gray-500">Catégorie</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className="text-sm font-medium text-gray-900">€{99 + i * 10}</p>
                  <p className="text-xs text-gray-500">{100 + i * 20} ventes</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
'''
        
        with open(self.frontend_path / "src/pages/DashboardPage.jsx", "w") as f:
            f.write(dashboard_page)
        
        self.logger.info("✅ Dashboard et navigation créés")
    
    def _create_product_components(self):
        """Crée les composants de gestion des produits"""
        self.logger.info("📦 Création des composants de gestion des produits")
        
        # ProductList
        product_list = '''import React, { useState, useEffect } from 'react';
import { Plus, Edit, Trash2, Eye } from 'lucide-react';

const ProductList = ({ onEdit, onDelete, onView }) => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await fetch('/api/products', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      
      if (response.ok) {
        const data = await response.json();
        setProducts(data);
      }
    } catch (error) {
      console.error('Error fetching products:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  return (
    <div className="bg-white shadow rounded-lg">
      <div className="px-6 py-4 border-b border-gray-200">
        <div className="flex items-center justify-between">
          <h3 className="text-lg font-medium text-gray-900">Liste des Produits</h3>
          <button
            onClick={() => onEdit(null)}
            className="btn-primary flex items-center space-x-2"
          >
            <Plus className="h-4 w-4" />
            <span>Ajouter un produit</span>
          </button>
        </div>
      </div>
      
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Produit
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Prix
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Stock
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Actions
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {products.map((product) => (
              <tr key={product.id} className="hover:bg-gray-50">
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className="flex items-center">
                    <div className="w-10 h-10 bg-gray-200 rounded-lg mr-4"></div>
                    <div>
                      <div className="text-sm font-medium text-gray-900">{product.name}</div>
                      <div className="text-sm text-gray-500">{product.description}</div>
                    </div>
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  €{product.price}
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${
                    product.stock > 10 ? 'bg-green-100 text-green-800' : 
                    product.stock > 0 ? 'bg-yellow-100 text-yellow-800' : 
                    'bg-red-100 text-red-800'
                  }`}>
                    {product.stock}
                  </span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div className="flex space-x-2">
                    <button
                      onClick={() => onView(product)}
                      className="text-primary-600 hover:text-primary-900"
                    >
                      <Eye className="h-4 w-4" />
                    </button>
                    <button
                      onClick={() => onEdit(product)}
                      className="text-indigo-600 hover:text-indigo-900"
                    >
                      <Edit className="h-4 w-4" />
                    </button>
                    <button
                      onClick={() => onDelete(product.id)}
                      className="text-red-600 hover:text-red-900"
                    >
                      <Trash2 className="h-4 w-4" />
                    </button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default ProductList;
'''
        
        with open(self.frontend_path / "src/components/ProductList.jsx", "w") as f:
            f.write(product_list)
        
        # ProductForm
        product_form = '''import React, { useState, useEffect } from 'react';
import { X, Save } from 'lucide-react';

const ProductForm = ({ product, onSave, onCancel }) => {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: '',
    stock: ''
  });
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (product) {
      setFormData({
        name: product.name || '',
        description: product.description || '',
        price: product.price || '',
        stock: product.stock || ''
      });
    }
  }, [product]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const token = localStorage.getItem('token');
      const url = product ? `/api/products/${product.id}` : '/api/products';
      const method = product ? 'PUT' : 'POST';
      
      const response = await fetch(url, {
        method,
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(formData)
      });
      
      if (response.ok) {
        onSave();
      }
    } catch (error) {
      console.error('Error saving product:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full z-50">
      <div className="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-medium text-gray-900">
            {product ? 'Modifier le produit' : 'Ajouter un produit'}
          </h3>
          <button
            onClick={onCancel}
            className="text-gray-400 hover:text-gray-600"
          >
            <X className="h-6 w-6" />
          </button>
        </div>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Nom du produit
            </label>
            <input
              type="text"
              required
              className="input-field"
              value={formData.name}
              onChange={(e) => setFormData({...formData, name: e.target.value})}
            />
          </div>
          
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Description
            </label>
            <textarea
              required
              rows="3"
              className="input-field"
              value={formData.description}
              onChange={(e) => setFormData({...formData, description: e.target.value})}
            />
          </div>
          
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Prix
              </label>
              <input
                type="number"
                step="0.01"
                min="0"
                required
                className="input-field"
                value={formData.price}
                onChange={(e) => setFormData({...formData, price: e.target.value})}
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Stock
              </label>
              <input
                type="number"
                min="0"
                required
                className="input-field"
                value={formData.stock}
                onChange={(e) => setFormData({...formData, stock: e.target.value})}
              />
            </div>
          </div>
          
          <div className="flex space-x-3 pt-4">
            <button
              type="button"
              onClick={onCancel}
              className="btn-secondary flex-1"
            >
              Annuler
            </button>
            <button
              type="submit"
              disabled={loading}
              className="btn-primary flex-1 flex items-center justify-center"
            >
              {loading ? (
                <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
              ) : (
                <>
                  <Save className="h-4 w-4 mr-2" />
                  {product ? 'Modifier' : 'Ajouter'}
                </>
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ProductForm;
'''
        
        with open(self.frontend_path / "src/components/ProductForm.jsx", "w") as f:
            f.write(product_form)
        
        # ProductsPage
        products_page = '''import React, { useState } from 'react';
import ProductList from '../components/ProductList';
import ProductForm from '../components/ProductForm';

const ProductsPage = () => {
  const [showForm, setShowForm] = useState(false);
  const [editingProduct, setEditingProduct] = useState(null);

  const handleEdit = (product) => {
    setEditingProduct(product);
    setShowForm(true);
  };

  const handleDelete = async (productId) => {
    if (window.confirm('Êtes-vous sûr de vouloir supprimer ce produit ?')) {
      try {
        const token = localStorage.getItem('token');
        const response = await fetch(`/api/products/${productId}`, {
          method: 'DELETE',
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        
        if (response.ok) {
          // Refresh the page to update the list
          window.location.reload();
        }
      } catch (error) {
        console.error('Error deleting product:', error);
      }
    }
  };

  const handleView = (product) => {
    // Implement product view modal
    console.log('View product:', product);
  };

  const handleSave = () => {
    setShowForm(false);
    setEditingProduct(null);
    // Refresh the page to update the list
    window.location.reload();
  };

  const handleCancel = () => {
    setShowForm(false);
    setEditingProduct(null);
  };

  return (
    <div className="p-6">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Gestion des Produits</h1>
        <p className="text-gray-600 mt-2">Gérez votre catalogue de produits</p>
      </div>
      
      <ProductList
        onEdit={handleEdit}
        onDelete={handleDelete}
        onView={handleView}
      />
      
      {showForm && (
        <ProductForm
          product={editingProduct}
          onSave={handleSave}
          onCancel={handleCancel}
        />
      )}
    </div>
  );
};

export default ProductsPage;
'''
        
        with open(self.frontend_path / "src/pages/ProductsPage.jsx", "w") as f:
            f.write(products_page)
        
        self.logger.info("✅ Composants de gestion des produits créés")
    
    def _create_api_services(self):
        """Crée les services API"""
        self.logger.info("🔌 Création des services API")
        
        # apiService.js
        api_service = '''const API_BASE_URL = '/api';

class ApiService {
  constructor() {
    this.token = localStorage.getItem('token');
  }

  setToken(token) {
    this.token = token;
    localStorage.setItem('token', token);
  }

  getHeaders() {
    return {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${this.token}`
    };
  }

  async request(endpoint, options = {}) {
    const url = `${API_BASE_URL}${endpoint}`;
    const config = {
      headers: this.getHeaders(),
      ...options
    };

    try {
      const response = await fetch(url, config);
      
      if (response.status === 401) {
        // Token expired or invalid
        localStorage.removeItem('token');
        localStorage.removeItem('user');
        window.location.href = '/login';
        return;
      }
      
      return response;
    } catch (error) {
      console.error('API request error:', error);
      throw error;
    }
  }

  // Auth methods
  async login(credentials) {
    const response = await fetch(`${API_BASE_URL}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(credentials)
    });
    
    if (response.ok) {
      const data = await response.json();
      this.setToken(data.token);
      return data;
    }
    
    throw new Error('Login failed');
  }

  async register(userData) {
    const response = await fetch(`${API_BASE_URL}/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
    
    if (response.ok) {
      const data = await response.json();
      this.setToken(data.token);
      return data;
    }
    
    throw new Error('Registration failed');
  }

  async logout() {
    await this.request('/logout', { method: 'POST' });
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  }

  // Product methods
  async getProducts() {
    const response = await this.request('/products');
    return response.json();
  }

  async getProduct(id) {
    const response = await this.request(`/products/${id}`);
    return response.json();
  }

  async createProduct(productData) {
    const response = await this.request('/products', {
      method: 'POST',
      body: JSON.stringify(productData)
    });
    return response.json();
  }

  async updateProduct(id, productData) {
    const response = await this.request(`/products/${id}`, {
      method: 'PUT',
      body: JSON.stringify(productData)
    });
    return response.json();
  }

  async deleteProduct(id) {
    const response = await this.request(`/products/${id}`, {
      method: 'DELETE'
    });
    return response.ok;
  }
}

export default new ApiService();
'''
        
        with open(self.frontend_path / "src/services/apiService.js", "w") as f:
            f.write(api_service)
        
        self.logger.info("✅ Services API créés")
    
    def _setup_routing(self):
        """Configure le routing de l'application"""
        self.logger.info("🛣️ Configuration du routing")
        
        # App.jsx
        app_jsx = '''import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import Topbar from './components/Topbar';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import DashboardPage from './pages/DashboardPage';
import ProductsPage from './pages/ProductsPage';

const PrivateRoute = ({ children }) => {
  const token = localStorage.getItem('token');
  return token ? children : <Navigate to="/login" />;
};

const Layout = ({ children }) => (
  <div className="flex h-screen bg-gray-100">
    <Sidebar />
    <div className="flex-1 flex flex-col overflow-hidden">
      <Topbar />
      <main className="flex-1 overflow-x-hidden overflow-y-auto bg-gray-100">
        {children}
      </main>
    </div>
  </div>
);

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/dashboard" element={
            <PrivateRoute>
              <Layout>
                <DashboardPage />
              </Layout>
            </PrivateRoute>
          } />
          <Route path="/products" element={
            <PrivateRoute>
              <Layout>
                <ProductsPage />
              </Layout>
            </PrivateRoute>
          } />
          <Route path="/" element={<Navigate to="/dashboard" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
'''
        
        with open(self.frontend_path / "src/App.jsx", "w") as f:
            f.write(app_jsx)
        
        # index.js
        index_js = '''import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
'''
        
        with open(self.frontend_path / "src/index.js", "w") as f:
            f.write(index_js)
        
        # public/index.html
        index_html = '''<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="Application de gestion de startup" />
    <title>StartupApp</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
'''
        
        with open(self.frontend_path / "public/index.html", "w") as f:
            f.write(index_html)
        
        self.logger.info("✅ Routing configuré")