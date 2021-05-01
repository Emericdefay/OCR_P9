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
        [render]: [description]
            request: 
            template:
            context:
                data:
                range:
    """
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    users = UserFollows.objects.all()
    # Tickets
    # 1. Get all tickets from user
    # 2. Get all tickets from followed_user-s
    intersection_tickets = (
    tickets.filter(user=request.user) |
    tickets.filter(user__id__in=users.filter(user=request.user).values_list("followed_user_id"))
    )
    # Reviews
    # 1. Get all reviews from user
    # 2. Get all reviews from followed_user-s
    # 3. Get reviews from un-followed_user-s that review the user's ticket
    intersection_reviews = (
    reviews.filter(user=request.user) |
    reviews.filter(user__id__in=users.filter(user=request.user).values_list("followed_user_id")) |
    reviews.filter(ticket__id__in=tickets.filter(user=request.user).values_list("id"))
    )

    flow_posts = list(sorted(chain(intersection_tickets, intersection_reviews),
                      key=attrgetter("time_created"), reverse=True))
    return render(request, "flow/flow.html", context={"data": flow_posts, "range_5": range(5)})
