from data import next_books
import random
import requests
from bs4 import BeautifulSoup


book_choosed = ""
url = ""
infos = ""

class Book_Chooser:

    def choosing_from_list(self):
        """
        Chooses a book from data list
        :return: item_choosed
        """
        item_choosed = random.choice(next_books)
        return item_choosed

    def choosing_book(self):
        """
        Main function that calls all the others
        :return: book_choosed which is a data humanly readable for output
        """
        item_choosed = self.choosing_from_list()
        book_choosed = str(item_choosed["titre"]), "par", str(item_choosed["auteur"])
        self.printing_informations_about_book(item_choosed["titre"], item_choosed["auteur"])
        return (" ").join(book_choosed)

    def printing_informations_about_book(self, title, author):
        """
        We want to crawl the internet to find informations about the book chosen, his price for example
        :return:
        """
        repr_title = (" ").join([i for i in title.split(" ") if len(i) > 3])
        r = requests.get("https://www.chasse-aux-livres.fr/search?query="+ repr_title +" "+ author+"&catalog=fr")
        soup = BeautifulSoup(r.text, "html.parser")
        return r.url


