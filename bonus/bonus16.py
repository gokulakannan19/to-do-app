import PySimpleGUI as sg
from zip_creator import compress_files


label1 = sg.Text("Select files to compress")
input_box1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select Destination Folder")
input_box2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(text_color="green", key="output")

window = sg.Window(title="Compressor", layout=[
    [label1, input_box1, choose_button1],
    [label2, input_box2, choose_button2],
    [compress_button, output_label-[[[[[[[[[]]]]]]]]]]
])

while True:
    event, values = window.read()
    files = values["files"].split(";")
    destination_folder = values["folder"]
    compress_files(files, destination_folder)
    window["output"].update(value="Compression Completed")

window.close()