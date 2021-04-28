from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def flow(request):
    return render(request, "flow/flow.html")