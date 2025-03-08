from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def _init_driver(context):
    service = Service(ChromeDriverManager().install())

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(1024, 768)
    driver.implicitly_wait(0.5)
    context.driver = driver


def before_all(context):
    pass


def after_all(context):
    pass


def before_scenario(context, scenario):
    _init_driver(context)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        import os
        from datetime import datetime

        screenshots_folder = "screenshots"
        n = datetime.now()
        ns = n.strftime("%Y%m%dT%H%M%S")
        os.makedirs(screenshots_folder, exist_ok=True)
        context.driver.save_screenshot(f"{screenshots_folder}/{scenario.name}-{ns}.png")
    context.driver.quit()
