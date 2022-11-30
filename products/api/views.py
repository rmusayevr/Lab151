from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from products.models import Product
from .serializers import ProductListSerializer


class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category__parent', 'category', 'brand')
