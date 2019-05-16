import random

class Consumer:
    def __init__(self):
        self.age = 0
        self.reproductive = 0
        self.deadAge = 10
    def grow(self):
        self.age += 1
        if self.age > self.deadAge:
            return "D"
        elif self.age > 2:
            self.reproductive = 1
        return "E"
class Producer:
    def __init__(self):
        self.age = 0
        self.reproductive = 0
        self.deadAge = 15
    def grow(self):
        self.age += 1
        if self.age > self.deadAge:
            return "D"
        return "E"
