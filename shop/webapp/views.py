from django.shortcuts import render
from .models import Product

# Create your views here.


def index_view(request):
    products = Product.objects.all()
    products = {'products': products}
    return render(request, "index.html", context=products)


def detail_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

