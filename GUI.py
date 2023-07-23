import Functions as f
import PySimpleGUI as p

label = p.Text("Type in a To-Do")
input_box = p.InputText(tooltip="Enter a to do")
add_button = p.Button("Add")
window = p.Window('To-Do-App', layout=[[label], [input_box, add_button]])
window.read()
window.close()