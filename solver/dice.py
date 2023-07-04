import random

class Dice():
    def __init__(self, dice = None):
        self.roll = (0,0) if dice is None else dice
    
    # actual dice roll
    def roll_dice(self):
        self.roll = (random.randint(1, 6), random.randint(1, 6))
        return self.roll
    
    # jumps corresponding to dice roll
    def get_jumps(self):
        if self.roll[0] != self.roll[1]:
            return [self.roll[0], self.roll[1]]
        else:
            return [self.roll[0]] * 4
