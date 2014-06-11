# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from .views import (
    ProductCreateView,
    ProductListView,
    ProductUpdateView,
)


urlpatterns = patterns(
    '',
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
