import random
from words import words


def get_valid_word(words):
    word = random.choice(words)#randomly choose from the list
    while '-' in word orr ' ' in word:
        word = random.choice(words)

        return word

def hangman():
    word=get_valid_word(words):
        word_letters = set(word)#letters in the word
        alphabet = set(string.ascii_uppercase)
        used_letters= set() #what user has guessed

        #get user input
        user_letter = input('Guess a letter: ').upper()


user_input =input("Type something: ")
print(user_input)
