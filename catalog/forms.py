from django.forms import ModelForm
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(ModelForm):
    BANNED_WORDS = [
        'казино', 'криптовалюта', 'крипта',
        'биржа', 'дешево', 'бесплатно',
        'обман', 'полиция', 'радар'
    ]
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание продукта'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите цену продукта'})



    def clean(self):
        cleaned_data = super().clean()
        name = (cleaned_data.get("name") or "").lower()
        description = (cleaned_data.get("description") or "").lower()

        for word in self.BANNED_WORDS:
            if word in name:
                self.add_error('name', f'Название содержит запрещенное слово "{word}"')

            if word in description:
                self.add_error('description', f'Описание содержит запрещенное слово "{word}"')

        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get('price') or 0
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")

        return price
