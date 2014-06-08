# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand

from example.tests.scenario import default_scenario_product


class Command(BaseCommand):

    help = "Create demo data for 'product'"

    def handle(self, *args, **options):
        default_scenario_product()
        print("Created 'product' demo data...")
