import random #allow us to use this function

#play the game

class Board:
    def __init__(self, dim_size, num_bombs):
        #track params
        self.dim_size = dim_size
        self.num_bombs = num_bombs




        self.board = self.make_new_board()

        self.dug = set()

    def make_new_board(self):
        #make a new board based on info given


        #make new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]


        #plant bomb
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.
        

def play(dim_size=10, num_bombs=10):
    #create and plant bomb
    #show user the board and ask wher to dig next
    # if dig bomb gameover
    # if not a bomb continue

    #repeat step 2-3 until no more places to dig



