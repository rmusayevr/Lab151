from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView

from products.models import Product, ProductCategory, Brand
from .models import *
from core.forms import *
from products.models import *
from blog.models import *
# Create your views here.

class HomePage(TemplateView):
    model = Slider
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.all()
        context['banner'] = Banner.objects.all()
        context['categories'] = ProductCategory.objects.filter(parent__isnull=True)
        context['products'] = Product.objects.order_by('-created_at').all()[:4]
        context['brands'] = Brand.objects.all()
        context['blogs'] = Blog.objects.order_by('-created_at').all()[:4]
        
        return context


class BrandView(DetailView):
    model = Brand
    template_name = "brands.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(brand=self.object)[:4]
        context['categories'] = ProductCategory.objects.filter(parent__isnull=True)
        context['brands'] = Brand.objects.all()
        context['brand'] = self.kwargs.get('pk')
        return context


class Category(TemplateView):
    template_name = "category.html"

def product_search(request):

    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            version = ProductVersion.objects.all()
            query = form.cleaned_data['query']
            product = Product.objects.filter(title__icontains=query)

            context = {
                'products' : product,
                'version' : version,
            }

            
            return render(request, 'search.html', context)
    return  HttpResponseRedirect('/')       