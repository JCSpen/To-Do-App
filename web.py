import streamlit as st
import Functions as f

todos = f.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)


st.title("My To Do App")
st.subheader("This is my do to app!")
st.write("This app boosts productivity!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label="", placeholder="Add new to do....",
              on_change=add_todo, key="new_todo")
