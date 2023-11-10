from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=35,
        help_text="Required. 35 characters or fewer. <br>Letters, digits and @/./+/-/_ only.",
    )

    email = models.EmailField(
        help_text="Required. Enter a valid email address.", unique=True
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email address is already in use. Please provide a different email address."
            )
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    error_messages = {
        'invalid_login': (
            "Please enter a correct username and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': "This account is inactive."
    }
