from django.shortcuts import render, get_object_or_404
from .serializers import CategorySerializer, ProductSerializer
from .models import Product, Category
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def products(request):
    # Haal alle producten op uit de database
    products = Product.objects.all()
    rdm_img = "https://source.unsplash.com/400x500/?technology"
    
    # Definieer de context om aan de template door te geven
    context = {
        'products': products,  # Hier geef je de opgehaalde producten door aan de template
        'img': rdm_img,
    }

    # Render de template met de context en geef een HTTP-respons terug
    return render(request, 'products.html', context)

def product_detail(request, id):
    myproduct = get_object_or_404(Product, id=id)
    rdm_img = "https://source.unsplash.com/400x500/?technology"
    context = {
        'product': myproduct,
        'img': rdm_img,
    }
    return render(request, 'product_detail.html', context)


def create_product(request):
    template = loader.get_template('productcreate.html')
    return HttpResponse(template.render({}, request))
  