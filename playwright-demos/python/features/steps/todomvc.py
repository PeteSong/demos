import re

from behave import given, then, when
from playwright.sync_api import expect

from src.todomvc_page import TodoMvcPage


@given("I have the TodoMVC page open")
def step_impl(context):
    context.todomvc = TodoMvcPage(context.page).get()


@given('I add a todo "{todo_str}"')
@when('I add a todo "{todo_str}"')
def step_impl(context, todo_str):
    context.todomvc.new_todo(todo_str)


@given("I add the following todos")
@when("I add the following todos")
def step_impl(context):
    for row in context.table:
        todo_str = row["todo"]
        context.execute_steps(f'Given I add a todo "{todo_str}"')


@when('I add "{x}" todo items')
@given('I add "{x}" todo items')
def step_impl(context, x):
    for _ in range(int(x)):
        todo_str = "todo-" + str(_)
        context.execute_steps(f'Given I add a todo "{todo_str}"')


@then('I should see the todo "{todo_str}" in the list')
def step_impl(context, todo_str):
    todo_item_locator = context.todomvc.todo_item_locator(todo_str)
    expect(todo_item_locator).to_be_visible()


@then("I should see the following todos")
def step_impl(context):
    for row in context.table:
        todo_str = row["todo"]
        context.execute_steps(f'Then I should see the todo "{todo_str}" in the list')


@then('I should not see the todo "{todo_str}" in the list')
def step_impl(context, todo_str):
    todo_item_locator = context.todomvc.todo_item_locator(todo_str)
    expect(todo_item_locator).to_be_hidden()


@then('I should see "{x}" todo items in the list')
def step_impl(context, x):
    expect(context.todomvc.todo_items).to_have_count(int(x))


@then('The footer should be "{footer_visibility}"')
def step_impl(context, footer_visibility):
    if footer_visibility == "visible":
        expect(context.todomvc.footor).to_be_visible()
    elif footer_visibility == "hidden":
        expect(context.todomvc.footor).to_be_hidden()


@then('I should see "{x_items_left}" in the footer')
def step_impl(context, x_items_left):
    expect(context.todomvc.footor).to_have_text(re.compile(x_items_left))


@given('I "{action}" the todo "{todo_str}"')
@when('I "{action}" the todo "{todo_str}"')
def step_impl(context, action, todo_str):
    def _check():
        context.todomvc.set_todo_item_checked(todo_str)

    def _uncheck():
        context.todomvc.set_todo_item_checked(todo_str, False)

    def _delete():
        context.todomvc.delete_todo_item(todo_str)

    actions = {"check": _check, "uncheck": _uncheck, "delete": _delete}
    actions[action]()


@given('I "{action}" the following todos')
@when('I "{action}" the following todos')
def step_impl(context, action):
    for row in context.table:
        todo_str = row["todo"]
        context.execute_steps(f'When I "{action}" the todo "{todo_str}"')


@then('I should see the todo "{todo_str}" "{todo_state}"')
def step_impl(context, todo_str, todo_state):
    todo_item_locator = context.todomvc.todo_item_locator(todo_str)
    if todo_state == "checked":
        expect(todo_item_locator.get_by_role("checkbox")).to_be_checked()
    elif todo_state == "unchecked":
        expect(todo_item_locator.get_by_role("checkbox")).to_be_checked(checked=False, indeterminate=False)


@then('I should see all todo items "{todo_state}"')
def step_impl(context, todo_state):
    for todo_item in context.todomvc.todo_items.all():
        if todo_state == "checked":
            expect(todo_item.get_by_role("checkbox")).to_be_checked()
        else:
            expect(todo_item.get_by_role("checkbox")).to_be_checked(checked=False, indeterminate=False)


@when('I click "{action}" button')
def step_impl(context, action):
    def _toggle_all():
        context.todomvc.toggle_all_todo_items()

    def _clear_completed():
        context.todomvc.clear_completed_todo_items()

    action = action.casefold()

    actions = {
        "toggle all": _toggle_all,
        "clear completed": _clear_completed,
    }
    actions[action]()


@when('I filter todo item by clicking "{filter}" filter')
def step_impl(context, filter):
    def _filter_all():
        context.todomvc.filter_all()

    def _filter_active():
        context.todomvc.filter_active()

    def _filter_completed():
        context.todomvc.filter_completed()

    filter = filter.casefold()

    filters = {
        "all": _filter_all,
        "active": _filter_active,
        "completed": _filter_completed,
    }
    filters[filter]()
