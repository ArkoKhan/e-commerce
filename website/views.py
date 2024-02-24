from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Profile
from django.conf import settings
import random

# Create your views here.



def Home(request):
    return render(request, "web_temp/index.html")


def LogInForm(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = auth.authenticate(username=name, password=password)
        if user:
            if user.is_superuser:
                login(request, user)
                return redirect("all_product")
            else:
                prof = Profile.objects.get(user=user)
                if prof.is_verified == True:
                    if user.is_active and user.is_staff:
                        login(request, user)
                        return redirect("all_product")
                    elif user.is_active:
                        login(request, user)
                        return redirect("home")
                else:
                    messages.warning(request, "User is not verified.")
                    return redirect("login")
        else:
            messages.warning(request, "User not found.")
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
            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.set_password(password)
                user.save()
                otp = random.randint(1000, 9999)
                prof = Profile(user=user, token=otp)
                prof.save()
                subject = "Account varification OTP"
                message = f"Your OTP is {otp}"
                from_email = settings.EMAIL_HOST_USER
                recipent = [email]
                send_mail(subject, message, from_email, recipent)
                messages.success(request, "An OTP has been sent to your email.")
                return redirect("otp")
        else:
            messages.warning(request, "Fix the Problems and try again.")

    return render(request, "web_temp/registryfrom.html")


def Verify_otp(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        try:
            prof=  Profile.objects.get(token=otp)
            prof.is_verified = True
            prof.save()
            messages.success(request, "Your Profile is Created and verified successfully.")
            return redirect("logIn")
        except:
            messages.success(request, "Wrong OTP.")
            return redirect("otp")
    return render(request, "web_temp/otp.html")


def LogOut(request):
    logout(request)
    messages.warning(request, "User Logged out.")
    return redirect("logIn")


def RecoveryForm(request):
    return render(request, "web_temp/recoveryform.html")


@login_required(login_url="logIn")
def All_product(request):
    return render(request, "web_temp/all_product.html")

def Contact(request):
    if not request.user.is_authenticated:
        messages.success(request, "Please log in first.")
        return redirect("logIn")
    return render(request, "web_temp/contact.html")