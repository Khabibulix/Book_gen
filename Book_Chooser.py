from data import next_books
import random
import requests
from bs4 import BeautifulSoup


book_choosed = ""
url = ""
infos = ""

class Book_Chooser:
    #
    # def extract_mood(self):
    #     """
    #     List comprehension to get all the moods in data.py
    #     :return: moodlist converted to string
    #     """
    #     mood_list = []
    #     for i in next_books:
    #         if i["mood"] not in mood_list:
    #             mood_list.append(i["mood"])
    #     return (",").join(mood_list)
    #
    # def choosing_mood_if_user_consentment_or_print_a_random_book(self):
    #     """
    #     The user  inputs a mood which will be used to choose a book later
    #     :return: mood which is a string
    #     """
    #     yes_or_no = input("Voulez-vous choisir selon une humeur? \t oui/non\n")
    #     if yes_or_no.lower() == "oui":
    #         print("Humeurs disponibles:", self.extract_mood())
    #         while True:
    #             mood = input("De quelle humeur es-tu en ce moment ? ")
    #             if mood.isalpha():
    #                 if mood in self.extract_mood():
    #                     return mood
    #                 else:
    #                     print("Cette humeur n'est pas valide")
    #                     continue
    #             else:
    #                 print("Veuillez n\'entrer que des lettres")
    #     return -1

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
        #mood = self.choosing_mood_if_user_consentment_or_print_a_random_book()
        # if mood != -1:
        #     next_books_sorted = [x for x in next_books if x["mood"] == mood]
        #     item_choosed = random.choice(next_books_sorted)
        #     print("\nDans ce cas, je te conseille:",item_choosed["titre"], "écrit par", item_choosed["auteur"])
        # else:
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


