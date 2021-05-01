from django.shortcuts import redirect


def home(request):
    """Redirect user form root to /connect or /flow

    Args:
        request ([HttpRequest]): instance of HttpRequest

    Returns:
        [redirect]: To the most appropriate page.
    """
    if not request.user.is_authenticated:
        return redirect("/connect")
    else:
        return redirect("/flow")
