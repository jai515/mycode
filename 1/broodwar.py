#!/usr/bin/env python3
import random

#question bank
questions = {"Power overwhelming!": "Archon",
             "Carrier has arrived.": "Carrier",
            "It is a good day to die.": "Corsair",
             "Adun Toridas.": "Dark Templar",
             "I have returned.": "Dragoon",
             "All crews reporting.":"Battlecruiser",
             "Need a light?":"Firebat",
             "Somebody call for an exterminator?": "Ghost",
             "Ready to roll out!":"Siege tank",
             "*Screeching sound with wings*":"Mutalisk",
             "*Hissing zombie sound?*": "Hydralisk",
             "*Kind of sounds like a velociraptor*": "Zergling",
             "Go ahead TACCOM.": "Goliath",
             "In the pipe, five by five.":"Dropship",
             "*Probably like what a mutant mammoth sounds like*": "Ultralisk"}

"""
Given a question and answer prompt user
"""
def questionPrompt(question, answer):
    #number of guesses user has
    guesses = 2

    #while user has guesses remaining ask question
    while guesses != 0:
        #give quote and prompt for input
        input_answer = input(f"What unit says: {question} \nYour answer:  ").strip().lower()

        #check if correct, return 1 to increment score
        if input_answer == answer.lower():
            print("Correct!")
            return 1
        #check if gg called, return -1 to end game
        elif input_answer == "gg":
            return -1
        # if not correct and not gg decrement guesses
        else:
            guesses -= 1
            # if not out of guesses
            if guesses != 0:
                print(f"Incorrect, guesses remaining: {guesses}.")
            # if out of guesses give correct answer and return 0
            else:
                print(f"The correct answer was {answer}.")
                return 0

#def game loop
def play(question_bank):
    #question counters
    totalQuestions = 0
    correct = 0

    #intro text
    print("Name the correct Starcraft unit given the following quotes.\nYou have 2 guesses per quote.\nTo end the game type: gg.")

    #while question remain call questionPrompt
    while len(question_bank) != 0:
        question = random.choice(list(question_bank.keys()))
        totalQuestions += 1
        response = questionPrompt(question, question_bank[question])

        # if gg called
        if response == -1:
            break
        # if not gg, increment correct by questionPrompt return value
        else:
            correct += response

        # remove asked question from question bank
        question_bank.pop(question)

    # game over response
    print(f"You got {correct} out of {totalQuestions} quotes right!")

play(questions)
