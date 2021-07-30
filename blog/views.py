from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "blog/index.html", {})


@login_required
def create_blog_post(request):
    return render(request, "blog/create-blog-post.html", {})
