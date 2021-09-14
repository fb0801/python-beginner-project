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

        def winner(self, square, letter):
            #winner if 3 in row, must check all possibilities
            row_ind = square // 3
            row = self.board[row_ind*3 : (row_ind + 1) * 3]
            if all([spot == letter for spot in row]):
                return True

        
            #check column
            col_ind = square % 3
            column = [self.board[col_ind+i*3] for i in range(3)]
            if all([spot == letter for spot in column]):
                return True

            #check diagonals
            if square % 2 ==0:
                diagonal1 = [self.board[i] for i in [0,4,8]]# L - R diagonal
                if all([spot == letter for spot in diagonal1]):
                    return True
                diagonal2 = [self.board[i] for i in [2,4,6]]# R - L diagonal
                if all([spot == letter for spot in diagonal2]):
                    return True
                
            # if all above fail
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
                

if __name__ =='__main__':
    x_player = HumanPlayer('X')
