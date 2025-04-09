from django import forms
from django.forms import DateInput, HiddenInput, ModelForm

from .models import Category, Option, Order, Product, ProductRating


class OptionForm(ModelForm):
    class Meta:
        model = Option
        fields = "__all__"


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class DateTimeInput(DateInput):
    input_type = "datetime-local"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["user", "deadline", "options", "product", "quantity"]
        widgets = {"user": HiddenInput(), "deadline": DateTimeInput()}


REVIEW_CHOICES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]


class ProductRatingForm(ModelForm):
    class Meta:
        model = ProductRating
        fields = ["product", "text", "author", "score"]
        widgets = {
            "score": forms.RadioSelect(choices=REVIEW_CHOICES),
            "author": HiddenInput(),
            "product": HiddenInput(),
        }
