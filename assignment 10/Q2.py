import random

def is_valid(board):
    for i in range(8):
        for j in range(i + 1, 8):
            # Check diagonals
            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def find_random_solution():
    attempts = 0
    while True:
        board = list(range(8))  # [0,1,2,3,4,5,6,7] — one queen per column
        random.shuffle(board)  # Shuffle to get random row placement
        attempts += 1
        if is_valid(board):
            print(f"Solution found after {attempts} attempts:")
            print_board(board)
            return board

def print_board(board):
    for row in range(8):
        line = ['.'] * 8
        line[board[row]] = 'Q'
        print(' '.join(line))

# Run it
find_random_solution()
