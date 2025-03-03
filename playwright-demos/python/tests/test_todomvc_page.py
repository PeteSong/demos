import pytest
from playwright.sync_api import Page, expect

from src.todomvc_page import TodoMvcPage


@pytest.fixture(scope="function", autouse=True)
def todomvc(page: Page) -> TodoMvcPage:
    return TodoMvcPage(page).get()


class TestTodoMvcPage:
    def test_new_todo_item(self, todomvc: TodoMvcPage):
        expect(todomvc.footor).to_be_hidden()
        todomvc.expect_count_todo_left(0)
        expect(todomvc.todo_items).to_have_count(0)

        todo_str = "aaa"
        todomvc.new_todo(todo_str)

        todo_item_locator = todomvc.todo_item_locator(todo_str)
        expect(todo_item_locator).to_be_visible()
        expect(todomvc.footor).to_be_visible()
        todomvc.expect_count_todo_left(1)
        expect(todomvc.todo_items).to_have_count(1)

    def test_todo_toggle(self, todomvc: TodoMvcPage):
        todo_str = "aaa"
        todomvc.new_todo(todo_str)
        expect(todomvc.todo_items).to_have_count(1)
        todomvc.expect_count_todo_left(1)

        todomvc.todo_item_set_checked(todo_str)
        todomvc.expect_count_todo_left(0)
        expect(todomvc.todo_items).to_have_count(1)

        todomvc.todo_item_set_checked(todo_str, False)
        todomvc.expect_count_todo_left(1)
        expect(todomvc.todo_items).to_have_count(1)

    def test_todo_delete(self, todomvc: TodoMvcPage):
        s1 = "aaa"
        s2 = "bbb"
        todomvc.new_todo(s1)
        todomvc.new_todo(s2)
        expect(todomvc.todo_items).to_have_count(2)
        todomvc.expect_count_todo_left(2)

        todomvc.todo_item_delete(s1)
        expect(todomvc.todo_items).to_have_count(1)
        todomvc.expect_count_todo_left(1)

        todomvc.todo_item_delete(s2)
        expect(todomvc.todo_items).to_have_count(0)
        todomvc.expect_count_todo_left(0)
        expect(todomvc.footor).to_be_hidden()

    def test_new_100_todo(self, todomvc: TodoMvcPage):
        expect(todomvc.todo_items).to_have_count(0)
        todomvc.expect_count_todo_left(0)

        for i in range(100):
            todomvc.new_todo(f"todo {i}")

        expect(todomvc.todo_items).to_have_count(100)
        todomvc.expect_count_todo_left(100)

    def test_todo_toggle_all(self, todomvc: TodoMvcPage):
        n = 20
        for i in range(n):
            todomvc.new_todo(f"todo {i}")

        expect(todomvc.todo_items).to_have_count(n)
        todomvc.expect_count_todo_left(n)

        todomvc.toggle_all_button.click(force=True)
        expect(todomvc.todo_items).to_have_count(n)
        todomvc.expect_count_todo_left(0)

        todomvc.toggle_all_button.click(force=True)
        expect(todomvc.todo_items).to_have_count(n)
        todomvc.expect_count_todo_left(n)

    def test_clear_completed(self, todomvc: TodoMvcPage):
        for i in range(20):
            todomvc.new_todo(f"todo {i}s")

        expect(todomvc.todo_items).to_have_count(20)
        todomvc.expect_count_todo_left(20)

        for i in range(15):
            todomvc.todo_item_set_checked(f"todo {i}s")

        expect(todomvc.todo_items).to_have_count(20)
        todomvc.expect_count_todo_left(5)

        todomvc.clear_completed_button.click()
        expect(todomvc.todo_items).to_have_count(5)
        todomvc.expect_count_todo_left(5)

    def test_view_todos(self, todomvc: TodoMvcPage):
        n1 = 20
        n2 = 14
        for i in range(n1):
            todomvc.new_todo(f"todo {i}s")

        todomvc.view_all_link.click()

        for i in range(n2):
            todomvc.todo_item_set_checked(f"todo {i}s")

        expect(todomvc.todo_items).to_have_count(n1)
        expect(todomvc.completed_todo_items).to_have_count(n2)
        expect(todomvc.active_todo_items).to_have_count(n1 - n2)
        todomvc.expect_count_todo_left(n1 - n2)
        expect(todomvc.visible_todo_items).to_have_count(n1)

        todomvc.view_active_link.click()
        expect(todomvc.todo_items).to_have_count(n1)
        todomvc.expect_count_todo_left(n1 - n2)
        expect(todomvc.visible_todo_items).to_have_count(n1 - n2)

        todomvc.view_completed_link.click()
        expect(todomvc.todo_items).to_have_count(n1)
        todomvc.expect_count_todo_left(n1 - n2)
        expect(todomvc.visible_todo_items).to_have_count(n2)

        todomvc.view_all_link.click()
        expect(todomvc.todo_items).to_have_count(n1)
        expect(todomvc.completed_todo_items).to_have_count(n2)
        expect(todomvc.active_todo_items).to_have_count(n1 - n2)
        todomvc.expect_count_todo_left(n1 - n2)
        expect(todomvc.visible_todo_items).to_have_count(n1)
