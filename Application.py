from tkinter import Tk, Button, Label, Frame, Text
from Book_Chooser import Book_Chooser, book_choosed

bc = Book_Chooser()
book_choosed = str(bc.choosing_book())

class Application(Tk):
    def __init__(self):
        super().__init__()

        #Top Frame
        top_container = Frame(self, width=700, height=100, borderwidth=5, relief="groove")
        top_container.place(x=0,y=0)

        label = Label(top_container, text="Let's randomize the next book I'll read -->")
        label.place(x=180, y=25)

        button = Button(top_container, text="Push me!", command=bc.choosing_book, fg="black", bg="lightblue")
        button.place(x=420, y=23)

        #Bottom frame
        bottom_container = Frame(self, width=700, height=300, borderwidth=5, relief="groove")
        bottom_container.place(x=0, y=110)

        text_for_result = Text(bottom_container, height=1, width=86)
        text_for_result.pack(expand=True)
        text_for_result.insert("end", book_choosed)
        text_for_result.config(state='disabled')

        text_box_for_url = Text(bottom_container, height=1, width=86)
        text_box_for_url.pack(expand=True)
        text_box_for_url.insert("end", "URL result here")
        text_box_for_url.config(state='disabled')

        text_box_for_informations = Text(bottom_container,height=16,width=86)
        text_box_for_informations.pack(expand=True)
        text_box_for_informations.insert("end","Contenu des infos ici")
        text_box_for_informations.config(state='disabled')

        self.geometry("700x400")
        self.title("Book Randomizer")
        self.resizable(False,False)