from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, View

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        dog = form.save()
        user = self.request.user
        dog.owner = user
        dog.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        user = request.user

        is_owner = product.owner == user
        is_moderator = user.has_perm("catalog.can_unpublish_product")

        if not (is_owner or is_moderator):
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        user = request.user

        is_owner = product.owner == user
        is_moderator = (
            user.has_perm("catalog.delete_product") and
            user.has_perm("catalog.can_unpublish_product")
        )

        if not (is_owner or is_moderator):
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class ProductUnpublishView(LoginRequiredMixin, View):
    def post(self, request, pk):
        if not request.user.has_perm("catalog.can_unpublish_product"):
            raise PermissionDenied

        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()

        return redirect("catalog:product_detail", pk=pk)


class ProductPublishView(LoginRequiredMixin, View):
    def post(self, request, pk):
        if not request.user.has_perm("catalog.can_unpublish_product"):
            raise PermissionDenied

        product = get_object_or_404(Product, pk=pk)
        product.is_published = True
        product.save()

        return redirect("catalog:product_detail", pk=pk)


class ContactsView(View):
    def get(self, request):
        return render(request, "contacts.html")
