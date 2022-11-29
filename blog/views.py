from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from blog.models import Blog, BlogBanner
from django.shortcuts import redirect, render, get_object_or_404

# Create your views here.

class Blogs(ListView):
    model = Blog
    template_name = "blog.html"
    paginate_by = 4
    context_object_name = "blog"

    def get_queryset(self):
        return Blog.objects.order_by('-created_at').all()

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['banner'] = BlogBanner.objects.all() 
       return context
    

# def blog_detail(request, id):
#     blog = Blog.objects.get(id=id)

#     context = {
#         "blog" : blog
#     }
#     return render(request, "blog-detail.html", context)

    