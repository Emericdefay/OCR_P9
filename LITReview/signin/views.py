from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreationForm, DivErrorList

# Create your views here.


def signin(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    if request.user.is_authenticated:
        return redirect("/flow")
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect("/connect/")
        elif request.method == "GET":
            form = UserCreationForm(request.POST, error_class=DivErrorList)

        return render(request, "signin/signin.html", {"form": form})
