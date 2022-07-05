from re import template
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse_lazy
from blog.models import Post

# Create your views here.


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    paginate_by: int = 6

    def get_queryset(self):
        return super().get_queryset().filter(status="published")



class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = "__all__"
    login_url = reverse_lazy("blog:home")
    success_url = reverse_lazy("blog:home")


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:home")


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:home")


class AboutView(View):
    def get(self, request):
        return render(request, "blog/about.html")


class ContactView(View):
    def get(self, request):
        return render(request, "blog/contact.html")
