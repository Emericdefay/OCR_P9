from django.shortcuts import render

from .models import Review

# Create your views here.
def create_review(request, id_ticket):
    if not request.user.is_authenticated:
        return redirect("/login")
    else:
        if request.method == "POST":
            form = Review(request.POST)
            if form.is_valid:
                form.save()
                return redirect("/posts/")
        elif request.method == "GET":
            form = Review(request.POST)

        return render(request, "create_review/create_review.html", {"form": form})
