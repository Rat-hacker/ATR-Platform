from django.urls import path

from .views import index, home

urlpatterns = [
    path("", index, name="index"),
    path("welcome/", home, name="home")
]