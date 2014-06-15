# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    DetailView,
    FormView,
    ListView,
    UpdateView,
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin

from .forms import (
    BundleAddProductForm,
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


class BundleDetailView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, DetailView):

    model = ProductBundle


class BundleListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = ProductBundle


class BundleAddProductView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, FormView):

    form_class = BundleAddProductForm
    template_name = 'stock/bundle_add_product_form.html'

    def _get_bundle(self):
        pk = self.kwargs.get('pk')
        bundle = ProductBundle.objects.get(pk=pk)
        return bundle

    def get_context_data(self, **kwargs):
        context = super(BundleAddProductView, self).get_context_data(**kwargs)
        context.update(dict(
            bundle=self._get_bundle(),
        ))
        return context

    def form_valid(self, form):
        product = form.cleaned_data['product']
        bundle = self._get_bundle()
        bundle.bundle.add(product)
        return HttpResponseRedirect(
            reverse(
                'stock.bundle.detail',
                kwargs=dict(pk=bundle.pk, )
            )
        )


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
