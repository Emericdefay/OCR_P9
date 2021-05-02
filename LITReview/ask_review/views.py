from django.shortcuts import render, redirect

from .forms import CreateTicket
from .models import Ticket


def ask_review(request):
    """Allow user to create a ticket.

    Args:
        request ([HttpRequest]): instance of HttpRequest

    Returns:
        [render]: Render the page.
            request: HttpRequest
            template: The template needed to be show :
                        ./templates/ask_review/ask_review.html
            context: context called in template
        [redirect]: Redirect to the appropriate page.
    """
    if not request.user.is_authenticated:
        return redirect("/login")
    else:
        if request.method == "POST":
            form = CreateTicket(request.POST or None)
            if form.is_valid():
                stitle = form.cleaned_data["title"]
                sdescription = form.cleaned_data["description"]
                # simage = form.cleaned_data["image"]
                suser = request.user
                data = Ticket(title=stitle,
                              description=sdescription,
                              user=suser)
                data.save()
                return redirect("/posts/")
            else:
                return redirect("/flow/")
        elif request.method == "GET":
            form = CreateTicket()

        return render(request, "ask_review/ask_review.html", {"form": form})
