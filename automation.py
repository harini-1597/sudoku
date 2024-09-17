import pyautogui as pg
import time

# Input function
board = []
while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    board.append(ints)

    if len(board) == 9:
        break
    print("Row " + str(len(board)) + " Complete")

time.sleep(3)

def automation_solver(board):
    # List to hold the board values as strings
    str_final = []
    for row in board:
        for num in row:
            str_final.append(str(num))
    
    counter = 0
    for num in str_final:
        if num != '0':  # Skip if the value is 0 (empty in Sudoku)
            pg.press(num)  # Press the number key
        pg.hotkey('right')  # Move right after pressing the number
        counter += 1
        
        # After each row (9 cells), move down and reset column position
        if counter % 9 == 0:
            pg.hotkey('down')
            for _ in range(8):
                pg.hotkey('left')

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("--------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=" ")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    # Row check
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        
    # Column check
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Loop through that box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
            
    return True

def solve(board):
    # Recursive solver
    find = find_empty(board)
    if not find:
        automation_solver(board)  # Trigger automation solver when done
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

solve(board)