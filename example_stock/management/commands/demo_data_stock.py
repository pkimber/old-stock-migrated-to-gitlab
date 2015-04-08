# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand

from example_stock.tests.scenario import default_scenario_product


class Command(BaseCommand):

    help = "Create demo data for 'product'"

    def handle(self, *args, **options):
        default_scenario_product()
        print("Created 'product' demo data...")
