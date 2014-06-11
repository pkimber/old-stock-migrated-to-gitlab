# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import (
    patterns,
    url,
)

from .views import ProductListView


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=ProductListView.as_view(),
        name='stock.product.list'
        ),
)
