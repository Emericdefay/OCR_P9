from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.files.storage import default_storage

from ask_review.models import Ticket
from ask_review.forms import CreateTicket
from create_review.models import Review
from create_review.forms import CreateReview


def modify(request, content, id_modify):
    """Allow user to modify their own tickets and reviews.

    Args:
        request (HttpRequest): instance of HttpRequest

    Returns:
        [render]: Render the page.
            request: HttpRequest
            template: The template needed to be show :
                        ./templates/modify/modify.html
            context: context called in template
        [redirect]: Redirect to the appropirate page.
    """
    try:
        if request.method == "GET":
            if content == "ticket":
                ticket = Ticket.objects.get(
                    Q(id=id_modify) & Q(user=request.user))

                form = CreateTicket(
                    instance=ticket,
                    initial={
                        'title': ticket.title,
                        "description": ticket.description,
                        "image": ticket.image
                    })

                return render(
                    request,
                    "modify/modify.html",
                    {"form": form, "old_image": ticket.image})

            elif content == "review":
                review = Review.objects.get(
                    Q(id=id_modify) & Q(user=request.user))

                form = CreateReview(
                    instance=review,
                    initial={
                        'headline': review.headline,
                        "rating": review.rating,
                        "body": review.body})

                return render(
                    request,
                    "modify/modify.html",
                    {"form": form, "ticket": review.ticket})

        elif request.method == "POST":
            if content == "ticket":
                form = CreateTicket(request.POST, request.FILES)

                if form.is_valid():
                    Ticket.objects.filter(
                        Q(id=id_modify) & Q(user=request.user)).update(
                            title=form.cleaned_data["title"])

                    Ticket.objects.filter(
                        Q(id=id_modify) & Q(user=request.user)).update(
                            description=form.cleaned_data["description"])

                    if request.FILES:
                        stest = request.FILES["image"]
                        simage = default_storage.save(stest.name, stest)
                    else:
                        stest = Ticket.objects.get(id=id_modify).image
                        simage = stest

                    Ticket.objects.filter(
                        Q(id=id_modify) & Q(user=request.user)).update(
                            image=simage)

                    # Optionnal
                    Review.objects.filter(ticket__id__in=Ticket.objects.filter(
                        id=id_modify).values_list("id")).delete()

                return redirect("/posts/")

            elif content == "review":
                form = CreateReview(request.POST)
                if form.is_valid():
                    Review.objects.filter(
                        Q(id=id_modify) & Q(user=request.user)).update(
                            headline=form.cleaned_data["headline"])

                    Review.objects.filter(
                        Q(id=id_modify) & Q(user=request.user)).update(
                            rating=form.cleaned_data["rating"])

                    Review.objects.filter(
                        Q(id=id_modify) & Q(user=request.user)).update(
                            body=form.cleaned_data["body"])

                return redirect("/posts/")

    except Ticket.DoesNotExist:
        return redirect("/flow/")
    except Review.DoesNotExist:
        return redirect("/flow/")
