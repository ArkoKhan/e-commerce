from django.urls import path
from .views import Home, LogInForm, Registry, RecoveryForm

urlpatterns = [
    path("", Home, name="home"),
    path("logIn", LogInForm, name="logIn"),
    path("registry",Registry,name="registry"),
    path("recover", RecoveryForm, name="recover"),

]