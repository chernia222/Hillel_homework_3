import pytest
import requests

class UserSignUpModel:
    def __init__(self, name, last_name, email, password, repeat_password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.repeat_password = repeat_password

user_to_sign_up = UserSignUpModel("Vova", "John", "qwertyyyy@test.com", "Qwerty12345", "Qwerty12345")

@pytest.fixture
def session():
    return requests.session()

def test_check_current_user_test(session):
    get_current_user = session.get("https://qauto2.forstudy.space/api/users/current")
    assert get_current_user.status_code == 200

@pytest.mark.parametrize("password, expected_password", [("Qwerty12345", "Qwerty12345"), ("Qwerty", "Qwerty12345")])
def test_password_test(password, expected_password):
    assert password == expected_password
