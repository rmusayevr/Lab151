from itertools import product
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from products.models import *
from django.urls.base import reverse_lazy

from products.serializers import ProductListSerializer

# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = "product-list.html"
    paginate_by = 16
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.order_by("-created_at").all()[:8]
        context['brands'] = Brand.objects.all()
        context['categories'] = ProductCategory.objects.filter(parent__isnull=True)
        return context



class ProductDetail(DetailView):
    template_name = "product-detail.html"
    pk_url_kwarg = 'pk'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return Product.objects.get(pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = Product.objects.get(pk = self.kwargs.get("pk"))
        context['brands'] = Brand.objects.all()
        context['categories'] = ProductCategory.objects.filter(parent__isnull=True)
        # context['related_products'] = Product.objects.filter(category__in=context['product'].category.all()).exclude(id=self.kwargs['pk'])
        return context


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category__parent', 'category', 'brand')
