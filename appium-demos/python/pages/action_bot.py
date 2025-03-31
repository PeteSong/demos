from appium.webdriver.webelement import WebElement
from selenium.common import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class ActionBot:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=2,
            ignored_exceptions=[
                NoSuchElementException,
                StaleElementReferenceException,
                ElementNotInteractableException,
            ],
        )

    def element_located(self, locator: tuple) -> WebElement:
        # return self.wait.until(EC.visibility_of_element_located(locator))
        self.wait.until(lambda driver: driver.find_element(*locator))
        return self.driver.find_element(*locator)

    def elements_located(self, locator: tuple) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def element_located_in_element(self, element: WebElement, locator: tuple) -> WebElement:
        self.wait.until(lambda element: element.find_element(*locator))
        return element.find_element(*locator)

    def elements_located_in_element(self, elelment: WebElement, locator: tuple) -> list[WebElement]:
        return elelment.find_elements(*locator)

    def hover(self, locator: tuple) -> None:
        element = self.element_located(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def click(self, locator: tuple) -> None:
        element = self.element_located(locator)
        element.click()

    def type(self, locator: tuple, value: str) -> None:
        element = self.element_located(locator)
        element.clear()
        element.send_keys(value)

    def text(self, locator: tuple) -> str:
        element = self.element_located(locator)
        return element.text
