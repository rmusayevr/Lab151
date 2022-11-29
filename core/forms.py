from django import forms

from products.models import Product

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

    class Meta:
        model = Product
        fields = ["title" ,"category"]