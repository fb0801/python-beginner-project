def find_next_empty(puzzle):


    for r in range(9):
        for c in range(9):
            if puzzle[r][c] ==-1:
                return r,c


def is_valid(puzzle, guess, row, col):
    #see if a valid guess

    row_vals = puzzle[row]
    if guess in row_vals:
        return False


    cols_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False


    row_start = (row // 3) * 3


def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)


    if row is None:
        return True

    #to makes guesses
    for guess in range
