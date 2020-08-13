#!/usr/bin/env python3

import sys
#flowchart: https://i.redd.it/24fzziysunlz.jpg
# dict of questions. format "origin question": ["question being asked", "responses..."]
questions = {
    "What Sci-Fi movie should you watch?": ["What type of Sci-Fi movie?", "Hard Sci-Fi", "Space Opera", "Action", "CyberPunk"],
    "No. Start over": ["Fine.", "Hard Sci-Fi", "Space Opera", "Action", "CyberPunk"],
    "Hard Sci-Fi": ["How Hard?", "Hardest", "Kinda hard"],
    "Hardest": ["Interstellar?", "Grittier", "Cooler", "Harder!", "That's the one"],
    "Kinda hard": ["Star Trek?", "Yes, Star Trek", 'No Star Trek'],
    "Grittier": ["Children of Men", "I'll watch it", "No. Start over"],
    "Cooler": ["Gattaca", "That's the one"],
    "Harder!": ["Solaris?", "Yes that's the one", "I said Harder!", "Too hard"],
    "Too hard": ["How about...", "Matt Damon?", "George Clooney?"],
    "George Clooney?": ["Gravity"],
    "Matt Damon?": ["The Martian"],
    "I said Harder": ["2001: a space odyssey?", "Yes that's the one"],
    "2001: a space odyssey?": ["2001: a space odyssey?"],
    "Yes, Star Trek": ["Which one?", "Star Trek II: The Wrath of Khan", "Star Trek: First Contact", "Star Trek (2009)"],
    "No Star Trek": ["Ex Machina?", "That's the one", "Europa Report"],

    "Space Opera": ["Have you seen Firefly?", "Yes I have", "No I have not"],
    "No I have not": ["Firefly the tv series"],
    "Yes I have": ["Have you seen Serenity", "I am a leaf on the wind", "Not yet"],
    "Not yet": ["Serenity"],
    "I am a leaf on the wind": ["Watch me soar", "Guardians of the Galaxy", "Guardians of the Galaxy 2", "The Fifth Element"],

    "Action": ["Which category?", "Time Travel", "Humans vs. Aliens", "Questioning Reality"],
    "Time Travel": ["Choose one", "Looper", "Edge of Tomorrow", "Terminator"],
    "Humans vs. Aliens": ["Choose one", "Independence Day", "Starship Troopers", "Alien"],
    "Questioning Reality": ["Choose one", "Inception", "Total Recall", "Source Code"],

    "CyberPunk": ["Have you seen Blade Runner?", "I watched C-beams glitter in the dark near Tannhauser Gate", "Nope"],
    "Nope": ["Blade Runner"],
    "I watched C-beams glitter in the dark near Tannhauser Gate": ["Choose One", "The Matrix", "Minority Report", "Ghost in the Shell"]

             }

questionKeys = list(questions.keys())
questionBank = {}

# create a question object from the questions
class Question:

    # create the question prompt and answers
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    # prompts user receives input from user
    def prompt(self):
        if len(self.answers) == 1:
            print("You're welcome.")
            sys.exit()

        # store user response
        response = 0

        # continue to ask until valid
        while response == 0:

            # ask question
            print(self.question)

            # show answers
            for x in range(1, len(self.answers)):
                print(f"{x}.", self.answers[x])

            user_selection = input("Please select a number. \n").strip()
            if user_selection.lower().strip() == "q":
                print("Fine then, no movie for you!")
                sys.exit()

            elif user_selection.isnumeric() is True and 1 <= int(user_selection) < len(self.answers):
                response = user_selection

            else:
                print("That is not how flow charts work.")

        else:
            return response

    def ask(self):
        # format response
        response = int(self.prompt())

        # if movie selected end.
        if self.answers[response] not in questionBank:
            print("Coolio. Go watch it.")
            sys.exit()

        # if flow continues
        else:
            questionBank[self.answers[response]].ask()


def enterTheFlowtrix():
    for key in range(0, len(questionKeys)):
        currentQ = questionKeys[key]
        questionBank[currentQ] = Question(questions[currentQ][0], questions[currentQ])

    questionBank["What Sci-Fi movie should you watch?"].ask()


enterTheFlowtrix()
