from django.forms import ModelForm
from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']
