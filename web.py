import streamlit as st
import functions

todos = functions.read_text()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if todo not in todos:
        todos.append(todo)
        functions.write_text(todos)
        st.session_state["new_todo"] = ""
    else:
        st.error("Todo already exists")


st.title("Todo App")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"checkbox_{index}")
    if checkbox:
        print(f"checkbox {index}")
        todos.pop(index)
        functions.write_text(todos)
        del st.session_state[f"checkbox_{index}"]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


