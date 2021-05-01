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
    # Get objects:
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    users = UserFollows.objects.all()

    # Tickets (t)
    # 1. Get all tickets from user
    t_from_user = tickets.filter(user=request.user)
    # 2. Get all tickets from followed_user-s
    t_from_followed_user = tickets.filter(user__id__in=users.filter(user=request.user).values_list("followed_user_id"))
    # Union :
    union_tickets = t_from_user | t_from_followed_user

    # Reviews (r)
    # 1. Get all reviews from user
    r_from_user = reviews.filter(user=request.user)
    # 2. Get all reviews from followed_user-s
    r_from_followed_user = reviews.filter(user__id__in=users.filter(user=request.user).values_list("followed_user_id"))
    # 3. Get reviews from un-followed_user-s that review the user's ticket
    r_from_unfollowed_reviewed = reviews.filter(ticket__id__in=tickets.filter(user=request.user).values_list("id"))
    # Union :
    union_reviews = (r_from_user | r_from_followed_user | r_from_unfollowed_reviewed)

    # Sort all posts by -time_created:
    flow_posts = list(sorted(chain(union_tickets, union_reviews),
                      key=attrgetter("time_created"), reverse=True))
    return render(request, "flow/flow.html", context={"data": flow_posts, "range_5": range(5)})
