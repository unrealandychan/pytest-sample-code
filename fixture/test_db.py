from db import Database
import pytest

# This is very useful when you want to run a setup before the test runs.
# In this case, we are creating a new instance of the Database class

@pytest.fixture
def db():
    database = Database()
    yield database # Provide a fixture instance
    database.data.clear() # Clean up the data after the test runs


def test_add_user(db):
    db.add_user(1,"eddie")
    assert db.get_user_by_id(1) == "eddie"

def test_add_duplicate_user(db):
    db.add_user(1,"eddie")
    with pytest.raises(ValueError,match="User already exists"):
        db.add_user(1,"eddie")

def test_delete_user(db):
    db.add_user(1,"eddie")
    db.delete_user(1)
    assert db.get_user_by_id(1) == None
