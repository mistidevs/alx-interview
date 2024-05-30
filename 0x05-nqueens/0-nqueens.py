#!/usr/bin/python3
"""
Placing non attacking queens on a
chess board using matrices, recursion
and backtracking
"""
import sys


def is_safe(board, row, col, n):
    """
    Checking if a queen can be placed here
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, n, 1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n, solutions):
    """
    Solving the nqueens problem using recursion
    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, n, solutions) or res
            board[i][col] = 0

    return res


def find_all_nqueens_solutions(n):
    """
    Finding and printing all nqueen solutions
    """
    if not isinstance(n, int):
        print("N must be a number")
        exit(1)
    
    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    if not sys.argv[1] or len(sys.argv) > 2:
        print("Usage: nqueens N")
        exit(1)

    find_all_nqueens_solutions(int(sys.argv[1]))
