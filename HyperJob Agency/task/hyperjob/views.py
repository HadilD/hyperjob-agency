from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class MainView(View):
    def get(self, request):
        return render(request, 'hyperjob/main.html')


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "hyperjob/login.html"


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'hyperjob/signup.html'


def profile(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    elif request.user.is_authenticated:
        return render(
            request,
            'hyperjob/profile.html',
            context={"user": request.user})
