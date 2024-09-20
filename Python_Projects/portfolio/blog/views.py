from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog
from django.views import View



class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        return  render(request, 'blog/blog_list.html', {'blogs': blogs})

class BlogDetailView(View):
    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        return render(request, 'blog/blog_detail.html', {'blog': blog})
