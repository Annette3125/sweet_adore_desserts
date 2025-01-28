from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"cakes": cakes}
    return render(request, "desserts/index.html", context=context)


def cakes(request):
    return render(request, "dessert/cakes.html")
