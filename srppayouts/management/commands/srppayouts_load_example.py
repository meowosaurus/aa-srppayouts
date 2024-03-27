from django.core.management.base import BaseCommand
from srppayouts.data_utils import add_example_reimbursements, add_example_payouts
from srppayouts import __title__, __version__

class Command(BaseCommand):
    help = 'Populate database with example data'

    prefix = "[" + __title__ + " " + __version__ + "] "

    def handle(self, *args, **kwargs):
        add_example_reimbursements()
        self.stdout.write(self.style.SUCCESS(self.prefix + 'Example reimbursement columns successfully populated!'))
        add_example_payouts()