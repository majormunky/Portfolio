from django.shortcuts import render
from blog import models as blog_models


def index(request):
    return render(request, "dashboard/index.html", {})


def posts(request):
    blog_list = blog_models.BlogPost.objects.all().order_by("created_at")
    return render(request, "dashboard/posts.html", {"blog_list": blog_list})

