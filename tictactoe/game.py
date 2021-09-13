class TicTacToe:
    def __init__(self):
        self.board = ['' for _ in range(9)] 
        self.current_winner = none #keep track of winner


    def print_board(self):
        #to get the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

        @staticmethod
        def print_board_nums():
            #tells us the corresponding number to box placement
            number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
            for row in number_board:
                print('|' + '|'.join(row) + ' |')

        def avaliable_moves(self):
            return = [i for i, spot in enumerate(self.board) if spot == ' ']

            

        def empty_squares(self):
            return ' ' in self.board

        def num_empty_sqaures(self):
            return self.board.count(' ')
            

    def play(game, x_player, o_player, print_game=True):
        if print_game:
            game.print_board_nums()

        letter = 'X' #starting letter
        # iterate while have empty spaces

        while game.empty_squares():
