# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import reversion

from base.model_utils import TimeStampedModel


class ProductType(TimeStampedModel):
    """Type of product e.g. course or membership."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product type'
        verbose_name_plural = 'Product types'

    def __str__(self):
        return '{}'.format(self.name)

reversion.register(ProductType)


class ProductCategoryManager(models.Manager):

    def product_type(self, slug):
        """List of all categories with the selected product type (slug)."""
        return self.model.objects.filter(product_type__slug=slug)


class ProductCategory(TimeStampedModel):
    """Category of product e.g. craft or gardening course."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    product_type = models.ForeignKey(ProductType)
    objects = ProductCategoryManager()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

    def __str__(self):
        return '{}'.format(self.name)

reversion.register(ProductCategory)


class ProductManager(models.Manager):

    def product_type(self, slug):
        """List of all products which have a type (slug)."""
        return self.model.objects.filter(category__product_type__slug=slug)


class Product(TimeStampedModel):
    """List of products and their price.

    The 'bundle' field allows us to build a bundle of products
    e.g. a pack of pencils + pens for a cheaper price than buying them
    separately.
    """

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(ProductCategory)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # option to hide legacy products
    legacy = models.BooleanField(default=False)
    objects = ProductManager()

    class Meta:
        ordering = ('legacy', 'category__slug', 'name')
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    def __str__(self):
        return '{}'.format(self.name)

reversion.register(Product)


#class ProductBundle(TimeStampedModel):
#    """If a product is selected... then display the 'bundle' of products.
#
#    If a product is selected, then these are the bundles to display.
#    """
#
#    name = models.CharField(max_length=100)
#    slug = models.SlugField(unique=True)
#    product = models.ForeignKey(Product, related_name='+')
#    price = models.DecimalField(max_digits=8, decimal_places=2)
#    bundle = models.ManyToManyField(Product, related_name='bundles')
#    # option to hide legacy bundles
#    legacy = models.BooleanField(default=False)
#
#    class Meta:
#        ordering = ('legacy', 'product__name', 'name',)
#        verbose_name = 'Product bundle'
#        verbose_name_plural = 'Product bundles'
#
#    def __str__(self):
#        return '{}'.format(self.name)
#
#reversion.register(ProductBundle)
