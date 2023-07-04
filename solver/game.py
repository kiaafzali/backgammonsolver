from board import Board
from dice import Dice
from move import Move



class Game():
    def __init__(self):
        self.board = Board()
        self.dice = Dice()
        self.current_player = self.board.current_player

    def run(self):

        while self.board.is_game_over() == 0:
            roll = self.dice.roll_dice()
            print(f"Player {self.current_player}'s turn with dice roll [{roll[0]}] [{roll[1]}].")
            self.board.print()
            move = input(f"Please input move, e.g.: 2,4\n")
            move_list = move.split(',')
            move = Move(int(move_list[0]), int(move_list[1]))
            self.board.apply_move(move, self.current_player)
            self.current_player = 3 - self.current_player





if __name__ == "__main__":
    game = Game()
    game.run()