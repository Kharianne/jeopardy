from renderer import make_jeopardy
import tkinter as tk
from tkinter import filedialog


class MainApplication:

    def __init__(self, parent):
        self.parent = parent
        self.file_path = None

        # Selected file
        self.path_label = tk.Label(text="No file")
        self.path_label.grid(row=0, column=3)
        self.message = tk.Label(text="")
        self.path_label.grid(row=0, column=3)

        # File selection button
        self.file_selection_b = tk.Button(self.parent, text='Choose your file',
                                          command=self.get_file_name)
        self.file_selection_b.grid(row=1, column=3)

        # Make jeopardy button
        self.jeopardy_b = tk.Button(self.parent, text='Make jeopardy',
                                    command=lambda: make_jeopardy(self.file_path))
        self.jeopardy_b.grid(row=2, column=3)

    def get_file_name(self):
        self.file_path = tk.filedialog.askopenfilename(title="Select your file",
                                                       filetypes=(("csv files",
                                                                 "*.csv"),
                                                                ("all files",
                                                                 "*.*")))
        self.path_label.configure(text=self.file_path)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('300x300')
    MainApplication(root)
    root.mainloop()
