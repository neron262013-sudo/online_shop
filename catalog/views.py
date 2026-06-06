from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ContactsView(View):
    def get(self, request):
        return render(request, "contacts.html")


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
