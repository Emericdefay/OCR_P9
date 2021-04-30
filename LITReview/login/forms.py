from django.contrib.auth.forms import AuthenticationForm, forms


class PlaceholderAuthForm(AuthenticationForm):
    """[summary]

    Args:
        AuthenticationForm ([type]): [description]
    """
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Enter your password"}))
