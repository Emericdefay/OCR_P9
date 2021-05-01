from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from django.forms.utils import ErrorList


class UserCreationForm(UserCreationForm):
    """Surcharge the class UserCreationForm to put place holder
    and remove help_text.

    Args:
        UserCreationForm ([class]): A form that create a user
    """
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': "Nom d'utilisateur"}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Mot de passe"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={"placeholder": "Confirmez votre mot de passe"}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

        help_texts = {
            "username": None,
            "password1": None,
            "password2": None,
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['style'] = "width:40%; height: 100%;"
        self.fields['password1'].widget.attrs['style'] = "width:40%; height: 100%;"
        self.fields['password2'].widget.attrs['style'] = "width:40%; height: 100%;"


class DivErrorList(ErrorList):
    """Surcharge the errorlist.

    Args:
        ErrorList ([class]): collection of errors.
    """

    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ""
        return '<div class="errorlist"></div>'
