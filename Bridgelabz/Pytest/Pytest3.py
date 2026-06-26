#Fixtures in Pytest
import pytest
@pytest.fixture
def user_data():
    return {"username": "testuser", "password": "testpass"}

def test_user_login(user_data):
    assert user_data["username"] == "testuser"
    assert user_data["password"] == "testpass"

def test_user_login_failure(user_data):
    assert user_data["username"] != "wronguser"
    assert user_data["password"] != "wrongpass" 

#Parameterization in Pytest
import pytest
def square(x):
    return x * x

@pytest.mark.parametrize("input, expected", [
    (2, 4),
    (3, 9),
    (4, 16)
])
def test_square(input, expected):
    assert square(input) == expected 