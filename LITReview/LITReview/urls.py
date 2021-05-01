"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("", include("django.contrib.auth.urls")),
    path("connect/", include("login.urls")),
    path("signin/", include("signin.urls")),
    path("flow/", include("flow.urls")),
    path("follow/", include("follow.urls")),
    path("posts/", include("posts.urls")),
    path("ask/", include("ask_review.urls")),
    path("create/", include("create_review.urls")),
    path("create/<int:id_ticket>/", include("create_review.urls")),
    path("modify/<str:content>/<int:id_modify>/", include("modify.urls")),
    path("delete/<str:content>/<int:id_delete>/", include("delete.urls")),
]
