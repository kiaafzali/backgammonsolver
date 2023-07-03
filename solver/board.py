from move import Move

class Board():

    # Board Constants 
    BOARD_LENGTH = 26
    INIT_BOARD = [0, 2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 5, 5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2, 0]
    INIT_PLAYER_POS = [0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 1,0 , 0, 0, 2, 0, 2, 0, 0, 0,0 , 1, 0]

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

    # Applies move and implements hitting logic. Assumes move is valid.
    # Move is already validated in move.is_valid() method
    # which should always be called before this apply_move()
    def apply_move(self, move, player):
        start_pos, end_pos = move.start, move.end

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

def TestBoardSetup():
    board = Board()
    assert board.player_pos == Board.INIT_PLAYER_POS
    assert board.board == Board.INIT_BOARD
    board.print()

if __name__ == '__main__':
    TestBoardSetup()
    

