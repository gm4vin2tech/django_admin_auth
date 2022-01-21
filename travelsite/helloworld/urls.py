from django.urls import path
from . import views  #importing views.py file


urlpatterns = [
    path("", views.homepage, name="home"), #homepage
    path("features", views.features, name="features"), #homepage

]
