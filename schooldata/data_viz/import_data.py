from django.core.management.base import BaseCommand
from data_viz.utils import load_student_data


class Command(BaseCommand):
    help = 'Load student data from CSV'

    def handle(self, *args, **options):
        load_student_data()
        self.stdout.write(self.style.SUCCESS('Successfully loaded student data'))

# Path: schooldata/data_viz/management/commands/load_student_data.py