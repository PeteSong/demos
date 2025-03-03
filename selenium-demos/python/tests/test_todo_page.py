"""
An example of `python + pytest + selenium`
which implemented "**Action Bot**, **Loadable Component** and **Page Object**".
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.action_bot import ActionBot
from src.loadable_component import LoadableComponent


class TodoPage(LoadableComponent):
    url = "https://todomvc.com/examples/react/dist/"

    new_todo_by = (By.CSS_SELECTOR, "input.new-todo")
    count_todo_left_by = (By.CSS_SELECTOR, "span.todo-count")
    todo_items_by = (By.CSS_SELECTOR, "ul.todo-list>li")

    view_all_by = (By.LINK_TEXT, "All")
    view_active_by = (By.LINK_TEXT, "Active")
    view_completed_by = (By.LINK_TEXT, "Completed")

    toggle_all_by = (By.CSS_SELECTOR, "input.toggle-all")
    clear_completed_by = (By.CSS_SELECTOR, "button.clear-completed")

    @staticmethod
    def build_todo_by(s: str) -> tuple:
        p = f"//li[.//label[contains(text(), '{s}')]]"
        return By.XPATH, p

    @staticmethod
    def build_todo_item_label_by(s: str) -> tuple:
        p = f"//label[contains(text(), '{s}')]"
        return By.XPATH, p

    @staticmethod
    def build_todo_item_toggle_by(s: str) -> tuple:
        by, using = TodoPage.build_todo_item_label_by(s)
        p = f"{using}/../input[@class='toggle']"
        return by, p

    @staticmethod
    def build_todo_item_delete_by(s: str) -> tuple:
        by, using = TodoPage.build_todo_item_label_by(s)
        p = f"{using}/../button[@class='destroy']"
        return by, p

    def build_count_todo_left(self, count: int) -> str:
        if count == 1:
            return "1 item left!"
        else:
            return f"{count} items left!"

    def __init__(self, driver):
        self.driver = driver
        self.bot = ActionBot(driver)

    def load(self):
        self.driver.get(self.url)

    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.new_todo_by))
            return True
        except Exception:
            return False

    # business domain below
    def count_todo_items_left(self) -> str:
        return self.bot.text(self.count_todo_left_by)

    def todo_count(self) -> int:
        return len(self.bot.elements(self.todo_items_by))

    def new_todo(self, s: str):
        self.bot.type(self.new_todo_by, s + "\n")

    def toggle_todo(self, s: str):
        self.bot.click(self.build_todo_item_toggle_by(s))

    def hover_todo(self, s: str) -> None:
        self.bot.hover(self.build_todo_by(s))

    def delete_todo(self, s: str):
        self.hover_todo(s)
        self.bot.click(self.build_todo_item_delete_by(s))

    def clear_completed_todo(self):
        self.bot.click(self.clear_completed_by)

    def toggle_all_todo(self):
        self.bot.click(self.toggle_all_by)

    def view_all_todo(self):
        self.bot.click(self.view_all_by)

    def view_active_todo(self):
        self.bot.click(self.view_active_by)

    def view_completed_todo(self):
        self.bot.click(self.view_completed_by)


@pytest.fixture
def page(chrome_driver) -> TodoPage:
    driver = chrome_driver
    return TodoPage(driver).get()


class TestTodoPage:
    def test_new_todo(self, page: TodoPage):
        assert page.todo_count() == 0
        page.new_todo("aaa")
        assert page.count_todo_items_left() == page.build_count_todo_left(1)

    def test_todo_toggle(self, page: TodoPage):
        s = "aaa"
        page.new_todo(s)
        assert page.count_todo_items_left() == page.build_count_todo_left(1)

        page.toggle_todo(s)
        assert page.count_todo_items_left() == page.build_count_todo_left(0)

        page.toggle_todo(s)
        assert page.count_todo_items_left() == page.build_count_todo_left(1)

    def test_todo_delete(self, page: TodoPage):
        s1 = "aaa"
        s2 = "bbb"
        page.new_todo(s1)
        page.new_todo(s2)
        assert page.count_todo_items_left() == page.build_count_todo_left(2)

        page.delete_todo(s1)
        assert page.count_todo_items_left() == page.build_count_todo_left(1)

        page.delete_todo(s2)
        assert page.todo_count() == 0

    def test_new_100_todo(self, page: TodoPage):
        for i in range(100):
            s = f"ToDo{i}"
            page.new_todo(s)
        assert page.count_todo_items_left() == page.build_count_todo_left(100)

    def test_toggle_all_todo(self, page: TodoPage):
        for i in range(10):
            s = f"ToDo{i}"
            page.new_todo(s)
        assert page.count_todo_items_left() == page.build_count_todo_left(10)
        assert page.todo_count() == 10

        page.toggle_all_todo()
        assert page.count_todo_items_left() == page.build_count_todo_left(0)
        assert page.todo_count() == 10

        page.toggle_all_todo()
        assert page.count_todo_items_left() == page.build_count_todo_left(10)
        assert page.todo_count() == 10

    def test_clear_completed_todo(self, page: TodoPage):
        for i in range(10):
            s = f"ToDo{i}"
            page.new_todo(s)
        assert page.count_todo_items_left() == page.build_count_todo_left(10)
        assert page.todo_count() == 10

        for i in range(5):
            s = f"ToDo{i}"
            page.toggle_todo(s)
        assert page.count_todo_items_left() == page.build_count_todo_left(5)
        assert page.todo_count() == 10

        page.clear_completed_todo()
        assert page.count_todo_items_left() == page.build_count_todo_left(5)
        assert page.todo_count() == 5

    def test_view_todo(self, page: TodoPage):
        for i in range(10):
            s = f"ToDo{i}"
            page.new_todo(s)
        for i in range(4):
            s = f"ToDo{i}"
            page.toggle_todo(s)

        page.view_all_todo()
        assert page.count_todo_items_left() == page.build_count_todo_left(6)
        assert page.todo_count() == 10

        page.view_active_todo()
        assert page.count_todo_items_left() == page.build_count_todo_left(6)
        assert page.todo_count() == 6

        page.view_completed_todo()
        assert page.count_todo_items_left() == page.build_count_todo_left(6)
        assert page.todo_count() == 4
