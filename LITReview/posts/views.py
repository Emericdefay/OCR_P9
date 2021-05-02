from operator import attrgetter
from itertools import chain

from django.shortcuts import render

from ask_review.models import Ticket
from create_review.models import Review


def post(request):
    """ Allow to see the user's posts.

    Args:
        request (HttpRequest): instance of HttpRequest

    Returns:
        [render]: Render the page
            request: HttpRequest
            template: The template needed to be show :
                        ./templates/posts/posts.html
    """
    if request.user.is_authenticated:
        if request.method == "GET":
            own_tickets = Ticket.objects.filter(user=request.user)
            own_reviews = Review.objects.filter(user=request.user)
            own_data = sorted(
                            chain(own_tickets, own_reviews),
                            key=attrgetter("time_created"),
                            reverse=True)
            return render(
                        request,
                        "posts/posts.html",
                        {"data": own_data, "range": range(5)})
    else:
        return render(request, "posts/posts.html")
