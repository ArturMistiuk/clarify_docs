from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from .forms import SignupForm, LoginForm


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()

    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect("login")
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})
