from Decomposers import Decomposer
from Producers import Producer
from Consumers import Consumer
import time

Producer()
Consumer()
Decomposer()
deadFood = 50
nutrients = 0
gen = 0
print("Gen: " + str(gen),"\nProducers: " + str(Producer.countP),"Consumers: " + str(Consumer.countC),"Decomposers: " + str(Decomposer.countD),"Dead Food: " + str(deadFood))
input()

def generationStep():
    global gen
    global deadFood
    global nutrients
    gen += 1
    
    p = list(Producer.listP)
    c = list(Consumer.listC)
    d = list(Decomposer.listD)
    
    deadFood += Producer.deadFood + Consumer.deadFood + Decomposer.deadFood
    Producer.deadFood = 0
    Consumer.deadFood = 0
    Decomposer.deadFood = 0
    
    nutrients += Decomposer.foodD
    for x in p:
        nutrients = x.eat(nutrients)
    for x in c:
        x.eat()
    for x in d:
        deadFood = x.eat(deadFood)
        
    print("Gen: " + str(gen),"\nProducers: " + str(Producer.countP),"Consumers: " + str(Consumer.countC),"Decomposers: " + str(Decomposer.countD),"Dead Food: " + str(deadFood))
    input()
    
    if Decomposer.countD == 0:
        Decomposer()
    if Producer.countP == 0:
        Producer()
    if Decomposer.countD == 0:
        Decomposer()
        
    generationStep()
generationStep()
