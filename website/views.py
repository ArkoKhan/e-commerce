from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, "web_temp/index.html")

def LogInForm(request):
    return render(request,"web_temp/loginform.html" )


def RecoveryForm(request):
    return render(request, "web_temp/recoveryform.html")


def Registry(request):
    return render(request, "web_temp/registryfrom.html")