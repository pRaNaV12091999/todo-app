from modules import functions
import time

print("enter exit to stop")
prompt = "Type add or show or edit or complete or exit:"

# time function for a timestamp
now = time.strftime("%b %d, %Y %H:%M:%S")
print("IT is:", now)


while True:
    user_action = input(prompt)
    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)
        # print(todos)

        functions.write_todos(todos, 'files/todos.txt')

    elif user_action.startswith("show"):

        todos = functions.get_todos('files/todos.txt')

        for index, items in enumerate(todos):
            row = f"{index + 1}-{items}"
            print(row, end="")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()
            # print('Here is todos existing', todos)

            new_todo = input("enter the new todo:")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not Valid !")
            continue

    elif user_action.startswith("exit"):
        break
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
        except IndexError:
            print("the number of todo is invalid")
            continue
    else:
        print("command not understood")

print("end of program")
print("bye")
