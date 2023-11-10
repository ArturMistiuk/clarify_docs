from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=35,
        help_text="Required. 35 characters or fewer. <br>Letters, digits and @/./+/-/_ only."
    )

    email = models.EmailField(
        help_text="Required. Enter a valid email address.",
        unique=True
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'This email address is already in use. Please provide a different email address.')
        return email
