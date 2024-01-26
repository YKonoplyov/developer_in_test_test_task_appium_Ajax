from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, element_id: str) -> WebElement:
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, f"{element_id}"))
        )
        return element

    def find_element_by_text(self, text: str) -> WebElement:
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, f"//*[@text='{text}']"))
        )
        return element

    def open_sidebar(self):
        sidebar_button = self.find_element_by_id("menuDrawer")
        self.click_element(sidebar_button)

    @staticmethod
    def click_element(element):
        element.click()
