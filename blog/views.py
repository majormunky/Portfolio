from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models


def index(request):
    blog_list = models.BlogPost.objects.all().order_by("created_at")
    return render(request, "blog/index.html", {"blog_list": blog_list})


def blog_detail(request, year, month, slug):
    pass


@login_required
def create_blog_post(request):
    return render(request, "blog/create-blog-post.html", {})
