from operator import attrgetter
from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse

from ask_review.models import Ticket
from create_review.models import Review
# Create your views here.


def post(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    if request.user.is_authenticated:
        if request.method == "GET":
            own_tickets = Ticket.objects.filter(user=request.user)
            own_reviews = Review.objects.filter(user=request.user)
            own_data = sorted(chain(own_tickets, own_reviews), key=attrgetter("time_created"), reverse=True)
            return render(request, "posts/posts.html", {"data": own_data})
    else:
        return render(request, "posts/posts.html")
