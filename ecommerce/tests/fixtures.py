import pytest


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
