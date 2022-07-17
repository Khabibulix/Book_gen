from data import next_books
import random

class Book_Chooser:

    def extract_mood(self):
        """
        List comprehension to get all the moods in data.py
        :return: moodlist converted to string
        """
        mood_list = []
        for i in next_books:
            if i["mood"] not in mood_list:
                mood_list.append(i["mood"])
        return (",").join(mood_list)

    def choosing_mood(self):
        """
        The user  inputs a mood which will be used to choose a book later
        :return: mood which is a string
        """
        print("Humeurs disponibles:", self.extract_mood())
        while True:
            mood = input("De quelle humeur es-tu en ce moment ? ")
            if mood.isalpha():
                if mood in self.extract_mood():
                    return mood
                else:
                    print("Cette humeur n'est pas valide")
                    continue
            else:
                print("Veuillez n\'entrer que des lettres")

    def choosing_book(self):
        """
        Main function that calls all the others
        :return: item_choosed, which is an element of the data randomly choosed
        """
        mood = self.choosing_mood()
        next_books_sorted = [x for x in next_books if x["mood"] == mood]
        item_choosed = random.choice(next_books_sorted)
        print("\nDans ce cas, je te conseille:",item_choosed["titre"], "écrit par", item_choosed["auteur"])
        return item_choosed

    #TODO Ajouter masse de données dans fichier python externe
    #TODO Générer prix selon différents sites internet puis faire moyenne

