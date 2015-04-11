# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.text import slugify

from stock.models import (
    Product,
    ProductCategory,
    ProductType,
)
from stock.tests.model_maker import (
    make_product,
    make_product_category,
    make_product_type,
)


def init_product(name, slug, description, price, product_category, **kwargs):
    """Create a new product - if it doesn't exist."""
    slug = slugify(slug)
    try:
        result = Product.objects.get(slug=slug)
        update = False
        # If the product exists - don't update it unless it is empty...
        # The user might have set a new price or description!!
        if not result.name:
            result.name = name or ''
            update = True
        if not result.description:
            result.description = description or ''
            update = True
        if not result.price:
            result.price = price
            update = True
        if result.category.slug == 'demo':
            result.category = product_category
            update = True
        if update:
            result.save()
    except Product.DoesNotExist:
        if not description:
            description = ''
        kwargs.update(dict(description=description))
        result = make_product(name, slug, price, product_category, **kwargs)
    return result


#def init_product_bundle(name, slug, product, price, **kwargs):
#    slug = slugify(slug)
#    try:
#        result = ProductBundle.objects.get(slug=slug)
#        # If the product exists - don't update it!!!
#        # The user might have set a new price or description!!
#    except ProductBundle.DoesNotExist:
#        result = make_product_bundle(name, slug, product, price, **kwargs)
#    return result
#
#
#def init_product_bundle_add_product(product_bundle, products):
#    """If a product has not been added to the bundle, then add it.
#
#    TODO When the system is live, I don't think we need this function as we
#    will have editing screens to add products to bundles.
#    """
#    for p in products:
#        try:
#            product_bundle.bundle.get(slug=p.slug)
#        except Product.DoesNotExist:
#            product_bundle.bundle.add(p)


def init_product_category(name, slug, product_type):
    result = None
    try:
        result = ProductCategory.objects.get(slug=slug)
        update = False
        if result.name != name:
            result.name = name or ''
            update = True
        if result.product_type.slug != product_type.slug:
            result.product_type = product_type
            update = True
        if update:
            result.save()
    except ProductCategory.DoesNotExist:
        result = make_product_category(name, slug, product_type)
    return result


def init_product_type(name, slug):
    result = None
    try:
        result = ProductType.objects.get(slug=slug)
        if result.name != name:
            result.name = name or ''
            result.save()
    except ProductType.DoesNotExist:
        result = make_product_type(name, slug)
    return result
