# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    #BundleAddProductView,
    #BundleCreateView,
    #BundleDetailView,
    #BundleListView,
    #BundleRemoveProductView,
    #BundleUpdateView,
    ProductCreateView,
    ProductListView,
    ProductUpdateView,
)


urlpatterns = patterns(
    '',
    #url(regex=r'^bundle/create/$',
    #    view=BundleCreateView.as_view(),
    #    name='stock.bundle.create'
    #    ),
    #url(regex=r'^bundle/(?P<pk>\d+)/$',
    #    view=BundleDetailView.as_view(),
    #    name='stock.bundle.detail'
    #    ),
    #url(regex=r'^bundle/$',
    #    view=BundleListView.as_view(),
    #    name='stock.bundle.list'
    #    ),
    #url(regex=r'^bundle/(?P<pk>\d+)/product/add/$',
    #    view=BundleAddProductView.as_view(),
    #    name='stock.bundle.product.add'
    #    ),
    #url(regex=r'^bundle/(?P<bundle_pk>\d+)/product/(?P<product_pk>\d+)/remove/$',
    #    view=BundleRemoveProductView.as_view(),
    #    name='stock.bundle.product.remove'
    #    ),
    #url(regex=r'^bundle/(?P<pk>\d+)/update/$',
    #    view=BundleUpdateView.as_view(),
    #    name='stock.bundle.update'
    #    ),
    url(regex=r'^product/create/$',
        view=ProductCreateView.as_view(),
        name='stock.product.create'
        ),
    url(regex=r'^product/$',
        view=ProductListView.as_view(),
        name='stock.product.list'
        ),
    url(regex=r'^product/(?P<pk>\d+)/update/$',
        view=ProductUpdateView.as_view(),
        name='stock.product.update'
        ),
)
