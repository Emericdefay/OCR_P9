from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def log(request):
    if not request.user.is_authenticated: 
        return render(request, "registration/login.html")
    else:
        return redirect("/flow")
    