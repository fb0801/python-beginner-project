#modules to use
import math
import random


class player():
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
            square = input(self.letter + '\'s turn. Input move(0-8):')
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


def GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
         if len(game.avaliable_moves()) ==9:
             square = random.choice(game.avaliable_moves()) #random choose one move
         else:
             #get square based off the miximax algor
             square = self.minimax(game, self.letter)
        return square

    def minimax(self, state, player):
        max_player = self.letter #yourself
        other_player = 'O' if player == 'X' else 'X'

        #check if previous move is winner
        if state.current_winner == other_player:
            return {'position':None,
                    'score': 1 * (state.num_empty_square()+ 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)
                    }
        
        elif not state.empty_squares(): # no empty space
            return {'position': None, 'score':0}

        if player ==max_player:
            best = {'position': None, 'score': -math.inf} #each score to be larger
        else:
            best = {'position':None, 'score': -math.inf}

        for possible_move in state.avaliable_moves():
            #1 try the spot
            state.make_moves(possible_move, player)
            #2 use minimax to simulate game
            sim_score = self.minimax(state, other_player)

            #3 undo the move
            state.board = [possible_move] = ' '
            state.current_winner = None
            sim_score['position']
            
            #4 update dict
            
