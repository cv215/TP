from itertools import product
from django.shortcuts import render
from .models import Product, Commande
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    product_objects = Product.objects.all()
    item_name = request.GET.get('item-name', None)
    
    if item_name:
        product_objects = Product.objects.filter(title__icontains=item_name)

    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    return render(request, 'shop/index.html', {'products_objects': product_objects})

def detail(request, product_id):
    product_object = Product.objects.get(id=product_id)
    return render(request, 'shop/details.html', {'product': product_object})

def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Commande(
            items=items,
            total=total,
            nom=nom,
            email=email,
            address=address,
            ville=ville,
            pays=pays,
            zipcode=zipcode
        )
        com.save()

    return render(request, 'shop/checkout.html')