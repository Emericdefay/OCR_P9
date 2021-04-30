from django.shortcuts import render, redirect

from ask_review.models import Ticket
from ask_review.forms import CreateTicket

from .models import Review
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
        if id_ticket:
            if request.method == "GET":
                ticket = Ticket.objects.get(id=id_ticket)
                form = CreateReview()
                return render(request, "create_review/create_review.html", {"form": form, "ticket": ticket})
            elif request.method == "POST":
                form = CreateReview(request.POST)
                if form.is_valid():
                    sticket = Ticket.objects.get(id=id_ticket)
                    sheadline = form.cleaned_data["headline"]
                    srating = form.cleaned_data["rating"]
                    sbody = form.cleaned_data["body"]
                    suser = request.user
                    data = Review(ticket=sticket,
                                  headline=sheadline,
                                  user=suser,
                                  rating=srating,
                                  body=sbody)
                    data.save()
                    return redirect("/posts/")
                else:
                    return redirect(f"/create/{id_ticket}/")
        else:
            if request.method == "GET":
                ticket = CreateTicket()
                form = CreateReview()
                return render(request, "create_review/create_review.html", {"form": form, "ticket": ticket})
            elif request.method == "POST":
                pass


"""
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
"""
