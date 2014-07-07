# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.template.defaultfilters import slugify

import factory

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDecimal

from stock.models import (
    Product,
    ProductCategory,
    ProductType,
)


class ProductTypeFactory(DjangoModelFactory):

    class Meta:
        model = ProductType

    @factory.sequence
    def slug(n):
        #slug = slugify(factory.Sequence(lambda n: 'type_{:02d}'.format(n)))
        return 'type_{:02d}'.format(n)


class ProductCategoryFactory(DjangoModelFactory):

    class Meta:
        model = ProductCategory

    product_type = SubFactory(ProductTypeFactory)
    @factory.sequence
    def slug(n):
        #slug = slugify(factory.Sequence(lambda n: 'category_{:02d}'.format(n)))
        return 'category_{:02d}'.format(n)


class ProductFactory(DjangoModelFactory):

    class Meta:
        model = Product

    category = SubFactory(ProductCategoryFactory)
    price = FuzzyDecimal(10.00, 100.00)

    @factory.sequence
    def slug(n):
        #slug = slugify(factory.Sequence(lambda n: 'product_{:02d}'.format(n)))
        return 'product_{:02d}'.format(n)
