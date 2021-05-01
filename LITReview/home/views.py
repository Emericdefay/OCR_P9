from django.shortcuts import render, redirect


def home(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    if not request.user.is_authenticated:
        return redirect("/connect")
    else:
        return redirect("/flow")
