from django.urls import path
from dashboard import views


urlpatterns = [
    path("", views.index, name="dashboard-index"),
    path("posts/", views.posts, name="dashboard-posts"),
]

