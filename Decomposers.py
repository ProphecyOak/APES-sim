import random

class Decomposer:
    countD = 0
    listD = []
    foodD = 0
    deadFood = 0
    def __init__(self,p=True):
        self.age = 0
        self.reproductive = 0
        self.produce = p
        Decomposer.countD += 1
        Decomposer.listD += [self]
    def grow(self):
        self.age += 1
        if self.age > 0:
            self.reproductive = 1
        if self.age > 4:
            self.die()
        elif self.produce == True:
            self.food()
    def die(self):
        Decomposer.countD -= 1
        Decomposer.listD.remove(self)
        Decomposer.deadFood += self.age//2
        #print("RIP D")
    def eat(self,deadFood):
        if deadFood > 0:
            deadFood -= 1
            self.grow()
            return deadFood
        else:
            self.die()
            return deadFood
    def food(self):
        Decomposer.foodD += 2
    def reproduce(self):
        if self.reproductive == 1 and random.randint(0,1) == 0:
            self.reproductive = 2
            Decomposer()
            #print("New D")
