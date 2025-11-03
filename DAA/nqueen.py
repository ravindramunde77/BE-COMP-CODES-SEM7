def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()  # blank line between solutions


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    if row == n:
        print_board(board, n)
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            res = solve_n_queens(board, row + 1, n) or res
            board[row][col] = 0  # backtrack

    return res


# Main program
n = int(input("Enter number of queens: "))
board = [[0 for _ in range(n)] for _ in range(n)]

print(f"\nSolutions for {n}-Queens Problem:\n")
if not solve_n_queens(board, 0, n):
    print("No solution exists!")
