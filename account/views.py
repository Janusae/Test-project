from django.contrib.auth import login, logout
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView , CreateView
from .form import RegisterForm, LoginForm, Forget_form, Reseat_pass
from .models import User
from django.utils.crypto import get_random_string
from email_service.email import Send_gmail

# Create your views here.
class RegisterView(View):
    def get(self , request):
        form = RegisterForm()
        return render(request, "account/register.html", {"form": form})
    def post(self , request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user : bool = User.objects.filter(email__exact=email).exists()
            if not user:
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                new_user = User(username=username , email=email , is_active=False , active_code_email=get_random_string(94))
                new_user.set_password(password)
                new_user.save()
                Send_gmail("Active your account", new_user.email, {"user": new_user}, 'active.html')
                return redirect(reverse("index"))
            else :
                raise Http404("Your email is exist!")
        else:
            raise Http404("Your information is not valid!")

class Active_AcountView(View):
    def get(self , request , code):
        user = User.objects.filter(active_code_email__exact=code).first()
        if user is not None:
            user.is_active = True
            user.active_email_code = get_random_string(94)
            user.save()
            return redirect(reverse("index"))
        else :
            raise Http404("We couldn't find your email")

class LoginView(View):
    def get(self , request):
        form = LoginForm()
        return render(request , "account/login.html" , {"form": form})
    def post(self , request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(email__exact=email).first()
            if user is not None:
                if user.is_active :
                    check = user.check_password(password)
                    if check:
                        login(request , user)
                        Send_gmail("Welcome Message" , user.email , {"user": user} , "welcome.html")
                        return redirect(reverse("index"))
                    else :
                        raise Http404("Your password or email is incorrect!")
                else :
                    raise Http404("Your account is not active yet!")
            else :
                raise Http404("We couldn't find your email!")
        else :
            raise Http404("Your information is not valid!")
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("index"))


class ForgetView(View):
    def get(self, request):
        form = Forget_form()
        return render(request , "account/forget.html" ,{"form":form})
    def post(self , request):
        form = Forget_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.filter(email__exact=email).first()
            if user is not None:
                user.active_code_email = get_random_string(94)
                user.save()
                Send_gmail("Change your password" , user.email , {"user":user} , "Change_pass.html")
                return redirect(reverse("index"))

class ChangeView(View):
    def get(self , request , code):
        form = Reseat_pass()
        return render(request , "account/change_pass.html" , {"form": Reseat_pass})
    def post(self , request , code):
        form = Reseat_pass(request.POST)
        if form.is_valid():
            user = User.objects.filter(active_code_email__exact=code).first()
            if user is not None:
                password = form.cleaned_data.get("password")
                user.set_password(password)
                user.active_code_email = get_random_string(94)
                user.save()
                return redirect(reverse("index"))