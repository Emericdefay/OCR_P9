from django.urls import path

from . import views

urlpatterns = [
    path("", views.delete, name="delete")
]
