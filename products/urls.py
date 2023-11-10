from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('products/product_detail/<int:id>', views.product_detail, name='product_detail'),
 
    # Voeg hier eventueel meer URL-routes toe
]
    