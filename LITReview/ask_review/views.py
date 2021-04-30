from django.shortcuts import render, redirect

from .forms import CreateTicket
from .models import Ticket


# Create your views here.
def ask_review(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    if not request.user.is_authenticated:
        return redirect("/login")
    else:
        if request.method == "POST":
            form = CreateTicket(request.POST or None)
            if form.is_valid():
                stitle = form.cleaned_data["title"]
                sdescription = form.cleaned_data["description"]
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
