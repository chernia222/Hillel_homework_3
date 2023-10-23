import allure
import pytest
import requests


@pytest.fixture
def session():
    return requests.session()

@allure.feature("play.djaminn.com")
def test_homepage_test(session):
    get_homepage = session.get("https://play.djaminn.com/")
    assert get_homepage.status_code == 200