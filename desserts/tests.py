from django.test import TestCase
from .models import OrderLine, Product

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sweet_adore_desserts.settings")
django.setup()

class OrderLineTestCase(TestCase):
    def test_order_line_price(self):
        product = Product.objects.create(name="Cake", price=10.0)
        order_line = OrderLine.objects.create(product=product, quantity=2)
        self.assertEqual(order_line.price, 20.0)