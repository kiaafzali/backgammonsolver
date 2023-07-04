import pytest
from dice import Dice


def test_dice():
    print("\n________________________________")
    print("test_dice")
    
    dice = Dice()
    assert dice.roll[0] == 0
    assert dice.roll[1] == 0

    dice.roll_dice()
    assert 1 <= dice.roll[0] <= 6
    assert 1 <= dice.roll[1] <= 6

    dice = Dice((2, 5))
    assert dice.get_jumps() == [2, 5]

    dice = Dice((5,5))
    assert dice.roll[0] == 5
    assert dice.get_jumps() == [5, 5, 5, 5]
    print("________________________________\n")



if __name__ == '__main__':
    test_dice()