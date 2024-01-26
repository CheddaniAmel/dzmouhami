from django.core.management.base import BaseCommand
from app1.models import Avocat, Langue

class Command(BaseCommand):
    help = 'Update existing Avocat instances with default languages'

    def handle(self, *args, **options):
        # List of languages to assign to each Avocat
        default_languages = ['english', 'french', 'arabic']

        for avocat in Avocat.objects.all():
            # Set default languages for each Avocat
            for lang in default_languages:
                langue, created = Langue.objects.get_or_create(name=lang)
                avocat.langue.add(langue)

        print("Languages added to Avocat instances successfully.")
