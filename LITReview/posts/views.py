from django.shortcuts import render
from django.http import HttpResponse

from ask_review.models import Ticket
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
            own_tickets = own_tickets.order_by('-time_created')
            return render(request, "posts/posts.html", {"tickets": own_tickets})
    else:
        return render(request, "posts/posts.html")
