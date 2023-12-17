import pytest
from faker import Faker


@pytest.fixture
def fake_email():
    fake = Faker()
    return fake.email()

def test_email_format(fake_email):
    assert "@" in fake_email
    assert "." in fake_email.split('@')[1]
    assert len(fake_email) > 0








