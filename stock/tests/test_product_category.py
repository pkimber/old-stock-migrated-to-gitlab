# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from stock.models import ProductCategory

from .factories import (
    ProductCategoryFactory,
    ProductTypeFactory,
)


class TestProductCategory(TestCase):

    def test_str(self):
        str(ProductCategoryFactory())

    def test_product_type(self):
        product_type = ProductTypeFactory()
        ProductCategoryFactory()
        ProductCategoryFactory(product_type=product_type)
        ProductCategoryFactory(product_type=product_type)
        categories = ProductCategory.objects.product_type(product_type.slug)
        self.assertEqual(2, categories.count())
