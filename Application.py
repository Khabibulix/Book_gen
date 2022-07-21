from tkinter import Tk, Button, Label
from Book_Chooser import Book_Chooser

bc = Book_Chooser()

class Application(Tk):
    def __init__(self):
        super().__init__()

        label = Label(self, text="Let's randomize the next book I'll read -->")
        label.place(x=80, y=25)

        button = Button(self, text="Push me!", command=bc.choosing_book)
        button.place(x=310, y=23)

        self.geometry("500x400")
        self.title("Book Randomizer")
        self.resizable(False,False)