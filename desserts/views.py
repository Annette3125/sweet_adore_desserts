from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
from django.views.generic.edit import FormView
from django.urls import reverse,reverse_lazy
from .forms import OrderLineForm, OrderForm
from .models import Option, Product, Cocktail, Order


def index(request):

    num_cakes = Option.objects.all().count
    num_cookies = Product.objects.filter(category__name="Cookies").count()
    num_cake_pops = Product.objects.filter(category__name="Cake Pops").count()
    num_cocktails_recipes = Cocktail.objects.all().count
    context = {"num_cakes": num_cakes,
               "num_cookies": num_cookies,
               "num_cake_pops": num_cake_pops,
               "num_cocktails_recipes": num_cocktails_recipes,
               }

    return render(request, "desserts/index.html", context=context)


def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("create_order"))
    else:
        form = OrderForm()
    context = {"form": form, "action_url": reverse("create_order")}

    return render(request, "desserts/generic_form.html", context)


def create_order_line(request):
    if request.method == "POST":
        form = OrderLineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("create_order_line"))
    else:
        form = OrderLineForm()
    context = {"form": form, "action_url": reverse("create_order_line")}

    return render(request, "desserts/generic_form.html", context)




def cakes(request):
    cakes_ = Option.objects.all()
    return render(request, "desserts/cakes.html", {"cakes": cakes_})


def cake_details(request, pk):
    cake_ = get_object_or_404(Option, pk=pk)
    return render(request, "desserts/cake_details.html", {"cake": cake_})


class CookiesListView(generic.ListView):
    template_name = "desserts/cookies.html"
    model = Product
    context_object_name = "cookies"

    def get_queryset(self):
        return Product.objects.filter(category__name="Cookies")

class CookiesDetailView(generic.DetailView):
    template_name = "desserts/cookies_details.html"
    model = Product
    context_object_name = "cookies"


class CakePopsListView(generic.ListView):
    template_name = "desserts/cake_pops.html"
    model = Product
    context_object_name = "cake_pops"

    def get_queryset(self):
        return Product.objects.filter(category__name="Cake Pops")

class CakePopsDetailView(generic.DetailView):
    template_name = "desserts/cake_pops_details.html"
    model = Product
    context_object_name = "cake_pops"


class OrdersListView(generic.ListView):
    template_name = "desserts/orders.html"
    paginate_by = 4
    model = Order
    context_object_name = "orders"
    ordering = ["id"]


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "desserts/order_details.html"
    context_object_name = "order"






