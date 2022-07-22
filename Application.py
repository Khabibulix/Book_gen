from tkinter import Tk, Button, Label, Frame, Text
from Book_Chooser import Book_Chooser, url

bc = Book_Chooser()

class Application(Tk):
    def __init__(self):
        super().__init__()

        #Bottom frame
        bottom_container = Frame(self, width=700, height=300, borderwidth=5, relief="groove")
        bottom_container.place(x=0, y=110)

        text_for_result = Text(bottom_container, height=1, width=86)
        text_for_result.pack(expand=True)
        text_for_result.config(state='normal')


        text_box_for_url = Text(bottom_container, height=1, width=86)
        text_box_for_url.pack(expand=True)
        text_box_for_url.config(state='disabled')

        text_box_for_informations = Text(bottom_container,height=16,width=86)
        text_box_for_informations.pack(expand=True)
        text_box_for_informations.insert("end","Contenu des infos ici")
        text_box_for_informations.config(state='disabled')

        # Top Frame
        top_container = Frame(self, width=700, height=100, borderwidth=5, relief="groove")
        top_container.place(x=0, y=0)

        label = Label(top_container, text="Let's randomize the next book I'll read -->")
        label.place(x=180, y=25)

        button = Button(top_container, text="Generate!",fg="black", bg="lightblue")
        button.place(x=420, y=23)

        button_delete = Button(top_container, text="Delete!", fg="black", bg="lightblue")
        button_delete.place(x=500, y=23)

        #Keybindings
        button.bind('<Button-1>', lambda event: text_for_result.insert("end", bc.choosing_book(), print(url)))
        button_delete.bind('<Button-1>', lambda event: text_for_result.delete("1.0", "end"))

        self.geometry("700x400")
        self.title("Book Randomizer")
        self.resizable(False,False)