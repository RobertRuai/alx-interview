#!/usr/bin/python3
"""N Queens File"""
import sys


def error_exit(mess="", code=1):
    """Handles exit"""
    print(mess)
    exit(code)


def pos(board, n):
    """Tests wether a queen can be placed at the current pos"""
    for i in range(n):
        if board[n][1] is board[i][1]:
            return False
        if abs(board[n][1] - board[i][1]) == n - i:
            return False
    return True


def backtrack(board, n):
    """Backtracks probable possibilities"""
    if n is N:
        print(board)
    else:
        for i in range(N):
            board[n][1] = i
            if pos(board, n):
                backtrack(board, n + 1)


if len(sys.argv) != 2:
    error_exit("Usage: nqueens N")

try:
    N = int(sys.argv[1])
except Exception:
    error_exit("N must be a number")

if N < 4:
    error_exit("N must be at least 4")

board = [[n, 0] for n in range(N)]
backtrack(board, 0)
