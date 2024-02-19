from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def Home(request):
    return render(request, "web_temp/index.html")


def LogInForm(request):
    return render(request, "web_temp/loginform.html")


def Registry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        if password == password1:
            if User.objects.filter(username=name).exists():
                messages.warning(request, "Username already exists try another one.")
            user = User.objects.create_user(username=name, email=email, password=password)
            user.set_password(password)
            user.save()
            messages.success(request, "Your account has been created successfully.")
            return redirect("logIn")
        else:
            messages.warning(request, "Fix the Problems and try again.")

    return render(request, "web_temp/registryfrom.html")


def LogOut(request):
    return redirect("logIn")


def RecoveryForm(request):
    return render(request, "web_temp/recoveryform.html")