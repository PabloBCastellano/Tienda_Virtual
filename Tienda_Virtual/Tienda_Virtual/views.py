from django.shortcuts import render
from django.http import HttpResponse
from Tienda.models import Product


def home_view(request):
    # return HttpResponse("<h1> Home</h1>")
    return render(request, 'home.html', {})


def catalog_view(request):
    # return HttpResponse("<h1>Catalog</h1>")
    obj = Product.objects.all()
    context = {
        "object": obj
    }
    return render(request, 'catalog.html', context)
    
def product_details_view(request,id):
    # return HttpResponse("<h1>Details of Products</h1>")
    obj = Product.objects.get(id=id)
    
    context = {
        "object": obj
    }
    
    #context = {
    #    "name": obj.name,
    #    "description": obj.description,
    #    "image": obj.image,
    #    "price": obj.price,
    #    "characteristic": obj.characteristic
    #} 
    return render(request, 'details.html', context)


def about_view(request):
    # return HttpResponse("<h1>About me</h1>")
    return render(request, 'about.html', {})
