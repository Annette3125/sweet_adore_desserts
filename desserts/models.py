from django.db import models
from my_auth.models import User
from tinymce.models import HTMLField


class Cake(models.Model):
    cake_type = models.CharField(max_length=200, blank=True, null=False)
    cake_name = models.CharField(max_length=200, blank=True, null=False)
    description = HTMLField("Description", max_length=4096, default="")
    price = models.FloatField(blank=False, null=False)

    class Meta:
        verbose_name = "Cake"
        verbose_name_plural = "Cakes"

    def __str__(self):
        return f"{self.cake_type} {self.cake_name} {self.price}"


class Cookie(models.Model):
    cookie_name = models.CharField(max_length=200, blank=True, null=False)
    description = HTMLField("Description", max_length=4096, default="")
    price = models.FloatField(blank=False, null=False)
    quantity = models.FloatField(blank=False, null=False)


    class Meta:
        verbose_name = "Cookie"
        verbose_name_plural = "Cookies"

    def __str__(self):
        return f"{self.cookie_name} {self.price}"


class CakePops(models.Model):
    cake_pops_name = models.CharField(max_length=200, blank=True, null=False)
    description = HTMLField("Description", max_length=4096, default="")
    price = models.FloatField(blank=False, null=False)
    quantity = models.FloatField(blank=False, null=False)


    class Meta:
        verbose_name_plural = "Cake Pops"

    def __str__(self):
        return f"{self.cake_pops_name} {self.price}"


class Cocktail(models.Model):
    cocktail_name = models.CharField(max_length=200, blank=True, null=False)
    description = HTMLField("Description", max_length=4096, default="")

    class Meta:
        verbose_name = "Cocktail"
        verbose_name_plural = "Cocktails"

    def __str__(self):
        return f"{self.cocktail_name}"


class Dessert(models.Model):
    cookie = models.ForeignKey(
        Cookie, on_delete=models.CASCADE, blank=False, null=False
    )
    cake_pops = models.ForeignKey(
        CakePops, on_delete=models.CASCADE, blank=False, null=False
    )
    cake = models.ForeignKey(Cake, on_delete=models.RESTRICT, blank=False, null=False)
    description = HTMLField("Description", max_length=4096, default="")

    class Meta:
        verbose_name = "Dessert"
        verbose_name_plural = "Desserts"

    def __str__(self):
        return f"{self.cookie.cookie_name} {self.cake_pops.cake_pops_name} {self.cake.cake_name}"


class Order(models.Model):
    desserts = models.ForeignKey(
        Dessert, on_delete=models.CASCADE, blank=False, null=False
    )
    date = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    total_price = models.FloatField(blank=True, null=True, default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    deadline = models.DateTimeField(verbose_name="Deadline", null=True, blank=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-id"]
# class OrderLine(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.RESTRICT, blank=False, Nul=False)
#     quantity = models.IntegerField(blank=True, null=False, default=1)
#
