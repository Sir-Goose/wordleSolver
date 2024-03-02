import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.letter_boxes = []
        for i in range(5):
            entry = ttk.Entry(self, width=2)
            entry.pack(side="left")
            self.letter_boxes.append(entry)

        self.submit_button = ttk.Button(self)
        self.submit_button["text"] = "Submit"
        self.submit_button["command"] = self.print_letters
        self.submit_button.pack(side="bottom")

    def print_letters(self):
        letters = [entry.get() for entry in self.letter_boxes]
        print(letters)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
