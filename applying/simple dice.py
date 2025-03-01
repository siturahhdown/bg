import random

class Dice:
    def __init__ (self):
        pass
        
    def __call__(self):
        roll = random.randint(1,6)
        print(roll)
        
dice1 = Dice()
dice1()