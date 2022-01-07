from django.shortcuts import render
from .models import Product

# Create your views here.


def index_view(request):
    products = Product.objects.all()
    products = {'products': products}
    return render(request, "index.html", context=products)
