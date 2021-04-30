from django.shortcuts import render

def modify(request, user, id_modify):
    """[summary]

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    return render(request, "modify/modify.html")