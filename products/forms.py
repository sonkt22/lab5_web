from django import forms
from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description', 'price','brand', 'picture', ]

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description', 'price', 'brand', 'picture']


