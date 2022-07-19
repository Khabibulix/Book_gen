import random
from data import *
from Book_Chooser import Book_Chooser
from tkinter import Tk, Button, Label

if __name__ == "__main__":
	bc = Book_Chooser()

	window = Tk()
	label = Label(window, text="Hello Tk")
	label.pack()

	button = Button(window, text="Push me!", command = bc.choosing_book)
	button.pack()

	window.mainloop()