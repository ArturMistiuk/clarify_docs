from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.shortcuts import render, redirect

from .forms import SignupForm, LoginForm


def signup_view(request: HttpRequest) -> HttpResponseRedirect:
    """
The signup_view function is a view that handles the signup form.
It takes in a request and returns an HTML page with the signup form.
If the user submits valid data, it creates a new user account and redirects to login.

:param request: Get the data from the form
:return: A rendered template
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
    It will display a form to the user, and if that form is valid, it will log in
    the user and redirect them to their profile page.

    :param request: Get the request data from the user
    :return: An http response object that renders the login
    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect("login")
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})