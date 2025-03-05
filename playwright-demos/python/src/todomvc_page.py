from playwright.sync_api import Page, expect


class TodoMvcPage:
    url = "https://todomvc.com/examples/web-components/dist/"

    def __init__(self, page: Page):
        self.page = page
        self.new_todo_input = self.page.get_by_role("textbox", name="Enter a new todo.")

        self.footor = self.page.locator("footer.bottombar")
        self.count_todo_left_label = self.page.locator("div.todo-status")

        self.todo_items = self.page.locator("ul.todo-list > todo-item")
        self.active_todo_items = self.page.locator('ul.todo-list > todo-item[item-completed="false"]')
        self.completed_todo_items = self.page.locator('ul.todo-list > todo-item[item-completed="true"]')
        self.visible_todo_items = self.page.locator('ul.todo-list > todo-item[style="display: block;"]')

        self.filter_all_link = self.page.get_by_role("link", name="All")
        self.filter_active_link = self.page.get_by_role("link", name="Active")
        self.filter_completed_link = self.page.get_by_role("link", name="Completed")

        self.toggle_all_button = self.page.locator("input.toggle-all-input")
        self.clear_completed_button = self.page.locator("button#clear-completed")

    def get(self):
        self.page.goto(self.url)
        return self

    def build_count_todo_left(self, count: int) -> str:
        if count == 1:
            return "1 item left!"
        else:
            return f"{count} items left!"

    def todo_item_locator(self, s: str):
        return self.todo_items.filter(has_text=s)

    def set_todo_item_checked(self, s: str, checked: bool = True):
        return self.todo_item_locator(s).get_by_role("checkbox").set_checked(checked)

    def delete_todo_item(self, s: str) -> None:
        todoitem = self.todo_item_locator(s)
        todoitem.hover()
        todoitem.get_by_role("button").click()

    def new_todo(self, todo_text) -> None:
        self.new_todo_input.fill(todo_text)
        self.new_todo_input.press("Enter")

    def toggle_all_todo_items(self) -> None:
        self.toggle_all_button.click(force=True)

    def clear_completed_todo_items(self) -> None:
        self.clear_completed_button.click()

    def expect_count_todo_left(self, count) -> None:
        count_todo_left = self.build_count_todo_left(count)
        expect(self.count_todo_left_label).to_have_text(count_todo_left)

    def filter_all(self):
        self.filter_all_link.click()

    def filter_completed(self):
        self.filter_completed_link.click()

    def filter_active(self):
        self.filter_active_link.click()
