from django.urls import path
from .views import Home, LogInForm, Registry, RecoveryForm, LogOut, All_product, Contact

urlpatterns = [
    path("", Home, name="home"),
    path("logIn", LogInForm, name="logIn"),
    path("registry",Registry,name="registry"),
    path("recover", RecoveryForm, name="recover"),
    path("logOut", LogOut, name="logOut"),
    path("all_product", All_product, name="all_product"),
    path("contact", Contact, name="contact"),

]