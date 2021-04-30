from django.shortcuts import render, redirect

from .models import Review
from ask_review.models import Ticket

from .forms import CreateReview

# Create your views here.


def create_review(request, id_ticket=None):
    """[summary]

    Args:
        request ([type]): [description]
        id_ticket ([type]): [description]

    Returns:
        [type]: [description]
    """
    if not request.user.is_authenticated:
        return redirect("/login")
    else:
        if request.method == "POST":
            form = Review(request.POST)
            if form.is_valid:
                form.save()
                return redirect("/posts/")
            return redirect(f"/create/{id_ticket}/")
        elif request.method == "GET":
            ticket = Ticket.objects.get(id=id_ticket) or None
            form = CreateReview()
            return render(request, "create_review/create_review.html", {"form": form, "ticket": ticket})
