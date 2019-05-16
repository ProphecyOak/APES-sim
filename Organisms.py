import random
import tkinter

class Organisms:
    deadFood = 0
    nutrients = 0
    plantFood = 0
    meatFood = 0

    ConsumersC = []
    ConsumersH = []
    ConsumersD = []
    ConsumersO = []
    Producers = []
    Decomposers = []
    
    consumerCountC = 0
    consumerCountH = 0
    consumerCountD = 0
    consumerCountO = 0
    producerCount = 0
    decomposerCount = 0

    Orgs = {"CC":ConsumersC,"CH":ConsumersH,"CD":ConsumersD,"CO":ConsumersO,"P":Producers,"D":Decomposers}
    OrgCount = {"CC":consumerCountC,"CH":consumerCountH,"CD":consumerCountD,"CO":consumerCountO,"P":producerCount,"D":decomposerCount}
    OrgFoods = {"CC":meatFood,"CH":plantFood,"P":nutrients,"D":deadFood,"CD":deadFood}
    OrgFoods2 = {"CC":meatFood,"CH":meatFood,"P":plantFood,"D":nutrients,"CD":meatFood}

    def __init__(self, orgType, deadAge = 5, age = 0, rAge = 0):
        self.age = age
        self.deadAge = deadAge
        self.rAge = rAge
        self.reproductive = 0
        self.orgType = orgType
        if orgType == "CC":
            Organisms.ConsumersC.append(self)
            Organisms.consumerCountC += 1
        elif orgType == "CH":
            Organisms.ConsumersH.append(self)
            Organisms.consumerCountH += 1
        elif orgType == "CD":
            Organisms.ConsumersD.append(self)
            Organisms.consumerCountD += 1
        elif orgType == "CO":
            Organisms.ConsumersO.append(self)
            Organisms.consumerCountO += 1
        elif orgType == "P":
            Organisms.Producers.append(self)
            Organisms.producerCount += 1
        elif orgType == "D":
            Organisms.Decomposers.append(self)
            Organisms.decomposerCount += 1
    def grow(self):
        self.age += 1
        if self.age > self.deadAge:
            self.die()
        else:
            self.food()
            if self.age >= self.rAge:
                self.reproductive = 1
    def die(self):
        print("Bye")
        Organisms.Orgs[self.orgType].remove(self)
        Organisms.OrgCount[self.orgType] -= 1
        Organisms.deadFood += self.age
    def eat(self):
        #Organisms.OrgFoods[self.orgType]
        if self.orgType == "CO":
            if (Organisms.deadFood > 0 or Organisms.plantFood > 0 or Organisms.meatFood > 0):
                foodList = []
                if Organisms.deadFood > 0:
                    foodList.append("D")
                if Organisms.plantFood > 0:
                    foodList.append("P")
                if Organisms.meatFood > 0:
                    foodList.append("M")
                f = random.choice(foodList)
                {"D":Organisms.deadFood,"P":Organisms.plantFood,"M":Organisms.meatFood}[f] -= 1
                self.grow()
            else:
                self.die()
        else:
            if Organisms.OrgFoods[self.orgType] > 0:
                Organisms.OrgFoods[self.orgType] -= 1
                self.grow()
            else:
                self.die()
    def food(self):
        Organisms.OrgFoods2[self.orgType] += 1
        print("hi")
    def reproduce(self):
        if self.reproductive == 1:
            if self.orgType == "CC" or self.orgType == "CH" or self.orgType == "CD" or self.orgType == "CO":
                for x in Organisms.ConsumersC:
                    if x != self and x.reproductive == 1 and self.orgType == x.orgType:
                        self.reproductive = 2
                        x.reproductive = 2
                        Organisms("C")
            else:
                self.reproductive = 2
                Organisms("C")
                print("Hello")
def gen():
    for x in Organisms.Producers:
        x.eat()
    for x in Organisms.ConsumersC:
        x.eat()
    for x in Organisms.ConsumersH:
        x.eat()
    for x in Organisms.ConsumersD:
        x.eat()
    for x in Organisms.ConsumersO:
        x.eat()
    for x in Organisms.Decomposers:
        x.eat()
        
    for x in Organisms.Producers:
        x.reproduce()
    for x in Organisms.ConsumersC:
        x.reproduce()
        x.reproduce()
    for x in Organisms.ConsumersH:
        x.reproduce()
        x.reproduce()
    for x in Organisms.ConsumersD:
        x.reproduce()
        x.reproduce()
    for x in Organisms.ConsumersO:
        x.reproduce()
    for x in Organisms.Decomposers:
        x.reproduce()
        
    print("P:",Organisms.producerCount,"C:",Organisms.consumerCountC+Organisms.consumerCountH+Organisms.consumerCountD+Organisms.consumerCountO,"D:",Organisms.decomposerCount)
    print("P:",Organisms.plantFood,"C:",Organisms.meatFood,"D:",Organisms.deadFood)
    input()
    gen()

Organisms("P")
Organisms("P")
Organisms("P")
Organisms("P")
Organisms("CH")
Organisms("CH")
Organisms("D")
Organisms("D")
Organisms.nutrients += 20
gen()
