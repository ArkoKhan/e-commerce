from django.urls import path
from .views import Home, LogInForm, RecoveryForm, Registry

urlpatterns = [
    path("", Home, name="home"),
    path("logIn", LogInForm, name="logIn"),
    path("recover", RecoveryForm, name="recover"),
    path("registry",Registry,name="registry")

]