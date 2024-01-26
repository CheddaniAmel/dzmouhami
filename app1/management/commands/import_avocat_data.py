# management/commands/import_avocat_data.py
import json
import os
from django.core.management.base import BaseCommand
from app1.models import Avocat, specialisation, Langue
import django
django.setup()

class Command(BaseCommand):
    help = 'Import avocat data from a JSON file in the same directory as the command file'

    def handle(self, *args, **options):

        self.setup_defaults()

        # Get the directory path of this management command file
        directory_path = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to your JSON file in the same directory
        json_file_path = os.path.join(directory_path, 'data.json')

        with open(json_file_path, 'r', encoding='utf-8') as jsonfile:
            data = json.load(jsonfile)

            for row in data:
                # Extracting data from the scraped row
                full_name = row.get('full_name', '')
                address = row.get('address', '')
                categories = row.get('categories', [])

                # Creating Avocat instance
                avocat = Avocat.objects.create(
                    nom=full_name.split()[1] if full_name else '',
                    prenom=full_name.split()[0] if full_name else '',
                    adresse=address,
                    numero_tlfn="",  # You may add the telephone number if available in your data
                    email="",  # You may add the email if available in your data
                )

                # Create specialisations
                specialisations = [specialisation.objects.get_or_create(name=category)[0] for category in categories]

                # Add specialisations to the avocat instance
                avocat.specialisation.set(specialisations)

        self.stdout.write(self.style.SUCCESS('Avocat data imported successfully'))

    def setup_defaults(self):
        # Set up default values for models
        default_langue = Langue.objects.get_or_create(name='French')[0]

        # Set the default language for the Avocat model
        Avocat._meta.get_field('langue').default = [default_langue]
        
