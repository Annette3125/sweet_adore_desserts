import os
from io import BytesIO

import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.db.models import Avg
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .forms import OrderForm, ProductRatingForm
from .models import (Cocktail, Contact, GalleryCategory, GalleryImage, Option,
                     Order, Product, ProductRating)


def index(request):

    num_cakes = Option.objects.all().count
    num_cookies = Product.objects.filter(category__name="Cookies").count()
    num_cake_pops = Product.objects.filter(category__name="Cake Pops").count()
    num_cocktails_recipes = Cocktail.objects.all().count

    homepage_category = GalleryCategory.objects.filter(name="Homepage").first()

    gallery_images = (
        GalleryImage.objects.filter(image_category=homepage_category)
        if homepage_category
        else []
    )

    context = {
        "num_cakes": num_cakes,
        "num_cookies": num_cookies,
        "num_cake_pops": num_cake_pops,
        "num_cocktails_recipes": num_cocktails_recipes,
        "gallery_images": gallery_images,
    }

    return render(request, "desserts/index.html", context=context)


def send_invoice_email(order):
    pdf_buffer = generate_invoice(order)

    # create email
    email = EmailMessage(
        subject=f"Your Order Invoice - {order.id}",
        body=f"Dear {order.user.username},\n\nPlease find your invoice attached.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[order.user.email],
    )

    # add an attachment and send an email
    email.attach(f"invoice_{order.id}.pdf", pdf_buffer.read(), "application/pdf")
    email.send()


@login_required
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            form.save_m2m()

            # after created order send invoice by email
            send_invoice_email(order)

            return HttpResponseRedirect(reverse("create_order"))
    else:
        form = OrderForm()
    context = {"form": form, "action_url": reverse("create_order")}

    return render(request, "desserts/generic_form.html", context)


def generate_invoice(order):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.drawString(100, 750, f"Order Invoice - {order.id}")
    c.drawString(100, 730, f"User: {order.user.username}")
    c.drawString(100, 710, f"Order Date: {order.order_date}")
    c.drawString(100, 690, f"Order Deadline: {order.deadline}")
    c.drawString(100, 670, f"Product: {order.product.name}")
    c.drawString(100, 650, f"Quantity: {order.quantity}")
    c.drawString(100, 630, f"Price: {order.price} EUR")
    c.drawString(100, 610, "Bank Name: XYZ Bank")
    c.drawString(100, 590, "Account Number: 1234567890")
    c.drawString(100, 570, "IBAN: LT123456789012345678")
    c.drawString(100, 550, "SWIFT/BIC: XYZBLT22")
    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer


class CakesOptionListView(generic.ListView):
    template_name = "desserts/cakes_option.html"
    model = Option
    context_object_name = "options"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # We get all the photos in the gallery that belong to the "Cakes" category
        cake_category = GalleryCategory.objects.filter(name="Cakes").first()
        if cake_category:
            context["gallery_images"] = GalleryImage.objects.filter(
                image_category=cake_category
            )
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
        return reverse("cake_details", kwargs={"pk": self.object.id})

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
        context["form"] = ProductRatingForm()
        context["image_url"] = self.object.image.url if self.object.image else None
        context["ratings"] = self.object.ratings.all()
        context["average_rating"] = (
            self.object.ratings.aggregate(Avg("score"))["score__avg"] or 0
        )
        return context


class CookiesListView(generic.ListView):
    template_name = "desserts/cookies.html"
    model = Product
    context_object_name = "cookies"

    def get_queryset(self):
        return Product.objects.filter(category__name="Cookies")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cookies_category = GalleryCategory.objects.filter(name="Cookies").first()
        if cookies_category:
            context["gallery_images"] = GalleryImage.objects.filter(
                image_category=cookies_category
            )
        else:
            context["gallery_images"] = []
        return context


class CookiesDetailView(generic.DetailView):
    template_name = "desserts/cookies_details.html"
    model = Product
    context_object_name = "cookies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProductRatingForm()
        context["image_url"] = self.object.image.url if self.object.image else None
        context["average_rating"] = (
            self.object.ratings.aggregate(Avg("score"))["score__avg"] or 0
        )
        return context


class CakePopsListView(generic.ListView):
    template_name = "desserts/cake_pops.html"
    model = Product
    context_object_name = "cake_pops"

    def get_queryset(self):
        return Product.objects.filter(category__name="Cake Pops")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cake_pops_category = GalleryCategory.objects.filter(name="Cake Pops").first()
        if cake_pops_category:
            context["gallery_images"] = GalleryImage.objects.filter(
                image_category=cake_pops_category
            )
        else:
            context["gallery_images"] = []
        return context


class CakePopsDetailView(generic.DetailView):
    template_name = "desserts/cake_pops_details.html"
    model = Product
    context_object_name = "cake_pops"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProductRatingForm()
        context["image_url"] = self.object.image.url if self.object.image else None
        context["average_rating"] = (
            self.object.ratings.aggregate(Avg("score"))["score__avg"] or 0
        )
        return context


class OrdersListView(LoginRequiredMixin, generic.ListView):
    template_name = "desserts/orders.html"
    paginate_by = 4
    model = Order
    context_object_name = "orders"
    ordering = ["id"]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("id")


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "desserts/order_details.html"
    context_object_name = "order"


def rate_product(request, product_id):
    if request.method == "POST":
        val = request.POST.get("score")
        text = request.POST.get("text")
        product = Product.objects.get(id=product_id)

        # new rating - assessment created
        rating = ProductRating.objects.create(
            product=product, score=val, author=request.user, text=text
        )
        rating.save()

        # Returns page with updated rating
        return redirect("cake_details", pk=product.id)
    return JsonResponse({"success": "false"})


def contacts(request):
    contact = Contact.objects.first()
    return render(request, "desserts/contacts.html", {"contact": contact})


def privacy_policy(request):
    return render(request, "desserts/privacy_policy.html")


def dessert_images(request):
    url = "https://api.unsplash.com/search/photos"
    access_key = os.getenv("UNSPLASH_API_KEY")

    search_query = "cake"

    response = requests.get(
        url, params={"client_id": access_key, "query": search_query, "per_page": 10}
    )

    if response.status_code == 200:
        images = response.json()["results"]
    else:
        images = []

    return render(request, "desserts/dessert_images.html", {"images": images})
