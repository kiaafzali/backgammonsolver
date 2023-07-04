from move import Move
from copy import deepcopy

class Board():

    # Board Init Setup 
    INIT_BOARD = [0, 2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 5, 5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2, 0]
    INIT_PLAYER_POS = [2, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 1,0 , 0, 0, 2, 0, 2, 0, 0, 0,0 , 1, 1]

    # Players
    EMPTY = 0 # Empty spots
    PLAYER1 = 1 # Blue or AI
    PLAYER2 = 2 # Red or Player

    # Color for terminal display
    PLAYER1COLOR = '\033[94m' # Blue or PLAYER1 | User
    PLAYER2COLOR = '\033[91m'  # Red for PLAYER2 | AI
    ENDC = '\033[0m'

    # Initialize Board into given state or create default start board with PLAYER1 | USER 
    def __init__(self, board = None, player_pos = None, current_player = None):
        self.board = Board.INIT_BOARD if board is None else board
        self.player_pos = Board.INIT_PLAYER_POS if player_pos is None else player_pos
        self.current_player = Board.PLAYER1 if current_player is None else current_player
        self.history = []
    
    def value_at(self, pos):
        return self.board[pos]
    
    def player_at(self, pos):
        return self.player_pos[pos]
    
    # Where this player goes to jail if got hit
    def jail_for(self, player):
        return 25 if player == self.PLAYER1 else 0
    
    # Returns True if player is jailed
    def is_jailed(self, player):
        if self.player_at(0) and player == self.PLAYER2:
            return True
        elif self.player_at(25) and player == self.PLAYER1:
            return True
        return False
    
    # Returns True if player is able to bear off
    def is_bearing_off(self, player):
        # For PLAYER1
        if player == self.PLAYER1:
            for pos in range(7, 26):
                if self.player_at(pos) == self.PLAYER1:
                    return False
            return True
        # For PLAYER2
        else:
            for pos in range(0, 19):
                if self.player_at(pos) == self.PLAYER2:
                    return False
                return True
    
    # Returns checker count for player
    def get_checker_count(self, player):
        count = 0
        for i in range(0, len(self.board)):
            if self.player_at(i) == player:
                count += self.value_at(i)
        return count
    
    def get_pips(self, player):
        count = 0
        for i in range(0, len(self.board)):
            if self.player_at(i) == player:
                count += (self.value_at(i) * i)
        if player == self.PLAYER2:
            count = (25 * self.get_checker_count(self.PLAYER2)) - count
        return count

    
    # Returns 0 if game is still going, 1 if player1 wins, and 2 if player2 wins
    def is_game_over(self):
        if self.get_checker_count(self.PLAYER1) == 0:
            return self.PLAYER1
        elif self.get_checker_count(self.PLAYER2) == 0:
            return self.PLAYER2
        else:
            return 0
    
    # Undo move
    def undo(self):
        current_player, board, player_pos = self.history.pop()
        self.current_player = current_player
        self.board = board
        self.player_pos = player_pos

    # Applies move and implements hitting logic. Assumes move is valid.
    # Move is already validated in move.is_valid() method
    # which should always be called before this apply_move()
    def apply_move(self, move, player):
        start_pos, end_pos = move.start, move.end
        self.history.append((self.current_player, deepcopy(self.board), deepcopy(self.player_pos)))

        # Remove checker from start pos
        self.board[start_pos] -= 1
        if self.board[start_pos] == 0:
            self.player_pos[start_pos] = Board.EMPTY
        
        # Move Checker to end pos

        # Don't land the checker during bear off
        if player == Board.PLAYER1 and end_pos >= 25:
            return
        if player == Board.PLAYER2 and end_pos <= 0:
            return   
        
        # Move other_player checker to jail if in end_pos
        other_player = 3 - player
        if self.player_at(end_pos) == other_player:
            if self.value_at(end_pos) > 1:
                raise Exception(f"Player {player} hitting more than one checker during move {(move.start, move.end)}")
            self.board[end_pos] = 0
            self.board[self.jail_for(other_player)] += 1
        
        # Move checker to end_pos
        self.player_pos[end_pos] = player
        self.board[end_pos] += 1
        
        return

    # Prints the board positions 0 -> 25
    # Blue for Player 1, Red for Player 2, White for Empties
    def print(self):
        for pos in range(len(self.board)):
            if self.player_at(pos) == Board.PLAYER1:
                color = Board.PLAYER1COLOR
            elif self.player_at(pos) == Board.PLAYER2:
                color = Board.PLAYER2COLOR
            else:
                color = Board.ENDC

            print(f"{color}{self.board[pos]}{Board.ENDC}", end=" ")
        print()

def test():
    board = Board()
    board.print()
    board.apply_move(Move(6, 0), 1)
    board.apply_move(Move(1, 25), 2)
    print(board.get_pips(1))
    print(board.get_pips(2))

if __name__ == '__main__':
    pass
    # board = Board()
    # dice = Dice()
    # move = input("Put move down here: e.g. 2,5")
    

