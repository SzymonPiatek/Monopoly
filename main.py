import pygame
import sys
import tkinter as tk


class Monopoly(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Monopoly")
        self.geometry("800x800")


    def crete_board(self):
        pass



if __name__ == "__main__":
    app = Monopoly()
    app.mainloop()

