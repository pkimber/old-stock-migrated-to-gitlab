# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from login.tests.scenario import default_scenario_login

from stock.service import (
    init_product,
    init_product_category,
    init_product_type,
)


class TestViewPerm(PermTestCase):

    def setUp(self):
        default_scenario_login()
        stock = init_product_type('Stock', 'stock')
        stationery = init_product_category(
            'Stationery', 'stationery', stock
        )
        self.product = init_product(
            'Pencil', 'pencil', '', Decimal('1.32'), stationery
        )

    def test_product_create(self):
        url = reverse('stock.product.create')
        self.assert_staff_only(url)

    def test_product_list(self):
        url = reverse('stock.product.list')
        self.assert_staff_only(url)

    def test_product_update(self):
        url = reverse(
            'stock.product.update',
            kwargs=dict(pk=self.product.pk)
        )
        self.assert_staff_only(url)
