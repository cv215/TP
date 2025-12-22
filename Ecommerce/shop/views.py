from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    product_objects = Product.objects.all()
    return render(request, 'shop/index.html', {'products_objects': product_objects})