from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_locations = ['Cape Town', 'Durban', 'Johannesburg', 'Pretoria']
        titles = ['Beachside Villa', 'Mountain Cabin', 'City Apartment', 'Luxury Lodge']

        for i in range(10):
            Listing.objects.create(
                title=random.choice(titles),
                description='A wonderful place to stay.',
                location=random.choice(sample_locations),
                price_per_night=random.uniform(500, 2000),
                available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings'))
