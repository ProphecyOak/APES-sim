import random

class Consumer:
    def __init__(self):
        self.age = 0
        self.reproductive = 1
        self.deadAge = 3
    def grow(self):
        self.age += 1
        if self.age > self.deadAge:
            return "D"
        elif self.age > 2:
            self.reproductive = 1
        return "E"
    def __lt__(self, other):
        return self.age < other.age
    def __gt__(self, other):
        return self.age > other.age
    def __eq__(self, other):
        return self.age == other.age
class Producer:
    def __init__(self):
        self.age = 0
        self.reproductive = 0
        self.deadAge = 15
    def grow(self):
        self.age += 1
        if self.age > self.deadAge:
            return "D"
        elif self.age > 2:
            self.reproductive = 1
        return "E"
    def __lt__(self, other):
        return self.age < other.age
    def __gt__(self, other):
        return self.age > other.age
    def __eq__(self, other):
        return self.age == other.age
