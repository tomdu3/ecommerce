import pytest
from django.contrib.auth.models import User
from django.core.management import call_command


@pytest.fixture()
def create_admin_user(django_user_model):
    """
    Return admin user
    """
    username = "admin"
    email = "admin@localhost"
    password = "admin"
    user = django_user_model.objects.create_superuser(
        username=username, email=email, password=password
    )
    return user


@pytest.fixture(scope="session")
def django_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load database data fixtures
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")
