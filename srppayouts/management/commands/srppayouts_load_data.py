from django.core.management.base import BaseCommand
from srppayouts.data_utils import add_ships
from srppayouts import __title__, __version__

class Command(BaseCommand):
    help = 'Populate database with predefined data'

    prefix = "[" + __title__ + " " + __version__ + "] "

    def handle(self, *args, **kwargs):

        self.stdout.write(self.prefix + 'Loading data might take a while.')
        add_ships()
        self.stdout.write(self.style.SUCCESS(self.prefix + 'Ship data successfully populated!'))