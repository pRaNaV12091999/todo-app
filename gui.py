
from modules import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("DarkBlue")

clock =sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
layout = [[clock], [label], [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
window = sg.Window("My to-do app",
                   layout=layout,
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=250)
    window['clock'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))
    print(event)
    print(values)
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo']+'\n'
        todos.append(new_todo)
        functions.write_todos(todos)
    if event == "Edit":
        try:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Please select an item first", font=("Helvetica", 10))

    if event == "Complete":
        try:
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todos'].update(value="")
        except IndexError:
            sg.popup("Please select an item first", font=("Helvetica", 10))

    if event == "Exit":
        break

    if event == 'todos':
        window['todo'].update(value=values['todos'][0])

    if event == sg.WIN_CLOSED:
        break

window.close()
