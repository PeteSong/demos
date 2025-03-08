Feature: TodoMVC

    Scenario: Add a todo
        Given I have the TodoMVC page open
         When I add a todo "Buy some milk"
         Then I should see the todo "Buy some milk" in the list
          and The footer should be "visible"
          and I should see "1 item left" in the footer

    Scenario: Check a todo
        Given I have the TodoMVC page open
          and I add a todo "Buy some milk"
         When I "check" the todo "Buy some milk"
         Then I should see the todo "Buy some milk" "checked"
          and The footer should be "visible"
          and I should see "0 items left!" in the footer

    Scenario: Uncheck a todo
        Given I have the TodoMVC page open
          and I add a todo "Buy some milk"
          and I "check" the todo "Buy some milk"
         When I "uncheck" the todo "Buy some milk"
         Then I should see the todo "Buy some milk" "unchecked"
          and The footer should be "visible"
          and I should see "1 item left!" in the footer

    Scenario: Delete a todo
        Given I have the TodoMVC page open
          and I add a todo "Buy some milk"
         When I "delete" the todo "Buy some milk"
         Then I should not see the todo "Buy some milk" in the list
          and The footer should be "hidden"

    Scenario: Add multiple todos
        Given I have the TodoMVC page open
         When I add the following todos
            | todo                        |
            | Buy some milk, eggs, bread  |
            | Buy some butter, cheese, ham, bacon, sausages|
            | Buy some tea, coffee        |
            | Buy some lettuce, tomatoes, cucumber|
            | Buy some apples             |
         Then I should see the following todos
            | todo                        |
            | Buy some milk, eggs, bread  |
            | Buy some butter, cheese, ham, bacon, sausages|
            | Buy some tea, coffee        |
            | Buy some lettuce, tomatoes, cucumber|
            | Buy some apples             |
          and The footer should be "visible"
          and I should see "5 items left" in the footer

    Scenario: Add lots of todos
        Given I have the TodoMVC page open
         When I add "100" todo items
         Then I should see "100" todo items in the list
          and The footer should be "visible"
          and I should see "100 items left" in the footer

    Scenario: Toggle all todos
        Given I have the TodoMVC page open
          and I add "5" todo items
         When I click "toggle all" button
         Then I should see all todo items "checked"
          and The footer should be "visible"
          and I should see "0 items left!" in the footer
         When I click "toggle all" button
         Then I should see all todo items "unchecked"
          and The footer should be "visible"
          and I should see "5 items left!" in the footer

    Scenario: Filter todos
        Given I have the TodoMVC page open
          and I add the following todos
            | todo                        |
            | Buy some milk, eggs, bread  |
            | Buy some butter, cheese, ham, bacon, sausages|
            | Buy some tea, coffee        |
            | Buy some lettuce, tomatoes, cucumber|
            | Buy some apples             |
         When I filter todo item by clicking "All" filter
         Then I should see the following todos
            | todo                        |
            | Buy some milk, eggs, bread  |
            | Buy some butter, cheese, ham, bacon, sausages|
            | Buy some tea, coffee        |
            | Buy some lettuce, tomatoes, cucumber|
            | Buy some apples             |
          and The footer should be "visible"
          and I should see "5 items left" in the footer
        When I "check" the following todos
            | todo                        |
            | Buy some milk, eggs, bread  |
            | Buy some butter, cheese, ham, bacon, sausages|
            | Buy some tea, coffee        |
         and I filter todo item by clicking "Active" filter
         Then I should see the following todos
            | todo                        |
            | Buy some lettuce, tomatoes, cucumber|
            | Buy some apples             |
          and The footer should be "visible"
          and I should see "2 items left" in the footer
         When I filter todo item by clicking "Completed" filter
         Then I should see the following todos
            | todo                        |
            | Buy some milk, eggs, bread  |
            | Buy some butter, cheese, ham, bacon, sausages|
            | Buy some tea, coffee        |
          and The footer should be "visible"
          and I should see "2 items left" in the footer
         When I filter todo item by clicking "All" filter
         Then I should see the following todos
            | todo                        |
            | Buy some milk, eggs, bread  |
            | Buy some butter, cheese, ham, bacon, sausages|
            | Buy some tea, coffee        |
            | Buy some lettuce, tomatoes, cucumber|
            | Buy some apples             |
          and The footer should be "visible"
          and I should see "2 items left" in the footer

    Scenario: Clear completed todos
        Given I have the TodoMVC page open
          and I add the following todos
            | todo                        |
            | Buy some milk, eggs, bread  |
            | Buy some butter, cheese, ham, bacon, sausages|
            | Buy some tea, coffee        |
            | Buy some lettuce, tomatoes, cucumber|
            | Buy some apples             |
          and I "check" the following todos
            | todo                        |
            | Buy some milk, eggs, bread  |
            | Buy some butter, cheese, ham, bacon, sausages|
         When I click "clear completed" button
         Then I should see the following todos
            | todo                        |
            | Buy some tea, coffee        |
            | Buy some lettuce, tomatoes, cucumber|
            | Buy some apples             |
          and The footer should be "visible"
          and I should see "3 items left" in the footer
