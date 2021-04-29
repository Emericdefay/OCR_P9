from django.shortcuts import render

# Create your views here.
def ask_review(request):
    return render(request, "ask_review/ask_review.html")