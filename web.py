import streamlit as st
from modules import functions


def add_todo():
    todo = st.session_state["new_todo"]+'\n'
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()
st.title("my todo list")
st.subheader("this is my todo app ")
st.write("This app is there to increase your productivity")
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",on_change=add_todo,key='new_todo')

print(st.session_state)