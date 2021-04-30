from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def follow(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    return render(request, "follow/follow.html")