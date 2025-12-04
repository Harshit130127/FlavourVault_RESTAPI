"""
Django command to wait for database to be available.
"""

import time
from django.core.management.base import BaseCommand

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

class Command(BaseCommand):
    """ Django command to wait for database to be available. """
    
    def handle(self, *args, **options):   
        """ Entry point for command. """
        self.stdout.write('Waiting for database...')  # it is useful to inform the user that the command is running
        db_up = False   #  we will keep checking until database is available
        while not db_up:
            try:
                self.check(databases=['default'])   # Check the default database connection
                db_up = True # If the check is successful, set it to True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)  # wait for 1 second before retrying
        self.stdout.write(self.style.SUCCESS('Database available!'))
        