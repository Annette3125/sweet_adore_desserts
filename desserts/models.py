from django.db import models
from tinymce.models import HTMLField

from my_auth.models import User


class CakeByOccasion(models.Model):
    by_occasion = models.CharField(max_length=200, blank=True, null=True)
    description = HTMLField("Description", max_length=4096, default="")

    def __str__(self):
        return f"{self.by_occasion}"


class CakeByFlavour(models.Model):
    by_flavour = models.CharField(max_length=200, blank=True, null=True)
    description = HTMLField("Description", max_length=4096, default="")

    def __str__(self):
        return f"{self.by_flavour}"


class CakeByDesign(models.Model):
    by_design = models.CharField(max_length=200, blank=True, null=True)
    description = HTMLField("Description", max_length=4096, default="")

    def __str__(self):
        return f"{self.by_design}"


class Cake(models.Model):
    cake_by_occasion = models.ForeignKey(
        CakeByOccasion, on_delete=models.CASCADE, blank=True, null=True
    )
    cake_by_flavour = models.ForeignKey(
        CakeByFlavour, on_delete=models.CASCADE, blank=True, null=True
    )
    cake_by_design = models.ForeignKey(
        CakeByDesign, on_delete=models.CASCADE, blank=True, null=True
    )
    description = HTMLField("Description", max_length=4096, default="")
    price = models.FloatField(blank=False, null=False)
    quantity = models.IntegerField(blank=True, null=False, default=1)

    class Meta:
        verbose_name = "Cake"
        verbose_name_plural = "Cakes"

    def __str__(self):
        return f"{self.cake_by_occasion} {self.cake_by_flavour} {self.cake_by_design} {self.price}"


class Cookie(models.Model):
    cookie = models.CharField(max_length=200, blank=True, null=False)
    description = HTMLField("Description", max_length=4096, default="")
    price = models.FloatField(blank=False, null=False)
    quantity = models.IntegerField(blank=True, null=False, default=1)

    class Meta:
        verbose_name = "Cookie"
        verbose_name_plural = "Cookies"

    def __str__(self):
        return f"{self.cookie} {self.price}"


class CakePop(models.Model):
    cake_pops = models.CharField(max_length=200, blank=True, null=False)
    description = HTMLField("Description", max_length=4096, default="")
    price = models.FloatField(blank=False, null=False)
    quantity = models.IntegerField(blank=True, null=False, default=1)

    class Meta:
        verbose_name_plural = "Cake Pops"

    def __str__(self):
        return f"{self.cake_pops} {self.price}"


class Order(models.Model):
    cake = models.ForeignKey(
        Cake, on_delete=models.CASCADE, max_length=200, blank=True, null=True
    )
    cookie = models.ForeignKey(
        Cookie, on_delete=models.CASCADE, max_length=200, blank=True, null=True
    )
    cake_pops = models.ForeignKey(
        CakePop, on_delete=models.CASCADE, max_length=200, blank=True, null=True
    )
    date = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    total_price = models.FloatField(blank=True, null=True, default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    deadline = models.DateTimeField(verbose_name="Deadline", null=True, blank=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class Cocktail(models.Model):
    cocktail_name = models.CharField(max_length=200, blank=True, null=True)
    description = HTMLField("Description", max_length=4096, default="")
    recipe = HTMLField("Recipe", max_length=4096, default="")

    class Meta:
        verbose_name = "Cocktail"
        verbose_name_plural = "Cocktails"

    def __str__(self):
        return f"{self.cocktail_name}"
