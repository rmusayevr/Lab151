from django.urls import path
from blog.views import *

urlpatterns = [
    path('blog/', Blogs.as_view(), name='blog'),
    # path('blog-detail/<int:id>/', blog_detail, name='blog-detail')
]