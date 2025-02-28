from django.forms import ModelForm, HiddenInput
from .models import Option, Category, Product, Order, OrderLine, Cocktail


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


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["user", "deadline"]
        widgets = {"user": HiddenInput()}


class OrderLineForm(ModelForm):
    class Meta:
        model = OrderLine
        fields = "__all__"