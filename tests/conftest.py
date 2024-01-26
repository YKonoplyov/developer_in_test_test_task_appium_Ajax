import subprocess
import time
import os
import pytest

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from utils.android_utils import (
    android_get_desired_capabilities,
    get_udid_of_connected_device,
)
from dotenv import load_dotenv

load_dotenv()

APPIUM_HOST = "127.0.0.1"
APPIUM_PORT = "4723"


@pytest.fixture(scope="session")
def appium_service():
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of
        # server command line arguments
        args=["--address", APPIUM_HOST, "-p", APPIUM_PORT],
        timeout_ms=20000,
    )
    yield service
    service.stop()


def create_android_driver(custom_opts=None):
    options = UiAutomator2Options()
    custom_opts["udid"] = get_udid_of_connected_device()
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    return webdriver.Remote(f"http://{APPIUM_HOST}:{APPIUM_PORT}", options=options)


@pytest.fixture
def driver():
    driver = create_android_driver(android_get_desired_capabilities())
    yield driver
    driver.quit()
