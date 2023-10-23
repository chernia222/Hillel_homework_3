import allure
import pytest
import requests
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def session():
    return requests.session()

class TestBase:
    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._session = requests.session()

    def teardown_method(self):
        self._driver.quit()

    @allure.feature("play.djaminn.com")
    def test_djaminn_test(self):
        self._driver.implicitly_wait(3)
        self._driver.get("https://play.djaminn.com/")

        app_widget = self._driver.find_element(By.XPATH, "//a[@href='https://apps.apple.com/tt/app/djaminn-create-songs-together/id1634589883']")
        app_widget.click()
        # Ждем, чтобы убедиться, что страница загрузилась
        self._driver.implicitly_wait(10)

        allure.attach("Screenshot play.djaminn.com", self._driver.get_screenshot_as_png())

    @allure.feature("appstore")
    def test_appstore_test(self):
        get_appstore = self._session.get("https://apps.apple.com/tt/app/djaminn-create-songs-together/id1634589883")
        assert get_appstore.status_code == 200

        allure.attach("Screenshot appstore", self._driver.get_screenshot_as_png())
