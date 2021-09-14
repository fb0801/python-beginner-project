import random #allow us to use this function

#play the game

class Board:
    def __init__(self, dim_size, num_bombs):
        #track params
        self.dim_size = dim_size
        self.num_bombs = num_bombs




        self.board = self.make_new_board()
        self.assign_values_to_board()

        self.dug = set()

    def make_new_board(self):
        #make a new board based on info given
         board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ..., None],
        #  [None, None, ..., None],
        #  [...                  ],
        #  [None, None, ..., None]]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # return a random integer N such that a <= N <= b
            row = loc // self.dim_size  # we want the number of times dim_size goes into loc to tell us what row to look at
            col = loc % self.dim_size  

            if board[row][col] == '*':
                # this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*' # plant the bomb
            bombs_planted += 1

        return board



    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] =='*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1,row+1)+1):
            for c in range(max(0,col-1), min(self.dim_size - 1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neightboring_bombs +=1

        return num_neighboring_bombs
        

    def dig(self, row, col):
        #dig at the location
        #hit bomb means end of game

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row-1), min(self.dim_size-1,row+1)+1):
            for c in range(max(0,col-1), min(self.dim_size - 1, col+1)+1):
                if (r,c) in self.dug:
                    continue #dont dig where you already have
                self.dig(r,c)
        return True

    def __str__(self):
        #print the board for the player
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for col in range(self.dim_size):
            if (row, )
        

def play(dim_size=10, num_bombs=10):
    #create and plant bomb
    board = Board(dim_size, num_bombs)
    #show user the board and ask wher to dig next
    # if dig bomb gameover
    # if not a bomb continue

    #repeat step 2-3 until no more places to dig



