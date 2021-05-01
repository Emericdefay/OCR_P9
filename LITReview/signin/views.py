from django.shortcuts import render, redirect

from .forms import UserCreationForm, DivErrorList

# Create your views here.


def signin(request):
    """ Allow to sign-in the website.

    Args:
        request (HttpRequest): instance of HttpRequest

    Returns:
        [render]: Render the page.
            request: HttpRequest
            template: The template needed to be show : ./templates/signin/signin.html
            context: context called in template
    """
    if request.user.is_authenticated:
        return redirect("/flow")
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect("/connect/")
            else:
                # form is not valid.
                return redirect("/signin/")
        elif request.method == "GET":
            form = UserCreationForm(request.POST, error_class=DivErrorList)

        return render(request, "signin/signin.html", {"form": form})
