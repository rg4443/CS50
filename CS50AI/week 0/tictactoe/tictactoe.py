"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # gets the sum of the x's & o's that are currently on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # if the game is terminated via terminal function game is over
    if terminal(board):
        return None

    # if there are less X's or same amount of X as O's then it is X's turn, else it is O's turn
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    # if game is over then there are no longer any possible moves
    if terminal(board):
        return possible_moves

    # get all spaces on the board via a 3x3 grid, if spaces are empty then add them to possible_moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Make a deep-copy of the original board
    new_board = copy.deepcopy(board)

    # Check if the action is valid by ensuring indices are within bounds
    i, j = action
    if i < 0 or i >= 3 or j < 0 or j >= 3:
        raise ValueError("Invalid Move, Out of Bounds")

    # Check if the space on the board is not empty
    if new_board[i][j] is not EMPTY:
        raise ValueError("Invalid Move, Space is Already Occupied")

    # return the board but with the move that the player made
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check if 3 are in a row
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # check if 3 are in a column
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]

    # check if 3 are in a diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # if all other cases fail, then that means that there is no winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Checks for a win
    if winner(board) is not None:
        return True

    # checks if the board is full
    for row in board:
        if EMPTY in row:
            return False

    # if all cases fail, then that means board is full, and there is no winner
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)

    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # check if the game is over or not if so no optiomal move can be made
    if terminal(board):
        return None

    current_player = player(board)

    # if player is X then try to get max value, else(e.g O) try to get min value
    if current_player == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)

    return action


# get the max value of the board (e.g 1)
def max_value(board):
    # check if game is over, if so then no max value can be provided
    if terminal(board):
        return utility(board), None

    # set v to negative infinity to get the lowest possible value
    v = float("-inf")
    optimal_action = None

    # for each avaliable possible action get the min value of the board and find the max value
    for action in actions(board):
        new_board = result(board, action)
        min_val, _ = min_value(new_board)

        if min_val > v:
            v = min_val
            optimal_action = action

    return v, optimal_action


def min_value(board):
    # check if the game is over
    if terminal(board):
        return utility(board), None

    # set v to postive infinity to get the highest possible value
    v = float("inf")
    optimal_action = None

    # for each avaliable possible action get the max value of the board and find the mix value
    for action in actions(board):
        new_board = result(board, action)
        max_val, _ = max_value(new_board)

        if max_val < v:
            v = max_val
            optimal_action = action

    return v, optimal_action
