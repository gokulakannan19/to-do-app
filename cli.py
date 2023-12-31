import functions
import time

now = time.strftime("%b %d %Y, %H:%M:%S")
print("The time is below")
print(now)
while True:
    user_action = input("Type add, show/display, edit, complete or exit : ").strip()

    if user_action.lower().startswith("add"):
        todo = user_action[4:] + "\n"
        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(filepath="files/todos.txt", todo_args=todos)

    elif user_action.lower().startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index+1} - {item}")

    elif user_action.lower().startswith("edit"):
        try:
            number = int(user_action[4:])

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ") + "\n"
            todos[number-1] = new_todo

            functions.write_todos(todo_args=todos)

        except ValueError:
            print("The command is not valid. You should enter the number of the todo to edit")
            continue

    elif user_action.lower().startswith("complete"):
        try:
            todos = functions.get_todos()

            number = int(user_action[9:]) - 1
            removed_todo = todos[number].strip("\n")
            todos.pop(number)

            functions.write_todos(todo_args=todos)

            print(f"{removed_todo} was removed from the list")
        except IndexError:
            print("The item is not in the todo to remove.")
            continue

    elif user_action.lower().startswith("exit"):
        break

    else:
        print("Command is not valid")
        user_action = input("Type add, show/display, edit, complete or exit : ").strip()

print("Bye")
