from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import SignupForm, LoginForm


def signup_view(request: HttpRequest) -> HttpResponseRedirect:
    """
The signup_view function handles the signup process for a new user.
It takes an HttpRequest object as its first argument, and returns an HttpResponseRedirect object that redirects to the login page if successful.
If unsuccessful, it renders the users/signup.html template with a SignupForm instance in its context.

:param request: HttpRequest: Pass the request to the view
:return: An httpresponseredirect object, which redirects the user to the login page
"""
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()

    return render(request, "users/signup.html", {"form": form})


def login_view(request: HttpRequest) -> HttpResponseRedirect:
    """
The login_view function is responsible for handling the login process.
It will first check if the request method is POST, and if so it will attempt to authenticate a user with the given
username and password. If authentication fails, an error message will be displayed on screen. Otherwise, we log in
the user using Django's built-in login function.

:param request: HttpRequest: Pass the request object to the view
:return: A httpresponseredirect object, which is a subclass of the httpresponse class
"""
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='login')

        login(request, user)
        return redirect(to='signup')

    return render(request, 'users/login.html', context={"form": LoginForm()})
