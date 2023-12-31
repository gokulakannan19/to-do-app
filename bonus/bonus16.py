import PySimpleGUI as sg

label1 = sg.Text("Select files to compress")
input_box1 = sg.Input()
choose_button1 = sg.Button("Choose")

label2 = sg.Text("Select Destination Folder")
input_box2 = sg.Input()
choose_button2 = sg.Button("Choose")

compress_button = sg.Button("Compress")

window = sg.Window(title="Compressor", layout=[
    [label1, input_box1, choose_button1],
    [label2, input_box2, choose_button2],
    [compress_button]
])
window.read()
window.close()