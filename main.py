import tkinter as tk
from game import *
from controller import *
from interface import * 

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Space Trader")
        self.geometry("1600x680")
        self.call('tk','scaling', 2)

        game = Game("Test Player","Test Ship")
        view = Window(self)
        controller = Controller(game, view)
        view.set_controller(controller)

if __name__ == "__main__":
    app = App()
    app.mainloop()