from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .forms import OrderLineForm
from .models import Option, Product, Cocktail, Category


def index(request):

    num_cakes = Option.objects.all().count
    num_cookies = Product.objects.filter(category__name="Cookies").count()
    num_cake_pops = Product.objects.filter(category__name="Cake_Pops").count()
    num_cocktails_recipes = Cocktail.objects.all().count
    context = {"num_cakes": num_cakes,
               "num_cookies": num_cookies,
               "num_cake_pops": num_cake_pops,
               "num_cocktails_recipes": num_cocktails_recipes,
               }

    return render(request, "desserts/index.html", context=context)


def cakes(request):
    return render(request, "dessert/cakes.html")
