# -*- encoding: utf-8 -*-
from django.db import IntegrityError
from django.test import TestCase

from stock.models import Product

from .factories import (
    ProductCategoryFactory,
    ProductFactory,
    ProductTypeFactory,
)


class TestProduct(TestCase):

    def test_no_duplicate(self):
        product = ProductFactory()
        self.assertRaises(
            IntegrityError,
            ProductFactory,
            slug=product.slug,
        )

    def test_product_type(self):
        product_type = ProductTypeFactory()
        category = ProductCategoryFactory(product_type=product_type)
        ProductFactory()
        ProductFactory(category=category)
        ProductFactory(category=category)
        products = Product.objects.product_type(product_type.slug)
        self.assertEqual(2, products.count())

    def test_str(self):
        str(ProductFactory())
