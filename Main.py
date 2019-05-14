from Decomposers import Decomposer
from Producers import Producer
from Consumers import Consumer
import time

Producer()
Producer()
Producer()
Consumer()
Consumer()
Decomposer()
deadFood = 50
nutrients = 0
gen = 0
print("Gen: " + str(gen),"\nProducers: " + str(Producer.countP),"Consumers: " + str(Consumer.countC),"Decomposers: " + str(Decomposer.countD),
      "Dead Food: " + str(deadFood),"Produced Food: " + str(Producer.foodP))
input()

def generationStep():
    global gen
    global deadFood
    global nutrients
    gen += 1
    
    if Decomposer.countD <= 0:
        Decomposer()
    if Producer.countP <= 0:
        Producer()
    if Consumer.countC <= 0:
        Consumer()
        Consumer()
    
    p = list(Producer.listP)
    c = list(Consumer.listC)
    d = list(Decomposer.listD)
    
    deadFood += Producer.deadFood + Consumer.deadFood + Decomposer.deadFood
    Producer.deadFood = 0
    Consumer.deadFood = 0
    Decomposer.deadFood = 0
    
    nutrients += Decomposer.foodD
    for x in c:
        z = x.eat(deadFood,Producer.foodP)
        Producer.foodP = int(z[1])
        deadFood = z[0]
    for x in d:
        deadFood = x.eat(deadFood)
    for x in p:
        nutrients = x.eat(nutrients)
    for x in c:
        x.reproduce()
    for x in d:
        x.reproduce()
    for x in p:
        x.reproduce()
        
    print("Gen: " + str(gen),"\nProducers: " + str(Producer.countP),"Consumers: " + str(Consumer.countC),"Decomposers: " + str(Decomposer.countD),
          "Dead Food: " + str(deadFood),"Produced Food: " + str(Producer.foodP))
    input()
        
    generationStep()
generationStep()
