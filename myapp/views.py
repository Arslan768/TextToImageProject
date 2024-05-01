from django.shortcuts import render
from django.http import HttpResponse


def index_templete(request):
    return render(request, "myapp/index.html")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def generate_index(request):
    return render(request, "myapp/generate.html")


def pricing_index(request):
    return render(request, "myapp/Pricing.html")


def history_index(request):
    return render(request, "myapp/History.html")


def gallery_index(request):
    return render(request, "myapp/Gallery.html")
