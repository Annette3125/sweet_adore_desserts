from django.db import models
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
    name = models.CharField(max_length=200, blank=True, null=True)
    description = HTMLField("Description", max_length=4096, default="")
    price = models.FloatField(blank=False, null=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name} {self.price} {self.category}"


class Order(models.Model):
    order_date = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    total_price = models.FloatField(blank=True, null=True, default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    deadline = models.DateTimeField(verbose_name="Deadline", null=True, blank=True)

    NEW = "N"
    IN_PROGRESS = "P"
    COMPLETED = "C"
    DELIVERED = "D"
    ORDER_STATUSES = {
        NEW: "New",
        IN_PROGRESS: "In Progress",
        COMPLETED: "Completed",
        DELIVERED: "Delivered"
    }
    status = models.CharField(
        max_length=1, choices=ORDER_STATUSES, default="NEW", blank=True
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f" {self.order_date} {self.user}"

class OrderLine(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, blank=True, null=True
    )
    options = models.ManyToManyField(
        Option, blank=False)
    product = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True
    )
    quantity = models.IntegerField(blank=True, null=False, default=1)

    class Meta:
        verbose_name = "Order Line"
        verbose_name_plural = "Order Lines"


    def __str__(self):
        return f"({self.options}, {self.product} {self.order} qty: {self.quantity})"


class Cocktail(models.Model):
    cocktail_name = models.CharField(max_length=200, blank=True, null=True)
    description = HTMLField("Description", max_length=4096, default="")
    recipe = HTMLField("Recipe", max_length=4096, default="")

    class Meta:
        verbose_name = "Cocktail"
        verbose_name_plural = "Cocktails"

    def __str__(self):
        return f"{self.cocktail_name}"

