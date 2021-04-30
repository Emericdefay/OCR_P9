from django.shortcuts import redirect
from django.db.models import Q

from ask_review.models import Ticket
from create_review.models import Review

def delete(request, id_delete):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        Ticket.objects.get(Q(id=id_delete)&Q(user=request.user)) # .delete()
        return redirect("/posts/")
    except Ticket.DoesNotExist:
        return redirect("/flow/")