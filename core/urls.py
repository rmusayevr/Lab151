from django.urls import path
from core.views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('filter/', Filter.as_view(), name='filter'),
    path('search/', product_search, name='search'),
    path('brand/<int:pk>/', BrandView.as_view(), name='brand'),   
    path('category/<int:pk>/', CategoryView.as_view(), name='category')
]