
#This .py will just do the basics of the Sudoku solver, but it will only solve, not going further than that.

def print_board(board):
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=" ")
        print()

def find_empty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    # Check row
    for i in range(4):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(4):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 2x2 square
    square_x = pos[1] // 2
    square_y = pos[0] // 2
    for i in range(square_y*2, square_y*2 + 2):
        for j in range(square_x*2, square_x*2 + 2):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 5):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

# Example puzzle
board = [
    [0, 0, 2, 0],
    [4, 2, 0, 3],
    [0, 0, 3, 0],
    [2, 3, 0, 0]
]

print("Original puzzle:")
print_board(board)
print("\nSolution:")
solve(board)
print_board(board)

