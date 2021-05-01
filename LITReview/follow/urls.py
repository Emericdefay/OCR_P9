from django.urls import path

from . import views

urlpatterns = [
    path("", views.follow, name="follow"),
    path("delete/<int:id_delete>/", views.delete, name="delete"),
    
]