# -*- encoding: utf-8 -*-
from django.conf.urls import url

from .views import ProductCreateView, ProductListView, ProductUpdateView


urlpatterns = [
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
]
