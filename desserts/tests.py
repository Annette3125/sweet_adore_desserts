from django.test import TestCase


import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sweet_adore_desserts.settings")
django.setup()


class MaxValueValidator:
    def __init__(self, max_value):
        self.max_value = max_value

    def __call__(self, value):
        if value > self.max_value:
            raise ValueError(f" value must be less than or equal to {self.max_value}")

class MinValueValidator:
    def __init__(self, min_value):
        self.min_value = min_value

        def __call__(self, value):
            if value < self.min_value:
                raise ValueError(f"Value must be greater than equal {self.min_value}")

max_validator = MaxValueValidator(100)
min_validator = MinValueValidator(0)

try:
    value = 100
    max_validator(value)
    print("value in range of max validator")
except ValueError as e:
    print(e)

try:
    value = 50
    min_validator(value)
    print("value in range of min validator")
except ValueError as e:
    print(e)

