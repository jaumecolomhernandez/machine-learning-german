import csv
import random
import difflib

class App:

    number_of_words = 10
    threshold = 0.8
    selected_rows = list()

    def __init__(self, db, UI):
        self.db = db
        self.UI = UI
    
    def start_game(self):
        """
        Called to start the game
        """

        #Stablish connection with the db
        conn = self.db.connect_to_db()

        #if user asks to load a new csv file
        # self.db.insert_csv()

        words = list()

        for i in range(self.number_of_words):

            #retrieve pair of words [asking, solution]
            words = self.choose_words()

            #Send to the UI the word to ask
            print(words[0])

            #wait to the user to put enter its answer
            answer = input()

            #Refactor words to compare them
            ratio=self.refactor_words(answer, words[1])

            #TO-DO: Save the ratio to the stadistics db

            if(ratio>self.threshold):

                #Tell the UI to update the screen with a succesful answer
                print("Correct!")
            else:
                #Tell the UI to update the screen with a wrong answer
                print("Oops, that's incorrect!")

    def ask_user_number(self):
        """
        Called to know how many words the user wants to practice
        """
        print("How many words do you want to practice?")
        return int(input())

    def choose_words(self):
        """
        returns two strings containing the [word to ask, solution]
        """
        row_num=random.randrange(1,self.db.length_db()-1)
        while(row_num in self.selected_rows):
            row_num=random.randrange(1,self.db.length_db()-1)
        self.selected_rows.append(row_num)
        
        row_words = list(self.db.get_row(row_num))
        row_words.pop(0)
        random.shuffle(row_words)
        return row_words


    def refactor_words(self, answer, correct):
        """
        Called to eliminate uppercase, quotation marks, spaces, dots...
        and calculate the similarity ratio
        """
        #both lower case
        answer=answer.lower()
        correct=correct.lower()

        #eliminate dots
        answer=answer.replace('.','')
        correct=correct.replace('.','')

        #eliminate quotation marks
        answer=answer.replace("\'",'')
        correct=correct.replace("\'", '')

        #remove spaces
        answer=answer.replace(" ", "")
        correct=correct.replace(" ","")

        #remove ? and !
        answer=answer.replace("?", "")
        correct=correct.replace("?", "")
        answer=answer.replace("!", "")
        correct=correct.replace("!", "")


        #Calculate ratio
        print("words refactored: "+answer+" "+correct)
        
        if(";" in correct):
            print("entro por aquí")
            correct_list = list()
            correct_list = correct.split(";")
            ratio1 = difflib.SequenceMatcher(None, correct_list[0],answer).ratio()
            ratio2 = difflib.SequenceMatcher(None, correct_list[1],answer).ratio()
            return(max(ratio1, ratio2))
        
        else:
            return(difflib.SequenceMatcher(None, correct,answer).ratio())