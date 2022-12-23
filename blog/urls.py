from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="home"),
    path("post/<slug:slug>", views.PostDetailView.as_view(), name="detail"),
    path("services", views.ServicesView.as_view(), name="services"),
]
