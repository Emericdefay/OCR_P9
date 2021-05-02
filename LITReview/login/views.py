from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import PlaceholderAuthForm


def log(request):
    """Allow user to login.

    Args:
        request (HttpRequest): instance of HttpRequest

    Returns:
        [render]: Render the page.
            request: HttpRequest
            template: The template needed to be show :
                        ./templates/login/login.html
            context: context called in template
        [redirect]: Redirect to the appropirate page.
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
