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
        self.pencil = init_product(
            'Pencil', 'pencil', '', Decimal('1.32'), stationery
        )
        init_product(
            'Pen', 'pen', '', Decimal('1.00'), stationery
        )
        #self.special_offer = init_product_bundle(
        #    'Pencil and a Pen',
        #    'pencil_pen_promo',
        #    self.pencil,
        #    Decimal('1.50'),
        #)
        #self.special_offer.bundle.add(pen)
        #self.special_offer.bundle.add(self.pencil)

    #def test_bundle_create(self):
    #    url = reverse('stock.bundle.create')
    #    self.assert_staff_only(url)

    #def test_bundle_detail(self):
    #    url = reverse(
    #        'stock.bundle.detail',
    #        kwargs=dict(pk=self.special_offer.pk)
    #    )
    #    self.assert_staff_only(url)

    #def test_bundle_list(self):
    #    url = reverse('stock.bundle.list')
    #    self.assert_staff_only(url)

    #def test_bundle_product_add(self):
    #    url = reverse(
    #        'stock.bundle.product.add',
    #        kwargs=dict(pk=self.special_offer.pk)
    #    )
    #    self.assert_staff_only(url)

    #def test_bundle_product_remove(self):
    #    url = reverse(
    #        'stock.bundle.product.remove',
    #        kwargs=dict(
    #            bundle_pk=self.special_offer.pk,
    #            product_pk=self.pencil.pk,
    #        )
    #    )
    #    self.assert_staff_only(url)

    #def test_bundle_update(self):
    #    url = reverse(
    #        'stock.bundle.update',
    #        kwargs=dict(pk=self.special_offer.pk)
    #    )
    #    self.assert_staff_only(url)

    def test_product_create(self):
        url = reverse('stock.product.create')
        self.assert_staff_only(url)

    def test_product_list(self):
        url = reverse('stock.product.list')
        self.assert_staff_only(url)

    def test_product_update(self):
        url = reverse(
            'stock.product.update',
            kwargs=dict(pk=self.pencil.pk)
        )
        self.assert_staff_only(url)
