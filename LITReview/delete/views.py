from django.shortcuts import redirect
from django.db.models import Q

from ask_review.models import Ticket
from create_review.models import Review

def delete(request, content, id_delete):
    """Delete the content (ticket or review) identified by its id.

    Args:
        request ([HttpRequest]): instance of HttpRequest
        content (str) : "ticket" or "review"
        id_delete (int) : id of the content to delete

    Returns:
        [redirect]: Redirect to the appropriate page.
    """
    try:
        if content == "ticket":
            Ticket.objects.get(Q(id=id_delete)&Q(user=request.user)).delete()
            return redirect("/posts/")
        if content == "review":
            Review.objects.get(Q(id=id_delete)&Q(user=request.user)).delete()
            return redirect("/posts/")
    except Ticket.DoesNotExist:
        return redirect("/flow/")
    except Review.DoesNotExist:
        return redirect("/flow/")