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

        def make_move(self, square, letter):
            #if the move is valid then it is performed
            if self.board[square] == ' ':
                self.board[square] = letter
                if self.winner(square, letter):
                    self.current_winner = letter
                return True
            return False
            

    def play(game, x_player, o_player, print_game = True):
        #shows the winner for the game or none if a draw
        if print_game:
            game.print_board_nums()

        letter = 'X' #starting letter
        # iterate while have empty spaces

        while game.empty_squares():
            #get move from the player
            if letter == 'o':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)

            #function to make the move
            if game.make_move(square, letter):
                if print_game:
                    print(letter + f' makes a move to square {square}')
                    game.print_board()
                    print('') #empty line

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    return letter

                #switch to the other letters turn
                    letter = 'O' if letter == 'X' else 'X'
                    #if letter =='X':
                    #    letter = 'O'

            if print_game:
                print('Its a tie')
                
