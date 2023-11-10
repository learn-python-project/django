from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Product


def products(request):
    # Haal alle producten op uit de database
    products = Product.objects.all()
    rdm_img = "https://picsum.photos/200/300"
    # Laad de template
    template = loader.get_template('products.html')

    # Definieer de context om aan de template door te geven
    context = {
        'products': products,  # Hier geef je de opgehaalde producten door aan de template
        'img': rdm_img,
    }

    # Render de template met de context en geef een HTTP-respons terug
    return HttpResponse(template.render(context, request))


def product_detail(request, id):
    myproduct = get_object_or_404(Product, id=id)
    template = loader.get_template('product_detail.html')
    rdm_img = "https://picsum.photos/200/300"
    context = {
        'product': myproduct,
        'img': rdm_img,
    }
    return HttpResponse(template.render(context, request))