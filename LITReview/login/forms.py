from django import forms
from django.contrib.auth.forms import AuthenticationForm


class PlaceholderAuthForm(AuthenticationForm):
    """Surcharge AuthentificationForm with placeholders.

    Args:
        AuthenticationForm ([class]): Base class for authentificating users.
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': "Nom d'utilisateur"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Mot de passe"}))

    def __init__(self, *args, **kwargs):
        super(PlaceholderAuthForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["style"] = "width: 80%;"
        self.fields["password"].widget.attrs["style"] = "width: 80%;"
