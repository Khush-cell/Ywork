def solveSudoku(board):
    def is_valid(r, c, ch):
        # check row
        for i in range(9):
            if board[r][i] == ch:
                return False
        # check column
        for i in range(9):
            if board[i][c] == ch:
                return False
        # check 3x3 subgrid
        start_r, start_c = 3 * (r // 3), 3 * (c // 3)
        for i in range(start_r, start_r + 3):
            for j in range(start_c, start_c + 3):
                if board[i][j] == ch:
                    return False
        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for ch in map(str, range(1, 10)):
                        if is_valid(i, j, ch):
                            board[i][j] = ch
                            if backtrack():
                                return True
                            board[i][j] = '.'  # undo
                    return False
        return True

    backtrack()


# Example usage
sudoku_board = [
    ["8",".",".","4",".","6",".",".","7"],
    [".",".",".",".",".",".","4",".","."],
    [".","1",".",".",".",".","6","5","."],
    ["5",".","9",".","3",".","7","8","."],
    [".",".",".",".","7",".",".",".","."],
    [".","4","8",".","2",".","1",".","3"],
    [".","5","2",".",".",".",".","9","."],
    [".",".","1",".",".",".",".",".","."],
    [".",".",".","9",".","2",".",".","5"]
]

print("Original Sudoku:")
for row in sudoku_board:
    print(row)

solveSudoku(sudoku_board)

print("\nSolved Sudoku:")
for row in sudoku_board:
    print(row)
