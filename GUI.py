import Functions as f
import PySimpleGUI as p

label = p.Text("Type in a To-Do")
input_box = p.InputText(tooltip="Enter a to do", key='todo')
add_button = p.Button("Add")
edit_button = p.Button("Edit")
complete_button = p.Button("Complete")
exit_button = p.Button("Exit")
list_box = p.Listbox(values=f.get_todos(), key='todos',
                     enable_events=True, size=[45, 10])
window = p.Window('To-Do-App',
                  layout=[[label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]],
                  font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = f.get_todos()
            new_todo = values['todo']
            todos.append(new_todo + "\n")
            f.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = f.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            f.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = f.get_todos()
            todos.remove(todo_to_complete)
            f.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case p.WIN_CLOSED:
            break
window.close()