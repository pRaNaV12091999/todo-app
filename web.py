import streamlit as st
from modules import functions

todos = functions.get_todos()

st.title("my todo list")
st.subheader("this is my todo app ")
st.write("This app is there to increase your productivity")
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")
