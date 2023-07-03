class Move():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_valid(self, board, player):
        # if player has checker at start and end is empty, make move, otherwise throw exception
        # TODO Move Validation:
        # - Direction of movement 
        # - Hitting 1 checker
        # - Moving out of bar
        # - Bearing off moves
        move = (self.start, self.end)

        # Check if start pos in in bound
        if self.start < 0 or self.start > 25:
            print(f"Start position {self.start} is out of range for player {player}")
            return False
        
        elif self.start == 0 and player == board.PLAYER1:
            print(f"Start position {self.start} is out of range for player {player}")
            return False
        
        elif self.start == 25 and player == board.PLAYER2:
            print(f"Start position {self.start} is out of range for player {player}")
            return False
        
        # Check if player has checkers at start pos 
        if board.player_at(self.start) != player:
            print(f"Player {player} does not have a checkers at {self.start}")
            return False
        
        # Check direction of movement
        if self.start == self.end:
            print(f"Move {move} is in place")
            return False

        if (player == board.PLAYER1) and (self.start <= self.end):
            print(f"Player {player} is trying to move {move} in counter-clockwise direction")
            return False
        
        if (player == board.PLAYER2) and (self.start >= self.end):
            print(f"Player {player} is trying to move {move} in clockwise direction")
            return False
        
        # Check if player is jailed and tries to move other pieces
        # Player 1 is jailed
        if board.is_jailed(player) and player == board.PLAYER1 and self.start != 25:
            print(f"Player {player} tried move {move} when jailed at 25")
            return False
        
        # Player 2 is jailed
        elif board.is_jailed(player) and player == board.PLAYER2 and self.start != 0:
            print(f"Player {player} tried move {move} when jailed at 0")
            return False
        
        # If end_pos is out of bounds, make sure player can bear off
        if (player == board.PLAYER1) and (self.end <= 0):
            if board.is_bearing_off(player) == False:
                print(f"Player {player} is trying to move {move} but cannot bear-off yet")
                return False
            return True
        
        if (player == board.PLAYER2) and (self.end >= 25):
            if board.is_bearing_off(player) == False:
                print(f"Player {player} is trying to move {move} but cannot bear-off yet")
                return False
            return True

        # If end_pos is in range, handle hitting checkers
        other_player = 3 - player # 2 of PLAYER1, 1 if PLAYER2
        if board.player_at(self.end) == other_player:
            if board.value_at(self.end) > 1:
                print(f"Player {player} cannot move {move} where player {other_player} has {board.value_at(self.end)} checkers")
                return False
        
        return True
        
