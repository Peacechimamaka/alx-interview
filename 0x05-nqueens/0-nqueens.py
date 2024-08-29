#!/usr/bin/python3
import sys

def print_solution(board, N):
    """Prints the solution in the required format."""
    solution = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)

def is_safe(board, row, col, N):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, N):
    """Utilizes backtracking to solve the N Queens problem."""
    if col == N:
        print_solution(board, N)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N) or res
            board[i][col] = 0

    return res

def solve_nqueens(N):
    """Initializes the board and starts solving the N Queens problem."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens_util(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
