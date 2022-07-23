from data import next_books
import random
import requests
from bs4 import BeautifulSoup
import mechanize

item_choosed_backup = ""
infos = ""

class Book_Chooser:

    def choosing_from_list(self):
        """
        Chooses a book from data list
        :return: item_choosed_backup
        """
        global item_choosed_backup
        item_choosed_backup = random.choice(next_books)
        return item_choosed_backup

    def choosing_book_and_preparing_for_output(self):
        """
        Main function that calls all the others
        :return: book_choosed which is a data humanly readable for output
        """
        self.choosing_from_list()
        global item_choosed_backup
        book_choosed = str(item_choosed_backup["titre"]), "par", str(item_choosed_backup["auteur"])
        return (" ").join(book_choosed)

    def printing_price_informations_about_book(self):
        """
        We want to crawl the internet to find informations about the book chosen, his price for example
        :return: url of a price comparator
        """
        global item_choosed_backup
        repr_title = (" ").join([i for i in item_choosed_backup["titre"].split(" ") if len(i) > 3])
        r = requests.get("https://www.chasse-aux-livres.fr/search?query="+ repr_title +" "+ item_choosed_backup["auteur"]+"&catalog=fr")
        soup = BeautifulSoup(r.text, "html.parser")
        return r.url

    def printing_summary_informations_about_book(self):
        """
        We want to crawl the internet to find the summary of the book
        :return: summary
        """
        global item_choosed_backup
        repr_title = (" ").join([i for i in item_choosed_backup["titre"].split(" ") if len(i) > 3])
        r = requests.get("https://fr.wikipedia.org/w/index.php?search="+ repr_title + "&title=Sp%C3%A9cial%3ARecherche&ns0=1")
        soup = BeautifulSoup(r.text, "html.parser")
        print(soup)


