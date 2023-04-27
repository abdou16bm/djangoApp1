from django import forms
from .models import Product

class producAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','price','stock_qt']
        labels = {'name':'nom produit','category':'categorie','price':'prix','stock_qt':'quantité'}
