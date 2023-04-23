#Sudoku solver for 4x4 Sudokus
#Sudokus are a matrix, and must be a squared matrix so values will range from 1 to 4


#This function just prints the board based in range matrix, will go through the matrix array.
def print_board(board):
    for i in range(4):
        for j in range(4):
            print(board[i][j], end=" ")
        print()


#This function will just find empty spaces for analysis and problem solving
def find_empty(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return (i, j)
    return None


#Complex function of all the Sudoku app, it will check each Row, column then the whole square to check the numbers
#Mostly for repeats and incidents

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


#Once verified, it will proceed to solve the matrix

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


# This function will go through the whole matrix verifying the solution.
def verify_solution(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False

            temp = board[i][j]
            board[i][j] = 0

            if not is_valid(board, temp, (i, j)):
                board[i][j] = temp
                return False

            board[i][j] = temp

    return True

#Summarizing in steps:
#Through in solution it will use the validation function and to see which inputs are empty.
#The solution will be made, then verified.


# This is an example puzzle, but in fact is the input.
# It would be interesting a keyboard input for the matrix but that's outside of the scope of the project
# So... Board is the input section, input the exercise correctly.
board = [
    [0, 1, 0, 2],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [4, 0, 1, 0]
]

# Board must be 4x4, exercise must be 4x4
# Wrong input will lead to no solution or multiple solutions

#This will print the original board function previously explained.
print("Original puzzle:")
print_board(board)
print()


#This will print the solution or the other paths.
if solve(board):
    print("Solution:")
    print_board(board)
    if verify_solution(board):
        print("The puzzle has a unique solution.")  #in this case the solution will be printed
    else:
        print("The puzzle has multiple solutions.")
else:
    print("The puzzle has no solution.")

# If the puzzle has multiple solutions... it will not try to solve it, just to tell it.