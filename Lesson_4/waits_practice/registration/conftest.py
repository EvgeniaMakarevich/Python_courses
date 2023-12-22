from faker import Faker
import pytest

@pytest.fixture
def random_email():
    fake = Faker()
    return fake.email()

