import tkinter as tk
from tkinter import ttk

class Window:
    def __init__(self, size):
        self.root = tk.Tk()
        self.root.title("Space Trader")
        self.root.geometry("1000x800")
        self.tree = ttk.Treeview()
        self.tree.size()
        self.tree.pack()
        self.running_state = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self):
        self.running_state = True
        while self.running_state == True:
            self.redraw()

    def close(self):
        self.running_state = False