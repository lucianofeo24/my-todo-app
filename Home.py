import streamlit as st
import functions as ft

todos = ft.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    ft.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")

for i, v in enumerate(todos):
    checkbox = st.checkbox(v, key=i)
    if checkbox:
        todos.pop(i)
        ft.write_todos(todos)
        del st.session_state[i]
        st.rerun()

st.text_input("scrivi", on_change=add_todo, key='new_todo')