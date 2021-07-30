from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="blog-index"),
    path("create/", views.create_blog_post, name="blog-create-post"),
]
