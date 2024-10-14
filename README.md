# PDF Merger

This Python GUI application allows users to quickly merge multiple PDF files into a single PDF. The application is built using PySimpleGUI for the graphical interface and PyPDF2 for handling PDF merging.

## Features

- Select multiple PDF files to merge.
- Specify the output file name and location.
- Simple and intuitive user interface.
- Error handling for non-existent files.

## Requirements

- Python 3.x
- PySimpleGUI
- PyPDF2

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd pdf-merger
    ```

2. **Set up a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```bash
    python pdf_merger.py
    ```

2. **Select multiple PDF files to merge:**
    - Click on the "Browse" button and select the PDF files you want to merge. You can select multiple files by holding the SHIFT key.

3. **Specify the output file name:**
    - Enter the desired name and location for the merged PDF file.

4. **Merge the PDFs:**
    - Click on the "Merge" button to merge the selected PDF files into the specified output file.

## Code Overview

```python
import PySimpleGUI as sg
from PyPDF2 import PdfMerger
import os

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
```
## Author

Adrian Sanabria-Diaz
