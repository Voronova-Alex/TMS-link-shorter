from django.core.management.base import BaseCommand
from link_shoter_app.models import Link
from datetime import datetime, timedelta

DAYS_AGO = timedelta(days=365)

class Command(BaseCommand):
    def add_argument(self):
        pass

    def handle(self, *args, **options):

        if Link.objects.filter(date_last_click__lte=(datetime.now() - DAYS_AGO)).exists():
            Link.objects.filter(date_last_click__lte=(datetime.now() - DAYS_AGO)).delete()
