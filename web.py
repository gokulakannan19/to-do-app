import streamlit as st
import functions
import time

todos = functions.get_todos()

st.title("To do App")
st.subheader(time.strftime("%d-%m-%y %H:%M:%S"))

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a todo...")