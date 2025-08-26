#!/usr/bin/env python3
"""
Tests du système d'agents IA pour création de startup
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import json

# Import des modules à tester
from core_engine.agents.dev_backend_agent import DevBackendAgent
from core_engine.agents.dev_frontend_agent import DevFrontendAgent
from main import StartupOrchestrator
from config import get_config, get_agent_config, is_agent_enabled

class TestDevBackendAgent(unittest.TestCase):
    """Tests pour DevBackendAgent"""
    
    def setUp(self):
        """Configuration initiale pour chaque test"""
        self.temp_dir = tempfile.mkdtemp()
        self.backend_path = Path(self.temp_dir) / "backend"
        self.agent = DevBackendAgent()
        self.agent.backend_path = self.backend_path
        
        # Configuration de test
        self.test_stack = {
            "backend": {"framework": "Laravel 10"},
            "frontend": {"framework": "React 18"}
        }
    
    def tearDown(self):
        """Nettoyage après chaque test"""
        shutil.rmtree(self.temp_dir)
    
    def test_agent_initialization(self):
        """Test de l'initialisation de l'agent"""
        self.assertIsNotNone(self.agent)
        self.assertIsNotNone(self.agent.logger)
        self.assertEqual(str(self.agent.backend_path), str(self.backend_path))
    
    def test_laravel_structure_creation(self):
        """Test de la création de la structure Laravel"""
        # Créer d'abord le dossier backend
        self.backend_path.mkdir(parents=True, exist_ok=True)
        
        self.agent._create_laravel_structure()
        
        # Vérifier que les dossiers sont créés
        expected_dirs = [
            "app",
            "app/Http",
            "app/Http/Controllers", 
            "app/Models",
            "database/migrations",
            "routes",
            "tests",
            "tests/Feature",
            "config"
        ]
        
        for dir_path in expected_dirs:
            full_path = self.backend_path / dir_path
            self.assertTrue(full_path.exists(), f"Le dossier {dir_path} n'existe pas")
    
    def test_composer_json_creation(self):
        """Test de la création du composer.json"""
        # Créer d'abord le dossier backend
        self.backend_path.mkdir(parents=True, exist_ok=True)
        
        self.agent._create_laravel_structure()
        
        composer_file = self.backend_path / "composer.json"
        self.assertTrue(composer_file.exists())
        
        with open(composer_file, 'r') as f:
            composer_data = json.load(f)
        
        self.assertEqual(composer_data["name"], "startup/backend")
        self.assertEqual(composer_data["type"], "project")
        self.assertIn("laravel/framework", composer_data["require"])
    
    def test_models_creation(self):
        """Test de la création des modèles"""
        # Créer d'abord le dossier backend et la structure
        self.backend_path.mkdir(parents=True, exist_ok=True)
        self.agent._create_laravel_structure()
        
        self.agent._setup_auth()
        
        # Vérifier que les modèles sont créés
        user_model = self.backend_path / "app/Models/User.php"
        product_model = self.backend_path / "app/Models/Product.php"
        
        self.assertTrue(user_model.exists())
        self.assertTrue(product_model.exists())
    
    def test_migrations_creation(self):
        """Test de la création des migrations"""
        # Créer d'abord le dossier backend et la structure
        self.backend_path.mkdir(parents=True, exist_ok=True)
        self.agent._create_laravel_structure()
        
        self.agent._create_database_structure()
        
        # Vérifier que les migrations sont créées
        migrations_dir = self.backend_path / "database/migrations"
        migration_files = list(migrations_dir.glob("*.php"))
        
        self.assertGreaterEqual(len(migration_files), 2)
        
        # Vérifier les noms des migrations
        migration_names = [f.name for f in migration_files]
        self.assertTrue(any("users" in name for name in migration_names))
        self.assertTrue(any("products" in name for name in migration_names))
    
    def test_api_routes_creation(self):
        """Test de la création des routes API"""
        # Créer d'abord le dossier backend et la structure
        self.backend_path.mkdir(parents=True, exist_ok=True)
        self.agent._create_laravel_structure()
        
        self.agent._setup_api_routes()
        
        api_routes_file = self.backend_path / "routes/api.php"
        self.assertTrue(api_routes_file.exists())
        
        with open(api_routes_file, 'r') as f:
            routes_content = f.read()
        
        # Vérifier que les routes sont présentes
        self.assertIn("/register", routes_content)
        self.assertIn("/login", routes_content)
        self.assertIn("products", routes_content)  # Route apiResource crée automatiquement les routes
    
    def test_full_backend_generation(self):
        """Test de la génération complète du backend"""
        result = self.agent.run(self.test_stack)
        
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["backend_type"], "Laravel")
        self.assertIn("Authentication avec Sanctum", result["features"])
        self.assertIn("Products CRUD", result["features"])
        self.assertGreaterEqual(len(result["api_endpoints"]), 6)

class TestDevFrontendAgent(unittest.TestCase):
    """Tests pour DevFrontendAgent"""
    
    def setUp(self):
        """Configuration initiale pour chaque test"""
        self.temp_dir = tempfile.mkdtemp()
        self.frontend_path = Path(self.temp_dir) / "frontend"
        self.agent = DevFrontendAgent()
        self.agent.frontend_path = self.frontend_path
        
        # Configuration de test
        self.test_stack = {
            "backend": {"framework": "Laravel 10"},
            "frontend": {"framework": "React 18"}
        }
    
    def tearDown(self):
        """Nettoyage après chaque test"""
        shutil.rmtree(self.temp_dir)
    
    def test_agent_initialization(self):
        """Test de l'initialisation de l'agent"""
        self.assertIsNotNone(self.agent)
        self.assertIsNotNone(self.agent.logger)
        self.assertEqual(str(self.agent.frontend_path), str(self.frontend_path))
    
    def test_react_structure_creation(self):
        """Test de la création de la structure React"""
        # Créer d'abord le dossier frontend
        self.frontend_path.mkdir(parents=True, exist_ok=True)
        
        # Supprimer le dossier s'il existe pour forcer la recréation
        if (self.frontend_path / "package.json").exists():
            shutil.rmtree(self.frontend_path)
            self.frontend_path.mkdir(parents=True, exist_ok=True)
        
        self.agent._init_react_project()
        
        # Vérifier que les dossiers sont créés
        expected_dirs = [
            "src",
            "src/components",
            "src/pages",
            "src/services",
            "src/hooks",
            "public"
        ]
        
        for dir_path in expected_dirs:
            full_path = self.frontend_path / dir_path
            self.assertTrue(full_path.exists(), f"Le dossier {dir_path} n'existe pas")
    
    def test_package_json_creation(self):
        """Test de la création du package.json"""
        # Créer d'abord le dossier frontend
        self.frontend_path.mkdir(parents=True, exist_ok=True)
        
        # Supprimer le dossier s'il existe pour forcer la recréation
        if (self.frontend_path / "package.json").exists():
            shutil.rmtree(self.frontend_path)
            self.frontend_path.mkdir(parents=True, exist_ok=True)
        
        self.agent._init_react_project()
        
        package_file = self.frontend_path / "package.json"
        self.assertTrue(package_file.exists())
        
        with open(package_file, 'r') as f:
            package_data = json.load(f)
        
        self.assertEqual(package_data["name"], "startup-frontend")
        self.assertEqual(package_data["version"], "0.1.0")
        self.assertIn("react", package_data["dependencies"])
        self.assertIn("tailwindcss", package_data["devDependencies"])
    
    def test_tailwind_configuration(self):
        """Test de la configuration Tailwind"""
        # Créer d'abord le dossier frontend et la structure
        self.frontend_path.mkdir(parents=True, exist_ok=True)
        self.agent._init_react_project()
        
        self.agent._setup_tailwind()
        
        # Vérifier les fichiers de configuration
        tailwind_config = self.frontend_path / "tailwind.config.js"
        postcss_config = self.frontend_path / "postcss.config.js"
        index_css = self.frontend_path / "src/index.css"
        
        self.assertTrue(tailwind_config.exists())
        self.assertTrue(postcss_config.exists())
        self.assertTrue(index_css.exists())
    
    def test_auth_components_creation(self):
        """Test de la création des composants d'authentification"""
        # Créer d'abord le dossier frontend et la structure
        self.frontend_path.mkdir(parents=True, exist_ok=True)
        self.agent._init_react_project()
        
        self.agent._create_auth_components()
        
        # Vérifier que les composants sont créés
        login_page = self.frontend_path / "src/pages/LoginPage.jsx"
        register_page = self.frontend_path / "src/pages/RegisterPage.jsx"
        
        self.assertTrue(login_page.exists())
        self.assertTrue(register_page.exists())
    
    def test_dashboard_components_creation(self):
        """Test de la création des composants du dashboard"""
        # Créer d'abord le dossier frontend et la structure
        self.frontend_path.mkdir(parents=True, exist_ok=True)
        self.agent._init_react_project()
        
        self.agent._create_dashboard_components()
        
        # Vérifier que les composants sont créés
        sidebar = self.frontend_path / "src/components/Sidebar.jsx"
        topbar = self.frontend_path / "src/components/Topbar.jsx"
        dashboard_page = self.frontend_path / "src/pages/DashboardPage.jsx"
        
        self.assertTrue(sidebar.exists())
        self.assertTrue(topbar.exists())
        self.assertTrue(dashboard_page.exists())
    
    def test_full_frontend_generation(self):
        """Test de la génération complète du frontend"""
        result = self.agent.run(self.test_stack)
        
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["frontend_type"], "React + Tailwind")
        self.assertIn("Authentication (Login/Register)", result["features"])
        self.assertIn("Dashboard avec Sidebar + Topbar", result["features"])
        self.assertIn("Gestion des produits (CRUD)", result["features"])

class TestStartupOrchestrator(unittest.TestCase):
    """Tests pour StartupOrchestrator"""
    
    def setUp(self):
        """Configuration initiale pour chaque test"""
        self.temp_dir = tempfile.mkdtemp()
        self.orchestrator = StartupOrchestrator()
        self.orchestrator.generated_path = Path(self.temp_dir)
    
    def tearDown(self):
        """Nettoyage après chaque test"""
        shutil.rmtree(self.temp_dir)
    
    def test_orchestrator_initialization(self):
        """Test de l'initialisation de l'orchestrateur"""
        self.assertIsNotNone(self.orchestrator)
        self.assertIsNotNone(self.orchestrator.logger)
        self.assertEqual(str(self.orchestrator.generated_path), str(self.temp_dir))
    
    def test_ceo_agent_execution(self):
        """Test de l'exécution du CEOAgent"""
        roadmap = self.orchestrator._execute_ceo_agent("Test startup")
        
        self.assertIsInstance(roadmap, dict)
        self.assertIn("vision", roadmap)
        self.assertIn("objectifs", roadmap)
        self.assertIn("etapes", roadmap)
        self.assertIn("metriques", roadmap)
        
        self.assertIn("Test startup", roadmap["vision"])
        self.assertIsInstance(roadmap["objectifs"], list)
        self.assertIsInstance(roadmap["etapes"], list)
    
    def test_cto_agent_execution(self):
        """Test de l'exécution du CTOAgent"""
        roadmap = {"vision": "Test vision"}
        stack = self.orchestrator._execute_cto_agent(roadmap)
        
        self.assertIsInstance(stack, dict)
        self.assertIn("backend", stack)
        self.assertIn("frontend", stack)
        self.assertIn("infrastructure", stack)
        self.assertIn("devops", stack)
        
        self.assertEqual(stack["backend"]["framework"], "Laravel 10")
        self.assertEqual(stack["frontend"]["framework"], "React 18")
    
    def test_docker_compose_creation(self):
        """Test de la création du docker-compose.yml"""
        self.orchestrator._create_docker_compose()
        
        docker_file = self.orchestrator.generated_path / "docker-compose.yml"
        nginx_dir = self.orchestrator.generated_path / "nginx"
        
        self.assertTrue(docker_file.exists())
        self.assertTrue(nginx_dir.exists())
        
        # Vérifier le contenu du docker-compose
        with open(docker_file, 'r') as f:
            docker_content = f.read()
        
        self.assertIn("backend:", docker_content)
        self.assertIn("frontend:", docker_content)
        self.assertIn("mysql:", docker_content)
        self.assertIn("redis:", docker_content)

class TestConfiguration(unittest.TestCase):
    """Tests pour le système de configuration"""
    
    def test_config_loading(self):
        """Test du chargement de la configuration"""
        config = get_config()
        
        self.assertIsInstance(config, dict)
        self.assertIn("general", config)
        self.assertIn("agents", config)
        self.assertIn("infrastructure", config)
    
    def test_agent_config_loading(self):
        """Test du chargement de la configuration d'un agent"""
        backend_config = get_agent_config("dev_backend_agent")
        
        self.assertIsInstance(backend_config, dict)
        self.assertIn("enabled", backend_config)
        self.assertIn("frameworks", backend_config)
        self.assertTrue(backend_config["enabled"])
    
    def test_agent_enabled_check(self):
        """Test de la vérification d'activation d'un agent"""
        self.assertTrue(is_agent_enabled("dev_backend_agent"))
        self.assertTrue(is_agent_enabled("dev_frontend_agent"))
        self.assertTrue(is_agent_enabled("ceo_agent"))
        self.assertTrue(is_agent_enabled("cto_agent"))
    
    def test_available_stacks(self):
        """Test de la récupération des stacks disponibles"""
        from config import get_available_stacks, get_default_stack
        
        stacks = get_available_stacks()
        default_stack = get_default_stack()
        
        self.assertIsInstance(stacks, dict)
        self.assertIn("laravel_react", stacks)
        self.assertIn("node_react", stacks)
        self.assertIn("python_react", stacks)
        self.assertEqual(default_stack, "laravel_react")

def run_tests():
    """Exécute tous les tests"""
    print("🧪 LANCEMENT DES TESTS DU SYSTÈME D'AGENTS")
    print("=" * 60)
    
    # Créer la suite de tests
    test_suite = unittest.TestSuite()
    
    # Ajouter les tests
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDevBackendAgent))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDevFrontendAgent))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestStartupOrchestrator))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestConfiguration))
    
    # Exécuter les tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Résumé des résultats
    print("\n" + "=" * 60)
    print("📊 RÉSULTATS DES TESTS")
    print("=" * 60)
    print(f"Tests exécutés: {result.testsRun}")
    print(f"Échecs: {len(result.failures)}")
    print(f"Erreurs: {len(result.errors)}")
    
    if result.failures:
        print("\n❌ ÉCHECS:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback}")
    
    if result.errors:
        print("\n🚨 ERREURS:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback}")
    
    if result.wasSuccessful():
        print("\n✅ TOUS LES TESTS ONT RÉUSSI!")
    else:
        print("\n❌ CERTAINS TESTS ONT ÉCHOUÉ")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)