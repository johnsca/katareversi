#!/bin/env python

class Row(object):
    cols = None

    def __init__(self, data):
        self.cols = data

    def col(self, col_num):
        return self.cols[col_num]

class Board(object):
    rows = []
    num_rows = 0
    num_cols = 0

    def __init__(self, data):
        for line in data:
            self.rows.append(Row(line))
        self.num_rows = len(self.rows)
        self.num_cols = len(self.rows[0].cols)

    def row(self, row_num):
        return self.rows[row_num]

def read_board(data):
    data = data.split('\n')
    board = Board(data[0:-1])
    turn = data[-1]
    return board, turn

directions = {
    'N':  {'row':-1, 'col': 0},
    'NE': {'row':-1, 'col':+1},
    'E':  {'row': 0, 'col':+1},
    'SE': {'row':+1, 'col':+1},
    'S':  {'row':+1, 'col': 0},
    'SW': {'row':+1, 'col':-1},
    'W':  {'row': 0, 'col':-1},
    'NW': {'row':-1, 'col':-1},
}

def next_square(row, col, direction):
    row = row + directions[direction]['row']
    col = col + directions[direction]['col']
    return row, col

def check_direction(board, row, col, turn, direction, seen_opponent=False):
    current_square = board.row(row).col(col)
    if current_square != '.':
        return False
    row, col = next_square(row, col, direction)
    if row < 0 or row >= board.num_rows:
        return False
    if col < 0 or col >= board.num_cols:
        return False
    if board.row(row).col(col) == turn:
        return False
    if board.row(row).col(col) == '.':
        return seen_opponent
    # we encountered an opponent!
    return check_direction(board, row, col, turn, direction, seen_opponent=True)

def check_board_position(board, row, col, turn):
    for direction in directions.keys():
        check_direction(board, row, col, turn, direction)

def check_entire_board():
    pass

def output():
    pass
