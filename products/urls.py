from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register the ViewSets
router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'products', views.ProductViewSet, basename='product')

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/product_detail/<int:id>', views.product_detail, name='product_detail'),
    # create_product
    path('product/create/', views.create_product, name='create_product'),
    path('api/', include(router.urls)),  # Include the router's URLs under the 'api/' path
    # Add other URL patterns if needed
]
