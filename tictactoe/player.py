#modules to use
import math
import random


class player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter


        def get_move(self, game):
            pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        square = random.choice(game.avalibale_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, game):
        super().__init__(letter)


    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-9):')
            ''' check correct value and if the spot uses wants is taken or
            avaliable
            '''
            try:
                val = int(square)
                if val not in game.avaliable_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. try again.')

        return val
