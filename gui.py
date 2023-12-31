import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-do")
input_box = sg.Input(tooltip="Enter your todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window(title="My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break


window.close()
