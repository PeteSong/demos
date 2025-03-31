import os
from datetime import datetime

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService

APPIUM_HOST = "127.0.0.1"
APPIUM_PORT = 4723


@pytest.fixture(scope="session")
def appium_service():
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of
        # server command line arguments
        args=["--address", APPIUM_HOST, "-p", str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()


def create_ios_driver(custom_opts=None):
    options = XCUITestOptions()
    options.platformVersion = "13.4"
    # options.udid = "123456789ABC"
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    return webdriver.Remote(f"http://{APPIUM_HOST}:{APPIUM_PORT}", options=options)


def create_android_driver(custom_opts=None):
    options = UiAutomator2Options()
    options.platformVersion = "10"
    # options.udid = "123456789ABC"
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    return webdriver.Remote(f"http://{APPIUM_HOST}:{APPIUM_PORT}", options=options)


@pytest.fixture
def ios_driver_factory():
    return create_ios_driver


@pytest.fixture
def ios_driver():
    # prefer this fixture if there is no need to customize driver options in tests
    driver = create_ios_driver()
    yield driver
    driver.quit()


@pytest.fixture
def android_driver_factory():
    return create_android_driver


@pytest.fixture
def android_driver():
    # prefer this fixture if there is no need to customize driver options in tests
    driver = create_android_driver()
    yield driver
    driver.quit()


def pytest_configure(config):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"reports/report_{now}.html"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # get the report object
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("android_driver")
        if driver:
            test_name = item.name
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"reports/screenshots/{test_name}_{now}.png"

            os.makedirs(os.path.dirname(file_name), exist_ok=True)

            driver.save_screenshot(file_name)
            print(f"\n[Appium] Screenshot saved to: {file_name}")
