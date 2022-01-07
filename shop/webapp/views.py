from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product, CHOOSE_CATEGORY

# Create your views here.


def index_view(request):
    products = Product.objects.all()
    products = {'products': products}
    return render(request, "index.html", context=products)


def detail_view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})


def create_view(request):
    if request.method == "GET":
        # return render(request, "create_product.html", {'select': CHOOSE_CATEGORY})
        form = ProductForm()
        return render(request, "create_product.html", {'form': form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():

            product = request.POST.get('product')
            category = request.POST.get('category')
            description = request.POST.get('description')
            balance = request.POST.get('balance')
            price = request.POST.get('price')
            new_product = Product(product=product, category=category,
                                  description=description, balance=balance, price=price)
            new_product.save()
            return redirect('index')
        return render(request, "create_product.html", {'form': form})
        # products = Product.objects.create(product=product,
        #           category=category, description=description, balance=balance, price=price)
        # print(products)
        # return render(request, "product_detail.html", context={'product': products})


def update_view(request, id):
    # product = Product.objects.get(pk=pk)
    product = get_object_or_404(Product, id=id)
    if request.method == "GET":
        form = ProductForm(initial={
            'product': product.product,
            'category': product.category,
            'description': product.description,
            'balance': product.balance,
            'price': product.price,
            })
        return render(request, "update_product.html", {'product': product, 'form': form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.product = request.POST.get('product')
            product.category = request.POST.get('category')
            product.description = request.POST.get('description')
            product.balance = request.POST.get('balance')
            product.price = request.POST.get('price')
            product.save()
            return redirect('detail_view', id=product.id)
        return render(request, "update_product.html", {'product': product, 'form': form})


def delete_view(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == "GET":
        return render(request, "delete_product.html", {"product": product})
    else:
        print(product)
        product.delete()
        return redirect("index")