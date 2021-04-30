from django.shortcuts import render, redirect


def log(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    if not request.user.is_authenticated:
        return render(request, "registration/login.html")
    else:
        return redirect("/flow")
