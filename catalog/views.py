from django.shortcuts import get_object_or_404, render

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def contacts(request):
    return render(request, "contacts.html")


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)
