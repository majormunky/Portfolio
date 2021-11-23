from django.shortcuts import render


def index(request):
    return render(request, "dashboard/index.html", {})


def posts(request):
    return render(request, "dashboard/posts.html", {})

