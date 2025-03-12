# Short Description:

Merges content of all text files in the target folder, including child directories, into a single file.

# File Merger Tool

The File Merger Tool is a Python-based graphical user interface (GUI) application that merges the contents of all text files within
a specified directory into a single output file. For each file merged, the tool writes its relative path at the beginning of its
content in the output file, followed by a separator line.

![image](https://github.com/user-attachments/assets/85869d50-ebc2-407b-a277-047a1bc1c906)

## Features

- **Recursive Search**: Merges text files from the selected directory and all its subdirectories.
- **GUI Based**: Easy-to-use graphical interface for selecting directories and specifying the output file.
- **Automatic File Opening**: Automatically opens the merged output file with the default system application for `.txt` files upon completion.

## Requirements

To run this tool, you need Python installed on your system. The application is compatible with Python 3.x
and uses the `tkinter` library for the GUI, which is included in standard Python installations.

## Installation

No installation is needed. Just ensure you have Python installed on your system.

## Usage

1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using a Python interpreter:

   ```bash
   python file_merger_app.py
