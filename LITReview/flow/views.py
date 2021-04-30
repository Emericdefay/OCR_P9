from itertools import chain
from operator import attrgetter
from django.shortcuts import render

from ask_review.models import Ticket
from create_review.models import Review

def flow(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    flow_posts = list(sorted(chain(tickets, reviews), key=attrgetter("time_created"), reverse=True))
    return render(request, "flow/flow.html", context={"data": flow_posts})