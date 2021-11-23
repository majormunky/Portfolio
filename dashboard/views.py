from django.shortcuts import render
from django.http import JsonResponse
from blog import models as blog_models


def index(request):
    return render(request, "dashboard/index.html", {})


def posts(request):
    blog_list = blog_models.BlogPost.objects.all().order_by("created_at")
    return render(request, "dashboard/posts.html", {"blog_list": blog_list})


def create_post(request):
    if request.is_ajax() and request.method == "POST":
        title = request.POST.get("title", None)
        content = request.POST.get("content", None)
        if not all([title, content]):
            return JsonResponse({"result": "failed"})

        new_post = blog_models.BlogPost(
            title=title,
            content=content,
            user=request.user
        )
        new_post.save()
        return JsonResponse({"result": "success"})
    else:
        return render(request, "dashboard/create-post.html", {})


