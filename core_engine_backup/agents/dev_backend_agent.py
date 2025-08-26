import os
import subprocess
import json
from pathlib import Path
from typing import Dict, Any
import logging

class DevBackendAgent:
    """
    Agent responsable du développement backend Laravel
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.backend_path = Path("generated/backend")
        
    def run(self, stack: Dict[str, Any]) -> Dict[str, Any]:
        """
        Exécute le développement backend Laravel
        
        Args:
            stack: Configuration de la stack technique
            
        Returns:
            Dict contenant les informations du backend généré
        """
        self.logger.info("🚀 Démarrage du développement backend Laravel")
        
        try:
            # 1. Initialiser le projet Laravel
            self._init_laravel_project()
            
            # 2. Configurer l'authentification
            self._setup_auth()
            
            # 3. Créer les migrations et modèles
            self._create_database_structure()
            
            # 4. Créer les contrôleurs API
            self._create_api_controllers()
            
            # 5. Configurer les routes API
            self._setup_api_routes()
            
            # 6. Créer les tests
            self._create_tests()
            
            # 7. Configurer CORS et middleware
            self._setup_cors_and_middleware()
            
            self.logger.info("✅ Backend Laravel généré avec succès")
            
            return {
                "status": "success",
                "backend_type": "Laravel",
                "path": str(self.backend_path),
                "features": [
                    "Authentication avec Sanctum",
                    "Users CRUD",
                    "Products CRUD",
                    "API REST complète",
                    "Tests unitaires"
                ],
                "api_endpoints": [
                    "POST /api/login",
                    "POST /api/register", 
                    "GET /api/products",
                    "POST /api/products",
                    "PUT /api/products/{id}",
                    "DELETE /api/products/{id}"
                ]
            }
            
        except Exception as e:
            self.logger.error(f"❌ Erreur lors du développement backend: {str(e)}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _init_laravel_project(self):
        """Initialise le projet Laravel"""
        self.logger.info("📁 Initialisation du projet Laravel")
        
        if not self.backend_path.exists():
            self.backend_path.mkdir(parents=True, exist_ok=True)
            
            # Créer la structure Laravel
            self._create_laravel_structure()
        else:
            self.logger.info("📁 Projet Laravel déjà existant")
    
    def _create_laravel_structure(self):
        """Crée la structure de base Laravel"""
        self.logger.info("🏗️ Création de la structure Laravel")
        
        # Créer composer.json
        composer_json = {
            "name": "startup/backend",
            "type": "project",
            "description": "Backend Laravel pour startup",
            "require": {
                "php": "^8.1",
                "laravel/framework": "^10.0",
                "laravel/sanctum": "^3.0"
            },
            "autoload": {
                "psr-4": {
                    "App\\": "app/"
                }
            }
        }
        
        with open(self.backend_path / "composer.json", "w") as f:
            json.dump(composer_json, f, indent=2)
        
        # Créer la structure des dossiers
        (self.backend_path / "app").mkdir(exist_ok=True)
        (self.backend_path / "app/Http").mkdir(exist_ok=True)
        (self.backend_path / "app/Http/Controllers").mkdir(exist_ok=True)
        (self.backend_path / "app/Models").mkdir(exist_ok=True)
        (self.backend_path / "database/migrations").mkdir(parents=True, exist_ok=True)
        (self.backend_path / "routes").mkdir(exist_ok=True)
        (self.backend_path / "tests").mkdir(exist_ok=True)
        (self.backend_path / "tests/Feature").mkdir(parents=True, exist_ok=True)
        (self.backend_path / "config").mkdir(exist_ok=True)
        
        self.logger.info("✅ Structure Laravel créée")
    
    def _setup_auth(self):
        """Configure l'authentification avec Sanctum"""
        self.logger.info("🔐 Configuration de l'authentification Sanctum")
        
        # Créer le modèle User
        user_model = '''<?php

namespace App\\Models;

use Illuminate\\Foundation\\Auth\\User as Authenticatable;
use Illuminate\\Notifications\\Notifiable;
use Laravel\\Sanctum\\HasApiTokens;

class User extends Authenticatable
{
    use HasApiTokens, Notifiable;

    protected $fillable = [
        'name',
        'email', 
        'password',
        'role'
    ];

    protected $hidden = [
        'password',
        'remember_token',
    ];

    protected $casts = [
        'email_verified_at' => 'datetime',
        'password' => 'hashed',
    ];
}
'''
        
        with open(self.backend_path / "app/Models/User.php", "w") as f:
            f.write(user_model)
        
        # Créer le modèle Product
        product_model = '''<?php

namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;

class Product extends Model
{
    use HasFactory;

    protected $fillable = [
        'name',
        'description', 
        'price',
        'stock'
    ];

    protected $casts = [
        'price' => 'decimal:2',
        'stock' => 'integer'
    ];
}
'''
        
        with open(self.backend_path / "app/Models/Product.php", "w") as f:
            f.write(product_model)
        
        self.logger.info("✅ Modèles User et Product créés")
    
    def _create_database_structure(self):
        """Crée les migrations pour Users et Products"""
        self.logger.info("🗄️ Création des migrations de base de données")
        
        # Migration Users
        users_migration = '''<?php

use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

return new class extends Migration
{
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->timestamp('email_verified_at')->nullable();
            $table->string('password');
            $table->enum('role', ['user', 'admin'])->default('user');
            $table->rememberToken();
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('users');
    }
};
'''
        
        with open(self.backend_path / "database/migrations/2024_01_01_000001_create_users_table.php", "w") as f:
            f.write(users_migration)
        
        # Migration Products
        products_migration = '''<?php

use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

return new class extends Migration
{
    public function up()
    {
        Schema::create('products', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->text('description');
            $table->decimal('price', 10, 2);
            $table->integer('stock');
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('products');
    }
};
'''
        
        with open(self.backend_path / "database/migrations/2024_01_01_000002_create_products_table.php", "w") as f:
            f.write(products_migration)
        
        self.logger.info("✅ Migrations créées")
    
    def _create_api_controllers(self):
        """Crée les contrôleurs API"""
        self.logger.info("🎮 Création des contrôleurs API")
        
        # AuthController
        auth_controller = '''<?php

namespace App\\Http\\Controllers;

use App\\Models\\User;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Hash;
use Illuminate\\Support\\Facades\\Auth;

class AuthController extends Controller
{
    public function register(Request $request)
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|string|email|max:255|unique:users',
            'password' => 'required|string|min:8|confirmed',
        ]);

        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
        ]);

        $token = $user->createToken('auth_token')->plainTextToken;

        return response()->json([
            'user' => $user,
            'token' => $token
        ], 201);
    }

    public function login(Request $request)
    {
        $request->validate([
            'email' => 'required|email',
            'password' => 'required',
        ]);

        if (!Auth::attempt($request->only('email', 'password'))) {
            return response()->json([
                'message' => 'Invalid login credentials'
            ], 401);
        }

        $user = User::where('email', $request->email)->firstOrFail();
        $token = $user->createToken('auth_token')->plainTextToken;

        return response()->json([
            'user' => $user,
            'token' => $token
        ]);
    }

    public function logout(Request $request)
    {
        $request->user()->currentAccessToken()->delete();

        return response()->json([
            'message' => 'Logged out successfully'
        ]);
    }
}
'''
        
        with open(self.backend_path / "app/Http/Controllers/AuthController.php", "w") as f:
            f.write(auth_controller)
        
        # ProductController
        product_controller = '''<?php

namespace App\\Http\\Controllers;

use App\\Models\\Product;
use Illuminate\\Http\\Request;
use Illuminate\\Http\\JsonResponse;

class ProductController extends Controller
{
    public function index(): JsonResponse
    {
        $products = Product::all();
        return response()->json($products);
    }

    public function store(Request $request): JsonResponse
    {
        $request->validate([
            'name' => 'required|string|max:255',
            'description' => 'required|string',
            'price' => 'required|numeric|min:0',
            'stock' => 'required|integer|min:0',
        ]);

        $product = Product::create($request->all());
        return response()->json($product, 201);
    }

    public function show(Product $product): JsonResponse
    {
        return response()->json($product);
    }

    public function update(Request $request, Product $product): JsonResponse
    {
        $request->validate([
            'name' => 'sometimes|string|max:255',
            'description' => 'sometimes|string',
            'price' => 'sometimes|numeric|min:0',
            'stock' => 'sometimes|integer|min:0',
        ]);

        $product->update($request->all());
        return response()->json($product);
    }

    public function destroy(Product $product): JsonResponse
    {
        $product->delete();
        return response()->json(null, 204);
    }
}
'''
        
        with open(self.backend_path / "app/Http/Controllers/ProductController.php", "w") as f:
            f.write(product_controller)
        
        self.logger.info("✅ Contrôleurs API créés")
    
    def _setup_api_routes(self):
        """Configure les routes API"""
        self.logger.info("🛣️ Configuration des routes API")
        
        api_routes = '''<?php

use Illuminate\\Support\\Facades\\Route;
use App\\Http\\Controllers\\AuthController;
use App\\Http\\Controllers\\ProductController;

// Routes publiques
Route::post('/register', [AuthController::class, 'register']);
Route::post('/login', [AuthController::class, 'login']);

// Routes protégées
Route::middleware('auth:sanctum')->group(function () {
    Route::post('/logout', [AuthController::class, 'logout']);
    
    // Products CRUD
    Route::apiResource('products', ProductController::class);
});
'''
        
        with open(self.backend_path / "routes/api.php", "w") as f:
            f.write(api_routes)
        
        self.logger.info("✅ Routes API configurées")
    
    def _create_tests(self):
        """Crée les tests unitaires"""
        self.logger.info("🧪 Création des tests unitaires")
        
        # Test Products API
        products_test = '''<?php

namespace Tests\\Feature;

use Tests\\TestCase;
use App\\Models\\Product;
use App\\Models\\User;
use Illuminate\\Foundation\\Testing\\RefreshDatabase;

class ProductApiTest extends TestCase
{
    use RefreshDatabase;

    public function test_can_get_products()
    {
        $response = $this->getJson('/api/products');
        $response->assertStatus(200);
    }

    public function test_can_create_product()
    {
        $productData = [
            'name' => 'Test Product',
            'description' => 'Test Description',
            'price' => 99.99,
            'stock' => 10
        ];

        $response = $this->postJson('/api/products', $productData);
        $response->assertStatus(201);
        $response->assertJson($productData);
    }

    public function test_can_update_product()
    {
        $product = Product::factory()->create();
        $updateData = ['name' => 'Updated Product'];

        $response = $this->putJson("/api/products/{$product->id}", $updateData);
        $response->assertStatus(200);
        $response->assertJson($updateData);
    }

    public function test_can_delete_product()
    {
        $product = Product::factory()->create();
        $response = $this->deleteJson("/api/products/{$product->id}");
        $response->assertStatus(204);
    }
}
'''
        
        with open(self.backend_path / "tests/Feature/ProductApiTest.php", "w") as f:
            f.write(products_test)
        
        self.logger.info("✅ Tests unitaires créés")
    
    def _setup_cors_and_middleware(self):
        """Configure CORS et middleware"""
        self.logger.info("🔧 Configuration CORS et middleware")
        
        # Config CORS
        cors_config = '''<?php

return [
    'paths' => ['api/*'],
    'allowed_methods' => ['*'],
    'allowed_origins' => ['*'],
    'allowed_origins_patterns' => [],
    'allowed_headers' => ['*'],
    'exposed_headers' => [],
    'max_age' => 0,
    'supports_credentials' => false,
];
'''
        
        (self.backend_path / "config").mkdir(exist_ok=True)
        with open(self.backend_path / "config/cors.php", "w") as f:
            f.write(cors_config)
        
        self.logger.info("✅ Configuration CORS et middleware terminée")