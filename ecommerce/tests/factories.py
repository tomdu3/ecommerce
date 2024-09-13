import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from ecommerce.inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = fake.lexify(
        text="cat_name_??????"
    )  # create a random string that starts with cat_name_
    slug = fake.lexify(
        text="cat_slug_??????"
    )  # create a random string that starts with cat_slug_
    is_active = True
