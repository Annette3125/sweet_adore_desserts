from django.db import models
from django import forms
from PIL import Image
from tinymce.models import HTMLField

from my_auth.models import User


class Option(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Option"
        verbose_name_plural = "Options"

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True
    )
    options = models.ManyToManyField(Option, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = HTMLField("Description", max_length=4096, default="")
    price = models.FloatField(blank=False, null=False)
    image = models.ImageField(upload_to="products", blank=True, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name} {self.price} € {self.category.name} {self.options.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = Image.open(self.image.path)
            size = 500
            if img.height > size or img.width > size:
                output_size = (size, size)
                img.thumbnail(output_size)
                img.save(self.image.path)
        except ValueError:
            pass


class Order(models.Model):
    order_date = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    deadline = models.DateTimeField(verbose_name="Deadline", null=True, blank=True)
    options = models.ManyToManyField(
        Option,
        blank=False,
        help_text="*To select more than one Option, press CTRL and left mouse key.",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=False,
        null=True,
       )
    quantity = models.IntegerField(blank=True, null=False, default=1)


    NEW = "N"
    IN_PROGRESS = "P"
    COMPLETED = "C"
    DELIVERED = "D"
    ORDER_STATUSES = {
        NEW: "New",
        IN_PROGRESS: "In Progress",
        COMPLETED: "Completed",
        DELIVERED: "Delivered",
    }
    status = models.CharField(
        max_length=1, choices=ORDER_STATUSES, default="NEW", blank=True
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


    def __str__(self):
        return (f" Order date: {self.order_date} {self.user} {self.price} €, Return date: {self.deadline}"
                f"qty: {self.quantity} {self.product}")

    @property
    def price(self):
        if self.product:
            return self.product.price * self.quantity
        else:
            return 0

    def get_price_display(self):
        return str(self.price)


class Cocktail(models.Model):
    cocktail_name = models.CharField(max_length=200, blank=True, null=True)
    description = HTMLField("Description", max_length=4096, default="")
    recipe = HTMLField("Recipe", max_length=4096, default="")

    class Meta:
        verbose_name = "Cocktail"
        verbose_name_plural = "Cocktails"

    def __str__(self):
        return f"{self.cocktail_name}"


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery")
    image_category = models.ForeignKey(
        GalleryCategory, on_delete=models.CASCADE, related_name="images"
    )
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"({self.image_category})"


class Contact(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.address} {self.city} {self.phone} {self.email}"

