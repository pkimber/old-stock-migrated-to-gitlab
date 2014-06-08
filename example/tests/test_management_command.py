# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from example.management.commands import demo_data_stock

from stock.management.commands import init_app_stock


class TestCommand(TestCase):

    def test_demo_data(self):
        """ Test the management command """
        pre_command = init_app_stock.Command()
        pre_command.handle()
        command = demo_data_stock.Command()
        command.handle()
