from django.urls import path

from . import views

urlpatterns = [
    path("", views.ask_review, name="ask_review"),
]
