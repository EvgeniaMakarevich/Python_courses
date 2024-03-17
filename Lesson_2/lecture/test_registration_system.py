import pytest
from registration_system import Registration_system


@pytest.fixture
def init_system():
    system  = Registration_system
    yield system
    system.delete_all_users()


def test_registration_with_pre_post_cond(init_system):
    init_system.register("Алекс", "alex@example.com", "+1234567890")
    users = init_system.view_all_users()
    assert alex@example.com in users