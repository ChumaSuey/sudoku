#This is the Sudoku solver of a 9x9 Sudoku.
#

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if (j+1) % 3 == 0 and j != 8:
                print("|", end=" ")
        print()
        if (i+1) % 3 == 0 and i != 8:
            print("- - - - - - - - - - - -")

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    # Check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 square
    square_x = pos[1] // 3
    square_y = pos[0] // 3
    for i in range(square_y*3, square_y*3 + 3):
        for j in range(square_x*3, square_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def count_solutions(board):
    find = find_empty(board)
    if not find:
        return 1
    else:
        row, col = find

    count = 0
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            count += count_solutions(board)

            if count > 1:
                return count

            board[row][col] = 0

    return count





# Example puzzle
board = [
    [0, 2, 0, 0, 0, 0, 1, 0, 3],
    [6, 0, 0, 0, 4, 8, 2, 0, 0],
    [0, 0, 5, 7, 3, 0, 0, 4, 0],
    [0, 0, 0, 0, 5, 1, 8, 0, 0],
    [9, 0, 4, 0, 0, 0, 0, 0, 7],
    [0, 3, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 0, 2, 1, 7, 3, 0, 0],
    [2, 0, 8, 0, 0, 0, 5, 6, 0],
    [0, 1, 9, 0, 0, 0, 0, 0, 4]
]


print("Original board:")
print_board(board)
num_solutions = count_solutions(board)
if num_solutions == 0:
    print("This puzzle has no solution.")
elif num_solutions == 1:
    solve(board)
    print("\nSolved board:")
    print_board(board)
else:
    print("This puzzle has multiple solutions.")
