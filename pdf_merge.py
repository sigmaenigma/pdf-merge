import PySimpleGUI as sg
from PyPDF2 import PdfMerger
import os

""" I wrote this Python GUI to quickly merge a file with several PDFs """

""" Apache License, Version 2.0 """

# Define the layout of the GUI
layout = [
    [sg.Text('Select multiple PDF files to merge. You will need to highlight them using the SHIFT button:')],
    [sg.Input(key='-FILES-', enable_events=True, visible=False), sg.FilesBrowse()],
    [sg.Listbox(values=[], size=(50, 6), key='-LISTBOX-')],
    [sg.Text('Output file name:')],
    [sg.Input(key='-OUTPUT-', enable_events=True), sg.FileSaveAs()],
    [sg.Button('Merge'), sg.Button('Cancel'), sg.Button('Close')],
    [sg.Text('Author: Adrian Sanabria-Diaz')],
]

# Create the window
window = sg.Window('PDF Merger', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel' or event == 'Close':
        break
    elif event == '-FILES-':
        pdfs = values['-FILES-'].split(';')
        window['-LISTBOX-'].update(values=pdfs)
    elif event == 'Merge':
        pdfs = values['-FILES-'].split(';')
        output_file = values['-OUTPUT-']
        try:
            for pdf in pdfs:
                if os.path.exists(pdf):
                    continue
                else:
                    sg.popup(f"{pdf} does not exist.")
                    break
            merger = PdfMerger()
            for pdf in pdfs:
                merger.append(pdf)
            merger.write(output_file)
            merger.close()
            sg.popup(f"PDFs merged successfully into {output_file}")
        except Exception as e:
            sg.popup(f'Issue merging pdfs: {e}')

# Close the window
window.close()
