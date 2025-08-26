import React, { useState } from 'react';
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
