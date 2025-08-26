<?php

namespace Tests\Feature;

use Tests\TestCase;
use App\Models\Product;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;

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
