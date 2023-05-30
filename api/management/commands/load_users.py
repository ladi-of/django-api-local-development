import csv
from django.core.management.base import BaseCommand, CommandError
from api.models import UserSpec
import os


class Command(BaseCommand):
    help = 'Load user data from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str,
                            help='The path to the CSV file.')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        if not os.path.isfile(csv_file):
            raise CommandError(f"'{csv_file}' does not exist.")

        try:
            with open(csv_file, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        UserSpec.objects.create(username=row['name'])
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(
                            f"Error creating user '{row['name']}': {e}"))
        except Exception as e:
            raise CommandError(f"Error reading '{csv_file}': {e}")

        self.stdout.write(self.style.SUCCESS('Successfully loaded user data.'))
