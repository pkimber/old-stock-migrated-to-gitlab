# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from stock.tests.model_maker import (
    make_product,
    make_product_category,
    make_product_type,
)


def default_scenario_product():
    stock = make_product_type('Stock', 'stock')
    stationery = make_product_category('Stationery', 'stationery', stock)
    make_product('Pencil', 'pencil', Decimal('1.32'), stationery)
