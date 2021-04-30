from django.shortcuts import render

# Create your views here.

def flow(request):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    return render(request, "flow/flow.html")