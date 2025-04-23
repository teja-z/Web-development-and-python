def is_safe(board, row, col):
    for i in range(row):
        # Same column
        if board[i] == col:
            return False
        # Same diagonal (major or minor)
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_queens(board, row):
    if row == 8:
        print_board(board)
        return True  # Return True to stop at first solution, or collect all

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
    return False

def print_board(board):
    print("\n8 Queens Solution:")
    for row in range(8):
        line = ["." for _ in range(8)]
        line[board[row]] = "Q"
        print(" ".join(line))

# Start solving
board = [-1] * 8
solve_queens(board, 0)
