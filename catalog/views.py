from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, View, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class productCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_create.html"
    success_url = reverse_lazy("products")


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_update.html"
    success_url = reverse_lazy("products")

    def get_success_url(self):
        return reverse('product_detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"


class ContactsView(View):
    def get(self, request):
        return render(request, "contacts.html")
