from itertools import product
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import Product, Commande
from django.contrib import messages
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
        return redirect('confirmation')

    return render(request, 'shop/checkout.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'shop/confirmation.html', {'name': nom})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")

    return render(request, "shop/login.html")