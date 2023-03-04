
from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My to-do app",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo']+'\n'
        todos.append(new_todo)
        functions.write_todos(todos)
    if event == sg.WIN_CLOSED:
        break

window.close()
