from django.shortcuts import redirect
from django.db.models import Q

from ask_review.models import Ticket
from create_review.models import Review

def delete(request, content, id_delete):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
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