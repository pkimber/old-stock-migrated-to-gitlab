# -*- encoding: utf-8 -*-
from django.views.generic import (
    ListView,
    TemplateView,
)

from base.view_utils import BaseMixin
from stock.models import Product


class HomeView(BaseMixin, ListView):

    model = Product
    template_name = 'example/home.html'


class SettingsView(BaseMixin, TemplateView):

    template_name = 'example/settings.html'
