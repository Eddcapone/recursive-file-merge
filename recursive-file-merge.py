import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, Label, Entry, Button
import subprocess

class FileMergerApp:
    def __init__(self, master):
        self.master = master
        master.title("File Merger Tool")

        # Labels and entries
        Label(master, text="Select Target Folder:").pack()
        self.folder_entry = Entry(master, width=50)
        self.folder_entry.pack(padx=10)
        Button(master, text="Browse...", command=self.browse_folder).pack(pady=5)

        Label(master, text="Define Output File Path:").pack()
        self.file_entry = Entry(master, width=50)
        self.file_entry.pack(padx=10)
        Button(master, text="Browse...", command=self.browse_file).pack(pady=5)

        # Merge button
        Button(master, text="Merge Files", command=self.start_merging).pack(pady=20)

    def browse_folder(self):
        directory = filedialog.askdirectory()
        if directory:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, directory)

    def browse_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)

    def merge_files(self, root_directory, output_file):
        try:
            with open(output_file, 'w') as outfile:
                for dirpath, _, filenames in os.walk(root_directory):
                    for filename in filenames:
                        file_path = os.path.join(dirpath, filename)
                        relative_path = os.path.relpath(file_path, start=root_directory)
                        outfile.write(f"\n{relative_path}\n")
                        outfile.write("-" * 80 + "\n")  # Trennlinie
                        with open(file_path, 'r') as infile:
                            outfile.write(infile.read() + "\n")
            self.open_file(output_file)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def open_file(self, file_path):
        try:
            if os.name == 'nt':  # For Windows
                os.startfile(file_path)
            else:  # For macOS and Linux
                opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
                subprocess.call([opener, file_path])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {str(e)}")

    def start_merging(self):
        root_directory = self.folder_entry.get()
        output_file = self.file_entry.get()
        if root_directory and output_file:
            self.merge_files(root_directory, output_file)
        else:
            messagebox.showerror("Error", "Please specify both the target folder and output file.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileMergerApp(root)
    root.mainloop()
