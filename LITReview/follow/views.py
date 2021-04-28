from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def follow(request):
    return render(request, "follow/follow.html")