from django.shortcuts import render


def index(request):
    return render(request, "home/index.html", {})


def project(request, slug):
    template_name = "home/{}.html".format(slug)
    return render(request, template_name, {})
