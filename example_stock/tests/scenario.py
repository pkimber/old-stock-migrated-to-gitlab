# -*- encoding: utf-8 -*-
from decimal import Decimal

from stock.models import Product
from stock.tests.model_maker import (
    make_product_category,
    make_product_type,
)


def default_scenario_product():
    stock = make_product_type('Stock', 'stock')
    stationery = make_product_category('Stationery', 'stationery', stock)
    Product.objects.create_product(
        'pencil', 'Pencil', '', Decimal('1.32'), stationery
    )
