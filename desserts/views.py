from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import FormView, FormMixin
from django.urls import reverse

from .forms import OrderForm, ProductRatingForm
from .models import Option, Product, Cocktail, Order, GalleryCategory, GalleryImage, ProductRating, Contact


def index(request):

    num_cakes = Option.objects.all().count
    num_cookies = Product.objects.filter(category__name="Cookies").count()
    num_cake_pops = Product.objects.filter(category__name="Cake Pops").count()
    num_cocktails_recipes = Cocktail.objects.all().count

    homepage_category = GalleryCategory.objects.filter(name="Homepage").first()

    gallery_images = GalleryImage.objects.filter(image_category=homepage_category) if homepage_category else []

    context = {"num_cakes": num_cakes,
               "num_cookies": num_cookies,
               "num_cake_pops": num_cake_pops,
               "num_cocktails_recipes": num_cocktails_recipes,
               "gallery_images": gallery_images
               }

    return render(request, "desserts/index.html", context=context)

@login_required
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse("create_order"))
    else:
        form = OrderForm()
    context = {"form": form, "action_url": reverse("create_order")}

    return render(request, "desserts/generic_form.html", context)


class CakesOptionListView(generic.ListView):
    template_name = "desserts/cakes_option.html"
    model = Option
    context_object_name = "options"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # We get all the photos in the gallery that belong to the "Cakes" category
        cake_category = GalleryCategory.objects.filter(name="Cakes").first()
        if cake_category:
            context["gallery_images"] = GalleryImage.objects.filter(image_category=cake_category)
        else:
            context["gallery_images"] = []
        return context



class CakeListView(generic.DetailView):
    template_name = "desserts/cakes.html"
    model = Option
    context_object_name = "cakes"

    def get_context_data(self, **kwargs):
        option = self.get_object()
        cakes = Product.objects.filter(options__name=option.name)
        return {
            "cakes": cakes,
        }


class CakeDetailView(generic.edit.FormMixin, generic.DetailView):
    template_name = "desserts/cake_details.html"
    model = Product
    context_object_name = "cake"
    form_class = ProductRatingForm


    def get_success_url(self):
        return reverse('cake_details', kwargs={'pk': self.object.id})

    # Standard post method override using FormMixin, can be copied directly
    # to our project.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # Specify that the order will be the one after which we comment,
    # and the user will be the one who is logged in.
    def form_valid(self, form):
        form.instance.product = self.object
        form.instance.author = self.request.user
        form.save()
        return super(CakeDetailView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["image_url"] = self.object.image.url if self.object.image else None
        context["ratings"] = self.object.ratings.all()
        context["average_rating"] = self.object.average_rating
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["image_url"] = self.object.image.url if self.object.image else None
        return context


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


class OrdersListView(LoginRequiredMixin, generic.ListView):
    template_name = "desserts/orders.html"
    paginate_by = 4
    model = Order
    context_object_name = "orders"
    ordering = ["id"]


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "desserts/order_details.html"
    context_object_name = "order"



def rating_view(request):
    obj = ProductRating.objects.filter(score=0).order_by("?").first()
    context ={
        'object': obj
    }
    return render(request, "desserts/ratings.html", context)


def rate_product(request, product_id):
    if request.method == 'POST':
        val = request.POST.get("score")
        text = request.POST.get("text")
        product = Product.objects.get(id=product_id)

        # Sukuriamas naujas įvertinimas
        rating = ProductRating.objects.create(
            product=product,
            score=val,
            author=request.user,
            text=text
        )
        rating.save()

        # Grąžinamas puslapis su atnaujintu įvertinimu
        return redirect('cake_details', pk=product.id)
    return JsonResponse({'success':'false'})





def contacts(request):
    contact = Contact.objects.first()
    return render(request, "desserts/contacts.html", {"contact": contact})