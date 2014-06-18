# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from base.form_utils import RequiredFieldForm

from .models import (
    Product,
    ProductBundle,
)


class BundleAddProductForm(forms.Form):

    product = forms.ModelChoiceField(Product.objects.all())


class BundleForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(BundleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )

    class Meta:
        model = ProductBundle
        fields = (
            'name',
            'slug',
            'product',
            'price',
            'legacy',
        )


class EmptyForm(forms.Form):

    pass


class ProductForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for name in ('name', 'description'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'category',
            'description',
            'price',
            'legacy',
        )
