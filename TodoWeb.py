import streamlit as st
import Functions

todos = Functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    Functions.write_todos(todos)
    st.session_state['new_todo']=''


st.title("To Do's List")
st.subheader('For work productivity and efficiency!')
st.text('This will be fun!')
st.text_input('Add a new ToDo', placeholder="Type a new todo here", key='new_todo', on_change=add_todo)

for index, todo in enumerate(todos):
    checkboxes = st.checkbox(todo, key=todo)
    if checkboxes:
        completed = todos.pop(index)
        Functions.write_todos(todos)
        Functions.done_todos(completed)
        del st.session_state[todo]
        st.rerun()






