# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.template.defaultfilters import slugify

import factory

from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import (
    FuzzyDecimal,
    FuzzyText,
)

from stock.models import (
    Product,
    ProductCategory,
    ProductType,
)


class ProductTypeFactory(DjangoModelFactory):

    class Meta:
        model = ProductType

    slug = slugify(factory.Sequence(lambda n: 'type{}'.format(n)))


class ProductCategoryFactory(DjangoModelFactory):

    class Meta:
        model = ProductCategory

    product_type = SubFactory(ProductTypeFactory)
    slug = slugify(factory.Sequence(lambda n: 'category{}'.format(n)))


class ProductFactory(DjangoModelFactory):

    class Meta:
        model = Product

    category = SubFactory(ProductCategoryFactory)
    price = FuzzyDecimal(10.00, 100.00)
    slug = slugify(factory.Sequence(lambda n: 'product{}'.format(n)))
