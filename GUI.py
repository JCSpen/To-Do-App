import Functions as f
import PySimpleGUI as p

label = p.Text("Type in a To-Do")
input_box = p.InputText(tooltip="Enter a to do", key='todo')
add_button = p.Button("Add")
window = p.Window('To-Do-App',
                  layout=[[label], [input_box, add_button]],
                  font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = f.get_todos()
            new_todo = values['todo']
            todos.append(new_todo + "\n")
            f.write_todos(todos)
        case p.WIN_CLOSED:
            break
window.close()