print("The following is a Sodoku Solver coded in Python which utilizes the backtracking algorithm.")
print("")
print("Rules:")
print("You will input numbers to create the board, and the solver will produce the correct solution to the puzzle.")
print("")

#Initializing empty board
board = [[0] * 9 for _ in range(9)]

#Consuming user input to create board
for i in range(9):
    row_input = input(f"Enter nine values for row {i + 1}, seperated by spaces (use 0 for empty cells): ")
    board[i] = [int(num) for num in row_input.split()]

#Printing the board
def show_board(board):
    for i in range (len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range (len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(board[i][j])

            else:
                print(str(board[i][j]) + " ", end = "")


#Function that finds and returns empty spaces 
def find_space(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)   #row, column
            

#Function to check if the board is valid 
def valid_board(board, num, pos):

    #Checking row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        
    #Check column
        for i in range (len(board[0])):
            if board[i][pos[1]] == num and pos[0] != i:
                return False
            
    #Checking the box that we are in 
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #Loop through box that we are in, and ensuring that the same element does not repeat 
    for i in range (box_y * 3, box_y * 3 + 3):
        for j in range (box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
            
    return True


#Creating a function that solves the board and utilizes the backtracking algorithm
def solve(board):

    find = find_space(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid_board(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            
        board[row][col] = 0

    return False

#Displaying the board and solving it
print("Original board:")
show_board(board)
solve(board)
print("_______________________")
print("")
print("Solved board:")
show_board(board)