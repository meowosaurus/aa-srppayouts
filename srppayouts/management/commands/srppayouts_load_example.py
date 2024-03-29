from django.core.management.base import BaseCommand
from srppayouts.data_utils import add_example_reimbursements, add_example_payouts
from srppayouts import __title__, __version__

class Command(BaseCommand):
    help = 'Populate database with example data'

    prefix = "[" + __title__ + " " + __version__ + "] "

    def handle(self, *args, **kwargs):
        try: 
            self.stdout.write(self.prefix + "Trying to load example reimbursements (columns)")
            add_example_reimbursements()
            self.stdout.write(self.style.SUCCESS(self.prefix + 'Example reimbursement columns successfully loaded!'))
        except Exception as e: 
            self.stderr.write(self.prefix + "Failed to load example reimbursements (columns)! Error: " + str(e))

        try:
            self.stdout.write(self.prefix + "Trying to load example payouts (cells)")
            add_example_payouts()
            self.stdout.write(self.style.SUCCESS(self.prefix + 'Example payout cells successfully loaded!'))
        except Exception as e: 
            self.stderr.write(self.prefix + "Failed to load example payouts (cells)! Error: " + str(e))