from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    context = { 'posts': Post.objects.all() }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog_detail(request):
    
    return render(request, 'blog/blog_detail.html')

