from django.contrib import admin

from desserts.models import (Category, Cocktail, GalleryCategory, GalleryImage,
                             Option, Order, OrderLine, Product)


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]
    inlines = [OrderLineInline]
    list_display = ["order_date", "total_price", "user", "deadline", "status"]
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


admin.site.register(Option, OptionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderLine)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(GalleryCategory, GalleryCategoryAdmin)
