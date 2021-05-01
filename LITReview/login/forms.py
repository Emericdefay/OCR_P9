from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class PlaceholderAuthForm(AuthenticationForm):
    """Surcharge AuthentificationForm with placeholders.

    Args:
        AuthenticationForm ([class]): Base class for authentificating users.
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Nom d'utilisateur"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Mot de passe"}))
