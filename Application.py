from tkinter import Tk, Button, Label
from Book_Chooser import Book_Chooser

bc = Book_Chooser()

class Application(Tk):
    def __init__(self):
        super().__init__()

        label = Label(self, text="Let's random the next book I'll read!")
        label.pack()

        button = Button(self, text="Push me!", command=bc.choosing_book)
        button.pack()

        self.geometry("300x200")
        self.title("Book Randomizer")