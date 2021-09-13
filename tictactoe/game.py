class TicTacToe:
    def __init__(self):
        self.board = ['' for _ in range(9)] 
        self.current_winner = none #keep track of winner


    def print_board(self):
        #to get the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
