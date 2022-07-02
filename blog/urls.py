from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="home"),
    path("create/", views.PostCreateView.as_view(), name="create"),
    path("delete/<slug:slug>", views.PostDeleteView.as_view(), name="delete"),
    path("update/<slug:slug>", views.PostUpdateView.as_view(), name="update"),
    path("post/<slug:slug>", views.PostDetailView.as_view(), name="detail"),

]