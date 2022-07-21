from tkinter import Tk, Button, Label, Frame, Text
from Book_Chooser import Book_Chooser

bc = Book_Chooser()

class Application(Tk):
    def __init__(self):
        super().__init__()

        #Top Frame
        top_container = Frame(self, width=500, height=100, borderwidth=5, relief="groove")
        top_container.place(x=0,y=0)
        label = Label(top_container, text="Let's randomize the next book I'll read -->")
        label.place(x=80, y=25)
        button = Button(top_container, text="Push me!", command=bc.choosing_book, fg="black", bg="lightblue")
        button.place(x=320, y=23)

        #Bottom frame
        bottom_container = Frame(self, width=500, height=300, borderwidth=5, relief="groove")
        bottom_container.place(x=0, y=100)
        # text_box = Text(self,height=12,width=40)
        # text_box.pack(expand=True)
        # text_box.insert("end","Yup")
        # text_box.config(state='disabled')

        self.geometry("500x400")
        self.title("Book Randomizer")
        self.resizable(False,False)