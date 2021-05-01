from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class PlaceholderAuthForm(AuthenticationForm):
    """[summary]

    Args:
        AuthenticationForm ([type]): [description]
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Enter password"}))
