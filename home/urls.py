from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home-index"),
    path("project/<str:slug>/", views.project, name="home-project"),
]
