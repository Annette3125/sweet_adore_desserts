from django.contrib import admin
from django.forms import ModelForm

from desserts.models import (Cake, CakeByDesign, CakeByFlavour, CakeByOccasion,
                             CakePop, Cocktail, Cookie, Order)


class CakeAdmin(admin.ModelAdmin):
    list_display = ["cake_by_occasion", "cake_by_flavour", "cake_by_design"]
    list_filter = ["cake_by_occasion", "cake_by_flavour", "cake_by_design"]


class CakeByOccasionAdmin(admin.ModelAdmin):
    list_display = ["by_occasion", "description"]


class CakeByDesignAdmin(admin.ModelAdmin):
    list_display = ["by_design", "description"]


class CakeByFlavourAdmin(admin.ModelAdmin):
    list_display = ["by_flavour", "description"]


class CookieAdmin(admin.ModelAdmin):
    list_display = ["cookie", "price", "quantity", "description"]
    list_editable = ["price"]


class CakePopAdmin(admin.ModelAdmin):
    list_display = ["cake_pops", "price", "quantity", "description"]
    list_editable = ["price"]


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = [
        "cake",
        "cookie",
        "cake_pops",
        "date",
        "total_price",
        "user",
        "deadline",
    ]
    search_fields = ["cake", "cookie", "cake_pops"]


class CocktailAdmin(admin.ModelAdmin):
    model = Cocktail
    list_display = ["cocktail_name", "description", "recipe"]
    list_editable = ["description", "recipe"]


admin.site.register(Cake, CakeAdmin)
admin.site.register(CakeByOccasion, CakeByOccasionAdmin)
admin.site.register(CakeByDesign, CakeByDesignAdmin)
admin.site.register(CakeByFlavour, CakeByFlavourAdmin)
admin.site.register(Cookie, CookieAdmin)
admin.site.register(CakePop, CakePopAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cocktail, CocktailAdmin)
