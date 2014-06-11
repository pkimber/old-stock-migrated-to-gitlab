# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin

from .models import Product


class ProductListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = Product
