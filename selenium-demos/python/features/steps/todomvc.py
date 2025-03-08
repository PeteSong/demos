from behave import given, then, when
from selenium.webdriver.support import expected_conditions as EC

from src.todomvc_page import TodoMvcPage


@given("I have the TodoMVC page open")
def step_impl(context):
    context.todomvc = TodoMvcPage(context.driver).get()


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
    ele = context.todomvc.todo_item(todo_str)
    assert ele is not None


@then("I should see the following todos")
def step_impl(context):
    for row in context.table:
        todo_str = row["todo"]
        context.execute_steps(f'Then I should see the todo "{todo_str}" in the list')


@then('I should not see the todo "{todo_str}" in the list')
def step_impl(context, todo_str):
    is_visible = not EC.invisibility_of_element_located(context.todomvc.build_todo_by(todo_str))
    assert is_visible == False


@then('I should see "{x}" todo items in the list')
def step_impl(context, x):
    assert context.todomvc.todo_count() == int(x)


@then('The footer should be "{footer_visibility}"')
def step_impl(context, footer_visibility):
    footer_by = context.todomvc.footer_by
    if footer_visibility == "visible":
        ele = EC.visibility_of_element_located(footer_by)
        assert ele is not None
    elif footer_visibility == "hidden":
        is_visible = not EC.invisibility_of_element_located(footer_by)
        assert is_visible == False


@then('I should see "{x_items_left}" in the footer')
def step_impl(context, x_items_left):
    r = context.todomvc.count_todo_items_left().find(x_items_left)
    assert r != -1


@given('I "{action}" the todo "{todo_str}"')
@when('I "{action}" the todo "{todo_str}"')
def step_impl(context, action, todo_str):
    def _toggle():
        context.todomvc.toggle_todo(todo_str)

    def _delete():
        context.todomvc.delete_todo(todo_str)

    actions = {"check": _toggle, "uncheck": _toggle, "delete": _delete}
    actions[action]()


@given('I "{action}" the following todos')
@when('I "{action}" the following todos')
def step_impl(context, action):
    for row in context.table:
        todo_str = row["todo"]
        context.execute_steps(f'When I "{action}" the todo "{todo_str}"')


@then('I should see the todo "{todo_str}" "{todo_state}"')
def step_impl(context, todo_str, todo_state):
    todo_item_checkbox = context.todomvc.todo_item_checkbox(todo_str)
    is_checked = todo_item_checkbox.is_selected()
    if todo_state == "checked":
        assert is_checked == True
    elif todo_state == "unchecked":
        assert is_checked == False


@then('I should see all todo items "{todo_state}"')
def step_impl(context, todo_state):
    for todo_item in context.todomvc.todo_items():
        todo_item_checkbox = context.todomvc.todo_item_checkbox(todo_item.text)
        is_checked = todo_item_checkbox.is_selected()
        if todo_state == "checked":
            assert is_checked == True
        else:
            assert is_checked == False


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
