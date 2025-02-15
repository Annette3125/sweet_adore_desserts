from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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


def create_order(request):
    if request.method == "POST":
        form = OrderLineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("create_order"))
    else:
        form = OrderLineForm()
    context = {"form": form, "action_url": reverse("create_order")}

    return render(request, "desserts/generic_form.html", context)


def cakes(request):
    cakes_ = Option.objects.all()
    return render(request, "desserts/cakes.html", {"cakes": cakes_})


def cake_details(request, pk):
    cake_ = get_object_or_404(Option, pk=pk)
    return render(request, "desserts/cake_details.html", {"cake": cake_})
