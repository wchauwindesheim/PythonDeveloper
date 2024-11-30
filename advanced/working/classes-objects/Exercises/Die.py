import random
class Die:
    def __init__(self, sides=6):
        self._sides = sides
        
    # add a roll() method
    def roll(self):
        # print("Rolling the die!")
        return random.randint(1, self.sides)
    
    # add a getter for sides
    def get_sides(self):
        return self._sides
    
    # add a setter for sides
    def set_sides(self, sides):
        if sides > 10 :
            raise ValueError("The number of sides must be at least 10")
        else :        
            self._sides = sides