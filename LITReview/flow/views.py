from itertools import chain
from operator import attrgetter
from django.shortcuts import render

from ask_review.models import Ticket
from create_review.models import Review
from follow.models import UserFollows


def flow(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    
    intersection_tickets = tickets.filter(
        user=request.user) | tickets.filter(
        user__id__in=UserFollows.objects.filter(
        user=request.user).values_list("followed_user_id"))

    intersection_reviews = reviews.filter(
        user=request.user) | reviews.filter(
        user__id__in=UserFollows.objects.filter(
        user=request.user).values_list("followed_user_id")) | reviews.filter(
        ticket__id__in=Ticket.objects.filter(
        user=request.user).values_list("id"))

    flow_posts = list(sorted(chain(intersection_tickets, intersection_reviews),
                      key=attrgetter("time_created"), reverse=True))
    return render(request, "flow/flow.html", context={"data": flow_posts, "range": range(5)})
