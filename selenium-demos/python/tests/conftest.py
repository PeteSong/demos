import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver(request):
    marker = request.node.get_closest_marker("driver_type")
    driver_type = marker.args[0] if marker else None

    if driver_type == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.set_window_size(1024, 768)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def chrome_driver():
    options = Options()
    options.add_argument("--headless")
    with webdriver.Chrome(options=options) as driver:
        driver.set_window_size(1024, 768)
        driver.implicitly_wait(0.5)
        yield driver
