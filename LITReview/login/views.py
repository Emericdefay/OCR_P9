from django.shortcuts import render, redirect
from .forms import PlaceholderAuthForm
from django.contrib.auth import authenticate, login


def log(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    if not request.user.is_authenticated:
        if request.method == "GET":
            form = PlaceholderAuthForm()
            return render(request, "login/login.html", context={"form": form})
        else:
            suser = request.POST["username"]
            spassword = request.POST["password"]
            user = authenticate(request, username=suser, password=spassword)

            if user is not None:
                login(request, user)
                return redirect("/flow")
            else:
                return redirect("/connect")

    else:
        return redirect("/flow")
