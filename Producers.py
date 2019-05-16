import random

class Producer:
    countP = 0
    listP = []
    foodP = 0
    deadFood = 0
    def __init__(self,p=True):
        self.age = 0
        self.reproductive = 0
        self.produce = p
        Producer.countP += 1
        Producer.listP += [self]
    def grow(self):
        self.age += 1
        if self.age > 4:
            self.reproductive = 1
        if self.age > 20:
            self.die()
        elif self.produce == True:
            self.food()
    def die(self):
        Producer.countP -= 1
        Producer.listP.remove(self)
        Producer.deadFood += self.age//2
        #print("RIP P")
    def eat(self,nutrients):
        self.grow()
        if nutrients > 0:
            nutrients -= 1
            self.food()
            return nutrients
        return nutrients
    def food(self):
        Producer.foodP += 1
    def reproduce(self):
        if self.reproductive == 1 and random.randint(0,2) == 0:
            self.reproductive = 2
            Producer()
            #print("New P")
