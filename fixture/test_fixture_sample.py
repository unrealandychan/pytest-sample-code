from fixture_sample import UserManager
import pytest

# Fixture is something that is used to setup some data before the test runs
# and clean up the data after the test runs
# In this case, we are using a fixture to create a user_manager object
@pytest.fixture
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("eddie","eddie.chan@gmail.com") == True
    assert user_manager.get_user_by_username("eddie") == "eddie.chan@gmail.com"

def test_add_user_duplicate(user_manager):
    user_manager.add_user("eddie","eddie.chan@gmail.com")
    with pytest.raises(ValueError,match="Username already exists"):
        user_manager.add_user("eddie","eddie.chan@gmail.com")