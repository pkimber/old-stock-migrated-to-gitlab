# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.text import slugify

from base.tests.model_maker import clean_and_save

from stock.models import (
    Product,
    ProductCategory,
    ProductType,
)


def make_product(name, slug, price, category, **kwargs):
    defaults = dict(
        name=name,
        slug=slugify(slug),
        price=price,
        category=category,
    )
    defaults.update(kwargs)
    return clean_and_save(Product(**defaults))


#def make_product_bundle(name, slug, product, price, **kwargs):
#    defaults = dict(
#        name=name,
#        slug=slugify(slug),
#        product=product,
#        price=price,
#    )
#    defaults.update(kwargs)
#    return clean_and_save(ProductBundle(**defaults))


def make_product_category(name, slug, product_type, **kwargs):
    defaults = dict(
        name=name,
        slug=slugify(slug),
        product_type=product_type,
    )
    defaults.update(kwargs)
    return clean_and_save(ProductCategory(**defaults))


def make_product_type(name, slug, **kwargs):
    defaults = dict(
        name=name,
        slug=slugify(slug),
    )
    defaults.update(kwargs)
    return clean_and_save(ProductType(**defaults))
