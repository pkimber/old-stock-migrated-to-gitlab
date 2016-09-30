# -*- encoding: utf-8 -*-
import pytest

from django.db import IntegrityError

from stock.models import Product
from .factories import (
    ProductCategoryFactory,
    ProductFactory,
    ProductTypeFactory,
)


@pytest.mark.django_db
def test_no_duplicate():
    product = ProductFactory()
    with pytest.raises(IntegrityError) as e:
        ProductFactory(slug=product.slug)
    assert 'UNIQUE constraint failed' in str(e.value)


@pytest.mark.django_db
def test_product_type():
    product_type = ProductTypeFactory()
    category = ProductCategoryFactory(product_type=product_type)
    ProductFactory()
    ProductFactory(category=category)
    ProductFactory(category=category)
    products = Product.objects.product_type(product_type.slug)
    assert 2 == products.count()


@pytest.mark.django_db
def test_str():
    assert 'Apple' == str(ProductFactory(name='Apple'))
