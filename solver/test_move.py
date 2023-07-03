import pytest
from board import Board
from move import Move

INIT_BOARD = [0, 2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 5, 5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2, 0]
INIT_PLAYER_POS = [0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 1,0 , 0, 0, 2, 0, 2, 0, 0, 0,0 , 1, 0]

def test_regular_moves():
    print("\n________________________________")
    print("test_regular_moves")
    
    board = Board(board=INIT_BOARD, player_pos=INIT_PLAYER_POS)

    move1 = Move(24, 23)
    move2 = Move(23, 22)

    assert move1.is_valid(board, 1) == True
    assert move2.is_valid(board, 1) == False
    print("________________________________\n")

def test_direction_moves():
    print("\n________________________________")
    print("test_direction_moves")
    board = Board(board=INIT_BOARD, player_pos=INIT_PLAYER_POS)

    move1 = Move(1, 3)
    move2 = Move(12, 10) 

    assert move1.is_valid(board, 2) == True
    assert move2.is_valid(board, 2) == False
    print("________________________________\n")


def test_start_moves():
    print("\n________________________________")
    print("test_start_moves")

    board = Board(board=INIT_BOARD, player_pos=INIT_PLAYER_POS)
    
    # Out of bounds
    move1 = Move(-2, 3)
    move2 = Move(27, 7)

    # Checkers don't exist 
    move3 = Move(2, 4)
    move4 = Move(1, 4)

    assert move1.is_valid(board, 2) == False
    assert move2.is_valid(board, 2) == False
    assert move3.is_valid(board, 2) == False
    assert move4.is_valid(board, 1) == False
    print("________________________________\n")


def test_hitting_moves():
    print("\n________________________________")
    print("test_hitting_moves")
    board = Board(board=INIT_BOARD, player_pos=INIT_PLAYER_POS)

    move1 = Move(1, 6)
    move2 = Move(6, 5)
    move3 = Move(1, 5)

    assert move1.is_valid(board, 2) == False
    assert move3.is_valid(board, 2) == True
    
    board.apply_move(move2, 1)
    assert board.player_at(5) == 1
    assert board.value_at(5) == 1
    assert move3.is_valid(board, 2) == True
    print("________________________________\n")


def test_bearing_off():
    print("\n________________________________")
    print("test_bearing_off")

    test_board = [0, 0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5, 3, 0, 0, 0, 2, 0]
    test_pos = [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1,0 , 0, 0, 0, 0, 2, 2, 0, 0,0 , 1, 0]
    
    board = Board(board=test_board, player_pos=test_pos, current_player=2)

    assert board.value_at(19) == 5
    assert board.value_at(20) == 3

    move1 = Move(19, 25)
    move2 = Move(20, 26)
    move3 = Move(6, 0)

    assert move1.is_valid(board, 2) == True
    assert move2.is_valid(board, 2) == True
    assert move3.is_valid(board, 1) == False
    print("________________________________\n")



    


    


if __name__ == '__main__':
    test_regular_moves()
    test_direction_moves()
    test_start_moves()
    test_hitting_moves()
    test_bearing_off()