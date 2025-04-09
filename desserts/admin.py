from django.contrib import admin

from desserts.models import (Category, Cocktail, Contact, GalleryCategory,
                             GalleryImage, Option, Order, Product,
                             ProductRating)


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]
    list_display = ["order_date", "price", "user", "deadline", "status"]
    list_editable = ["deadline", "status"]


class OptionAdmin(admin.ModelAdmin):
    list_display = ["name"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["category", "name", "description", "price"]
    list_filter = ["category", "name", "price"]
    list_editable = ["name", "description", "price"]
    search_fields = ["category", "name"]


class CocktailAdmin(admin.ModelAdmin):
    model = Cocktail
    list_display = ["cocktail_name", "description", "recipe"]
    list_editable = ["description", "recipe"]


class GalleryCategoryAdmin(admin.ModelAdmin):
    model = GalleryCategory
    list_display = ["name"]
    list_filter = ["name"]


class GalleryImageAdmin(admin.ModelAdmin):
    model = GalleryImage
    list_display = ["image_category", "name"]
    list_filter = ["image_category", "name"]

class ProductRatingAdmin(admin.ModelAdmin):
    model = ProductRating
    list_display = ["product", "score", "author", "date", "text"]


admin.site.register(Option, OptionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(GalleryCategory, GalleryCategoryAdmin)
admin.site.register(ProductRating, ProductRatingAdmin)
admin.site.register(Contact)
