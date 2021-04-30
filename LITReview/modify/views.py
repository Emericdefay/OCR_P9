from django.shortcuts import render, redirect
from django.db.models import Q

from ask_review.models import Ticket
from ask_review.forms import CreateTicket
from create_review.models import Review
from create_review.forms import CreateReview


def modify(request, content, id_modify):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    try:
        if request.method == "GET":
            if content == "ticket":
                ticket = Ticket.objects.get(Q(id=id_modify)&Q(user=request.user))
                form = CreateTicket(instance= ticket, initial={'title': ticket.title, "description": ticket.description})
            elif content == "review":
                review = Review.objects.get(Q(id=id_modify)&Q(user=request.user))
                form = CreateReview(instance= review, initial={'headline': review.headline, "rating": review.rating, "body": review.body})
            return render(request, "modify/modify.html", {"data": form})
        
        elif request.method == "POST":
            if content == "ticket":
                form = CreateTicket(request.POST)
                if form.is_valid():
                    Ticket.objects.filter(Q(id=id_modify)&Q(user=request.user)).update(title= request.POST["title"])
                    Ticket.objects.filter(Q(id=id_modify)&Q(user=request.user)).update(description= request.POST["description"])
                    pass    
                return redirect("/posts/")
            elif content == "review":
                form = CreateReview(request.POST)
                if form.is_valid():
                    Review.objects.filter(Q(id=id_modify)&Q(user=request.user)).update(headline= request.POST["headline"])
                    Review.objects.filter(Q(id=id_modify)&Q(user=request.user)).update(rating= request.POST["rating"])
                    Review.objects.filter(Q(id=id_modify)&Q(user=request.user)).update(body= request.POST["body"])
                    pass
                return redirect("/posts/")
    except Ticket.DoesNotExist:
        return redirect("/flow/")
    except Review.DoesNotExist:
        return redirect("/flow/")