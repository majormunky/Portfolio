from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models


def index(request):
    blog_list = models.BlogPost.objects.all().order_by("created_at")
    return render(request, "blog/index.html", {"blog_list": blog_list})


def blog_detail(request, year, month, slug):
    blog_data = models.BlogPost.objects.filter(
        slug=slug,
        created_at__year=year,
        created_at__month=month
    ).first()
    return render(request, "blog/view-blog-post.html", {"blog_data": blog_data})


@login_required
def create_blog_post(request):
    return render(request, "blog/create-blog-post.html", {})
