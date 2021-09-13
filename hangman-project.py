import random
from words import words


def get_valid_word(words):
    word = random.choice(words)#randomly choose from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

        return word

def hangman():
    word=get_valid_word(words)
    word_letters = set(word)#letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters= set() #what user has guessed

    #get user input
    while len(word_letters) > 0:
        #letters used
        #' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(' you have used these letters: ', ' '.join(used_letters))

            
        #current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '. join(word_list))


        user_letter = input('Guess a letter: ').upper()
        if  user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            elif user_letter in used letters:
                print("Already used that word")

user_input =input("Type something: ")
print(user_input)
