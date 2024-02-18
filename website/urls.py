from django.urls import path
from .views import *

urlpatterns = [
    path("", Home, name="home"),
    path("logIn", LogInForm, name="logIn"),
    path("registry",Registry,name="registry"),
    path("recover", RecoveryForm, name="recover"),

]