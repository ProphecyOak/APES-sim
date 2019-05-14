import random

class Consumer:
    countC = 0
    listC = []
    foodC = 0
    deadFood = 0
    def __init__(self,p=False):
        self.age = 0
        self.reproductive = 0
        self.eats = 0
        self.produce = p
        Consumer.countC += 1
        Consumer.listC += [self]
    def grow(self):
        pass
    def die(self):
        pass
    def eat(self):
        pass
    def food(self):
        pass
    def reproduce(self):
        pass
