from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class selfTest(TestCase):
    def ProductSetUp(self):
        Product.objects.create(name = "Tiny Cup", amount = "56", description = "blue butterflies edition")
        Product.objects.create(name = "Not So Tiny Cup", amount = "13", description = "halloween edition")
        Product.objects.create(name = "Very Not Tiny Cup", amount = "0", description = "cats edition")

    def product_check_stock(self):
        tiny_cup = Product.objects.get(name = "Tiny Cup")
        self.assertEqual(tiny_cup.stock_checking(), "Stock of Tiny Cup is currently available: 56 pcs.")
        very_not_tiny = Product.objects.get(description = "cats edition")
        self.assertEqual(very_not_tiny.stock_checking(), "Stock of Very Not Tiny Cup is currently not available.")

