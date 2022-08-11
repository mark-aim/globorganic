from django.http import *
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from authentication.forms import CostumUserLoginForm, UserRegistrationForm

# Create your views here.

def login_view(request):
    context = { }
    if request.POST:
        form = CostumUserLoginForm(request.POST);
        if form.is_valid():
            username = request.POST['username'];
            password = request.POST['password'];
            user = authenticate(request , username = username, password = password);

            if user is not None:
                login(request, user);
                return redirect('home');
        context['login_form'] = form;
    else:
        form = CostumUserLoginForm();
        context['login_form'] = form;
    return render(request, 'authentication/login.html', context);

def register(request):
    context = { }
    if request.POST:
        form = UserRegistrationForm(request.POST);
        if form.is_valid():
            form.save();
            return redirect('home');
        context['register_form'] = form;
    else:
        form = UserRegistrationForm();
        context['register_form'] = form;
    return render(request, 'authentication/register.html', context);

def logout_view(request):
    logout(request)
    return redirect('logout');
