from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import UserFollows
from .forms import FollowSomeone
# Create your views here.

def follow(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    if request.method == "GET":
        follow_an_user = FollowSomeone()
        users_followed = UserFollows.objects.filter(user=request.user)
        followed_by = UserFollows.objects.filter(followed_user=request.user)
        return render(request, "follow/follow.html", {"follow_an_user": follow_an_user, "users_followed": users_followed, "followed_by": followed_by})

    if request.method == "POST":
        form = FollowSomeone(request.POST)
        if form.is_valid() and form.cleaned_data["user"]!= request.user.username:
            try:
                user_followed = User.objects.get(username=form.cleaned_data["user"])
                data = UserFollows(user=request.user, followed_user=user_followed)
                data.save()
                return redirect("/flow/")
            except Exception:
                return redirect("/follow/")
        else:
            return redirect("/posts/")