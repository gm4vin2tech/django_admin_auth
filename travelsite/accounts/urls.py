from django.urls import path
from . import views  #importing views.py file


urlpatterns = [
    path("register", views.register, name="register"), #register
    path("login", views.login, name="login"), #login
    path("logout", views.logout, name="logout"), #logout
]
