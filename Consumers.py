import random

class Consumer:
    countC = 0
    listC = []
    foodC = 0
    deadFood = 0
    def __init__(self,e = 0,p=False):
        self.age = 0
        self.reproductive = 0
        self.eats = e   #0:Herbivore, 1:Carnivore, 2:Detritovore
        self.produce = p
        Consumer.countC += 1
        Consumer.listC += [self]
    def grow(self):
        self.age += 1
        if self.age > 3:
            self.reproductive = 1
        if self.age > 10:
            self.die()
        elif self.produce == True:
            self.food()
    def die(self):
        Consumer.countC -= 1
        Consumer.listC.remove(self)
        Consumer.deadFood += self.age//2
        #print("RIP C")
    def eat(self,deadFood,producerFood):
        if self.eats == 0 and producerFood > 0:
            producerFood -= 1
            self.grow()
            return deadFood,producerFood
        elif self.eats == 1 and len(Consumer.listC) > 1:
            ageBottom = 10
            for x in Consumer.listC:
                if x.age < ageBottom and x != self:
                    ageBottom = x.age
                    y = x
            self.grow()
            y.die()
            return deadFood,producerFood
        elif self.eats == 2 and deadFood > 0:
            deadFood -= 1
            self.grow()
            return deadFood,producerFood
        else:
            self.die()
            return deadFood,producerFood
    def food(self):
        Consumer.foodC += 1
    def reproduce(self):
        if self.reproductive == 1 and random.randint(0,2) == 0:
            for x in Consumer.listC:
                if x.reproductive ==1:
                    Consumer()
                    self.reproductive = 2
                    x.reproductive = 2
                    #print("New C")
