"""
Test cases for custom management commands in the FlavourVault application.
"""

from unittest.mock import patch  # patch used for mocking objects in tests

from psycopg2 import OperationalError as Psycopg2Error  # Importing PostgreSQL OperationalError for simulation

from django.core.management import call_command   

from django.db.utils import OperationalError
from django.test import SimpleTestCase



@patch('core.management.commands.wait_for_db.Command.check') # this command will use the patch decorator to mock the database check method
class CommandTests(SimpleTestCase):
    """ Tests for custom management commands. """

    def test_wait_for_db_ready(self,patched_check):
        """ Test waiting for database if database is available. """
        
        patched_check.return_value = True  # Simulate database being ready
        
        call_command('wait_for_db')  # Call the custom command
        
        patched_check.assert_called_once_with(databases=['default'])  # Assert the check method was called once  
    
    
    def test_wait_for_db_delay(self,patched_check):
        """ Test waiting for database when getting OperationalError. """
        
        patched_check.side_effect = [Psycopg2Error]*2 + [OperationalError]*3 + [True]  # Simulate delays in database readiness
        
        call_command('wait_for_db')  # Call the custom command
        
        self.assertEqual(patched_check.call_count,6)  # Assert the check method was called six times
