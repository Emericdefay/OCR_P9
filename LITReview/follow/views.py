from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q

from .models import UserFollows
from .forms import FollowSomeone


def follow(request):
    """ Allow to follow users.

    Args:
        request (HttpRequest): instance of HttpRequest

    Returns:
        [render]: Render the page.
            request: HttpRequest
            template: The template needed to be show :
                        ./templates/follow/follow.html
            context: context called in template
        [redirect]: Redirect to the appropriate page.
    """
    if request.user.is_authenticated:
        if request.method == "GET":
            follow_an_user = FollowSomeone()
            users_followed = UserFollows.objects.filter(user=request.user)
            followed_by = UserFollows.objects.filter(
                            followed_user=request.user)
            return render(
                        request,
                        "follow/follow.html",
                        {"follow_an_user": follow_an_user,
                         "users_followed": users_followed,
                         "followed_by": followed_by})

        if request.method == "POST":
            form = FollowSomeone(request.POST)
            different_user = form.cleaned_data["user"] != request.user.username
            if form.is_valid() and different_user:
                try:
                    user_followed = User.objects.get(
                                        username=form.cleaned_data["user"])
                    data = UserFollows(
                                user=request.user,
                                followed_user=user_followed)
                    data.save()
                    return redirect("/flow/")
                except Exception:
                    return redirect("/follow/")
            else:
                return redirect("/posts/")
    else:
        return redirect("/connect/")


def delete(request, id_delete):
    """ Allow user to unfollow someone.

    Args:
        request (HttpRequest): instance of HttpRequest
        id_delete (int): id of the user unfollowed

    Returns:
        [redirect]: Redirect to the appropriate page.
    """
    try:
        UserFollows.objects.get(
            Q(id=id_delete) & Q(user=request.user)).delete()
        return redirect("/follow/")
    except UserFollows.DoesNotExist:
        return redirect("/follow/")
