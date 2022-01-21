from django.urls import path
from . import views  #importing views.py file


urlpatterns = [
    path("", views.homepage, name="home"), #homepage
]
