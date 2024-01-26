
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, element_id):
        element = WebDriverWait(
            self.driver,
            10
            ).until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ID, f"{element_id}"
                    )
                )
            )
        return element

    @staticmethod
    def click_element(element):
        element.click()
