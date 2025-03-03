"""
An example of `python + pytest + selenium`
which implemented "**Action Bot**, **Loadable Component** and **Page Object**".
"""

import pytest

from src.todomvc_page import TodoMvcPage


@pytest.fixture
def page(chrome_driver) -> TodoMvcPage:
    driver = chrome_driver
    return TodoMvcPage(driver).get()


class TestTodoMvcPage:
    def test_new_todo(self, page: TodoMvcPage):
        assert page.todo_count() == 0
        page.new_todo("aaa")
        assert page.count_todo_items_left() == page.build_count_todo_left(1)

    def test_todo_toggle(self, page: TodoMvcPage):
        s = "aaa"
        page.new_todo(s)
        assert page.count_todo_items_left() == page.build_count_todo_left(1)

        page.toggle_todo(s)
        assert page.count_todo_items_left() == page.build_count_todo_left(0)

        page.toggle_todo(s)
        assert page.count_todo_items_left() == page.build_count_todo_left(1)

    def test_todo_delete(self, page: TodoMvcPage):
        s1 = "aaa"
        s2 = "bbb"
        page.new_todo(s1)
        page.new_todo(s2)
        assert page.count_todo_items_left() == page.build_count_todo_left(2)

        page.delete_todo(s1)
        assert page.count_todo_items_left() == page.build_count_todo_left(1)

        page.delete_todo(s2)
        assert page.todo_count() == 0

    def test_new_100_todo(self, page: TodoMvcPage):
        for i in range(100):
            s = f"ToDo{i}"
            page.new_todo(s)
        assert page.count_todo_items_left() == page.build_count_todo_left(100)

    def test_toggle_all_todo(self, page: TodoMvcPage):
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

    def test_clear_completed_todo(self, page: TodoMvcPage):
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

    def test_view_todo(self, page: TodoMvcPage):
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
