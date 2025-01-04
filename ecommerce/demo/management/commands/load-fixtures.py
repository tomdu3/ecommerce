from django.core.management import call_command
from django.core.management.base import BaseCommand

# https://docs.djangoproject.com/en/5.1/howto/custom-management-commands/

class Command(BaseCommand):

    def handle(self, *args, **options):
        # copy commands from our previous fixtures
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        # before running the commands, delete migrations and database file
        # reset the whole system
        # run from the root directory: `./manage.py load-fixtures`
