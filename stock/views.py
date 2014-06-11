# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin

from .forms import (
    BundleForm,
    ProductForm,
)
from .models import (
    Product,
    ProductBundle,
)


class BundleCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, CreateView):

    form_class = BundleForm
    model = ProductBundle

    def get_success_url(self):
        return reverse('stock.bundle.list')


class BundleListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = ProductBundle


class BundleUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):

    form_class = BundleForm
    model = ProductBundle

    def get_success_url(self):
        return reverse('stock.bundle.list')


class ProductCreateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, CreateView):

    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('stock.product.list')


class ProductListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = Product


class ProductUpdateView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):

    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('stock.product.list')
