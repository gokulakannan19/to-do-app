import streamlit as st
import functions
import time

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.write(time.strftime("%d-%m-%y %H:%M:%S"))

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a todo...",
              on_change=add_todo, key="new_todo")

st.session_state