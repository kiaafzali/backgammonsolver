import pytest
from board import Board
from move import Move
from copy import deepcopy

"""
TODO:
- test_is_bearing_off
- test_is_jailed
"""


PLAYER1 = 1
PLAYER2 = 2

INIT_BOARD = [0, 2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 5, 5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2, 0]
INIT_PLAYER_POS = [0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 1,0 , 0, 0, 2, 0, 2, 0, 0, 0,0 , 1, 0]


def test_board_setup():
    print("\n________________________________")
    print("test_board_setup")
    board = Board()
    assert board.player_pos == Board.INIT_PLAYER_POS
    assert board.board == Board.INIT_BOARD
    board.print()  # This line is not necessary for the test, but it can be useful for debugging
    print("________________________________\n")


def test_apply_move():
    print("\n________________________________")
    print("test_apply_move")

    board = Board()

    move1 = Move(24, 23)
    move2 = Move(12, 14)

    board.apply_move(move1, PLAYER1)
    board.apply_move(move2, PLAYER2)

    assert board.value_at(23) == 1
    assert board.player_at(23) == PLAYER1

    assert board.value_at(24) == 1
    assert board.player_at(24) == PLAYER1

    assert board.value_at(12) == 4
    assert board.player_at(12) == PLAYER2

    assert board.value_at(14) == 1
    assert board.player_at(14) == PLAYER2

    board.print()
    print("________________________________\n")


def test_undo():
    print("\n________________________________")
    print("test_undo")
    board = Board()
    board.print()
    test_board = deepcopy(board)
    board.apply_move(Move(1, 3), 2)
    board.undo()
    assert board.board == test_board.board
    assert board.player_pos == test_board.player_pos
    print("________________________________\n")


def test_get_pips():
    print("\n________________________________")
    print("test_get_pips")
    board = Board()
    board.print()
    assert board.get_pips(1) == 167
    assert board.get_pips(2) == 167
    print("________________________________\n")


if __name__ == '__main__':
    # test_board_setup()
    # test_apply_move()
    # test_undo()
    test_get_pips()