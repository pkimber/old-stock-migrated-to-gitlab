# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.template.defaultfilters import slugify

import factory
# https://github.com/rbarrois/factory_boy/issues/138
from factory import fuzzy

from stock.models import (
    Product,
    ProductCategory,
    ProductType,
)


class ProductTypeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ProductType

    @factory.sequence
    def slug(n):
        return 'type_{:02d}'.format(n)


class ProductCategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = ProductCategory

    product_type = factory.SubFactory(ProductTypeFactory)

    @factory.sequence
    def slug(n):
        return 'category_{:02d}'.format(n)


class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Product

    category = factory.SubFactory(ProductCategoryFactory)
    price = fuzzy.FuzzyDecimal(10.00, 100.00)

    @factory.sequence
    def name(n):
        return 'product_name_{:02d}'.format(n)

    @factory.sequence
    def slug(n):
        return 'product_slug_{:02d}'.format(n)
