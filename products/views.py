from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from products.models import *

class ProductList(ListView):
    model = Product
    template_name = "product-list.html"
    paginate_by = 16
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.order_by("-created_at").all()[:16]
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
