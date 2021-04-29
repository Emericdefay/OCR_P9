from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from django.forms.utils import ErrorList

class UserCreationForm(UserCreationForm):
    username = forms.CharField(label="Enter your username", widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(label="Enter your password", widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"})) 
    password2 = forms.CharField(label="Confirm your password", widget=forms.PasswordInput(attrs={"placeholder": "Confirm your password"})) 
    
    username.initial = "Enter your username"
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        
        help_texts = {
            "username": None,
            "password1": None,
            "password2": None,
        }

class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ""
        return '<div class="errorlist"></div>'