# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from base.view_utils import BaseMixin

from stock.models import Product


class HomeView(BaseMixin, ListView):

    model = Product
    template_name = 'example/home.html'
