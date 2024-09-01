#!/usr/bin/python3
"""
N Queens problem solver.
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    
    Args:
    board (list of list of int): The chessboard.
    row (int): The row index.
    col (int): The column index.
    
    Returns:
    bool: True if it's safe, False otherwise.
    """
    # Check this column on the upper side
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False
    
    # Check upper diagonal on the right side
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i] == j:
            return False
    
    return True


def solve_nqueens_util(board, row):
    """
    Solve the N Queens problem using backtracking.
    
    Args:
    board (list of int): The chessboard represented as a list.
    row (int): The current row to place a queen.
    
    Returns:
    list of list of int: List of solutions where each solution is a list of queen positions.
    """
    if row == len(board):
        print([[i, board[i]] for i in range(len(board))])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_util(board, row + 1)
            # Backtrack
            board[row] = -1


def solve_nqueens(n):
    """
    Find all solutions for the N Queens problem.
    
    Args:
    n (int): Size of the chessboard (n x n).
    """
    board = [-1 for _ in range(n)]
    solve_nqueens_util(board, 0)


if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Validate that N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Ensure N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Solve the N Queens problem
    solve_nqueens(n)
