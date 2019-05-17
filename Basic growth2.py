"""Import Modules"""
import random
import time
import tkinter
from Consumer2 import Consumer, Producer
"""Starter Values"""
proColor = "forest green"
conColor = "firebrick3"
resColor = "steelblue"
bacColor = "gainsboro"
resources = 100
pop = [Consumer()]
popPro = [Producer()]
fruit = 0
oldResources = 100
maxPop = 1
gen = 0
W = 1400
H = 600
Z = 20
Si = 6
Sp = 6
"""Read Save Data"""
newFile = open(r"Data.txt",mode="r")
exec(newFile.read())
newFile.close()
testNum = dataList[-1]
dataList = dataList[:-1]
"""Input 1"""
genNum = 0#input("How Many Generations?\n>>> ")
"""Functions"""
def Test():
    global gen, pop, gen, oldResources, maxPop, W, H, Z, resources, dataList, testNum, popPro, fruit
    global proColor, conColor, resColor, bacColor
    dataList.insert(0,[])
    
    def gene():
        global gen,pop, gen, oldResources, maxPop, W, H, Z, resources, dataList, testNum, genNum, popPro, fruit
        global proColor, conColor, resColor, bacColor
        """Resource Generation"""
        """
        for x in popPro:
            if int(resources) < len(popPro):
                for y in range(len(popPro)-int(resources)):
                    maxAge = 0
                    oldest = 0
                for x in popPro:
                    if x.age >= maxAge:
                        oldest = x
                        maxAge = x.age
                popPro.remove(oldest)
            elif x.grow() == "D":
                popPro.remove(x)
                resources += x.age
            else:
                if resources >= 10:
                    fruitNum = random.randint(0,4)
                    fruit += fruitNum
                    resources -= fruitNum
                else:
                    fruit += resources
                    resources = 0
        for x in range(fruit):
            fruit -= 1
            resources += 2
            if random.randint(0,9) == 0:
                popPro.append(Producer())
        """
        #"""
        changeInResources = abs(int(resources) - oldResources)
        #resources += (100 - (random.random()-.01)*resources) #Tall Logistic Growth
        #resources += 100 - resources #Simple Logistic Growth
        resources += abs(int(changeInResources+random.randint(-5,5))) #Fluctuating Logistic Growth
        #resources += int(changeInResources * (random.random() + .5)) #Wild
        #resources += random.randint(-10,20)*pop/100 + .8*pop #Die Out Fast
        #resources += len(pop) + 1 #Constant
        #resources += len(pop)*1.2 #Competition Die Out
        #resources += len(pop)*1.5 #Stablish
        if resources < 0:
            resources = 0
        oldResources = resources
        #"""
        """Gen Update"""
        gen += 1
        """Growth"""
        if int(resources) < len(pop):
            for y in range(len(pop)-int(resources)):
                maxAge = 0
                oldest = 0
                for x in pop:
                    if x.age >= maxAge:
                        oldest = x
                        maxAge = x.age
                pop.remove(oldest)
        for x in pop:
                resources -= 1
                if x.grow() == "D":
                    pop.remove(x)
                    resources += x.age
        """Reproduction"""
        for x in pop:
            if int(resources) > 20 and random.randint(0,1) == 0 and x.reproductive == 1:
                pop.append(Consumer())
                resources -= 5
        """Data Save"""
        dataList[0].append([int(resources),len(pop),len(popPro),gen])
        """Graphics Update"""
        L.config(text="R: " + str(int(resources)) + " C: " + str(len(pop)) + " P: " + str(len(popPro)))
        L2.config(text="Gen: " + str(gen))
        C.create_rectangle(gen*(3*Si+3)+Sp+Z,(H-20),gen*(3*Si+3)+2*Sp+Z,(H-20)-int(resources)*3,fill=resColor,outline="")
        C.create_rectangle(gen*(3*Si+3)+2*Sp+Z,(H-20),gen*(3*Si+3)+3*Sp+Z,(H-20)-len(pop)*3,fill=conColor,outline="")
        C.create_rectangle(gen*(3*Si+3)+3*Sp+Z,(H-20),gen*(3*Si+3)+4*Sp+Z,(H-20)-len(popPro)*3,fill=proColor,outline="")
        if (gen)%5 == 0:
            C.create_text(gen*(3*Si+3)+2.5*Sp+Z,H-10,text=gen)
        master.update()
    """Graphics Set-Up"""
    master = tkinter.Tk()
    master.geometry("%dx%d+%d+%d" % (W,H+30,0,0))
    B = tkinter.Button(master,command=gene,text="Next Gen.")
    B.grid(row=0,column=2, sticky="N")
    L = tkinter.Label(master,text="R: " + str(int(resources)) + " C: " + str(len(pop)) + " P: " + str(len(popPro)))
    L.grid(row=0,column=1, sticky="W")
    L2 = tkinter.Label(master,text="Gen: " + str(gen))
    L2.grid(row=0,column=0)
    C = tkinter.Canvas(master,width=W,height=H,bg=bacColor)
    C.grid(row=1,column=0,columnspan=30)
    for x in range(0,H,50):
        C.create_text(10,H-x*3-20,text=x)
    """Data 1"""
    C.create_rectangle(gen*(3*Si+3)+Sp+Z,(H-20),gen*(3*Si+3)+2*Sp+Z,(H-20)-int(resources)*3,fill=resColor,outline=resColor)
    C.create_rectangle(gen*(3*Si+3)+2*Sp+Z,(H-20),gen*(3*Si+3)+3*Sp+Z,(H-20)-len(pop)*3,fill=conColor,outline=conColor)
    C.create_rectangle(gen*(3*Si+3)+3*Sp+Z,(H-20),gen*(3*Si+3)+4*Sp+Z,(H-20)-len(popPro)*3,fill=proColor,outline=proColor)
    C.create_text(gen*(3*Si+3)+2.5*Sp+Z,H-10,text=gen)
    dataList[0].append([resources,len(pop),len(popPro),gen])
    """Run Generations"""
    for x in range(int(genNum)):
        gene()
    """Refresh"""
    resources = 100
    pop = [Consumer()]
    popPro = [Producer()]
    fruit = 0
    gen = 0
    oldResources = 100
    print(maxPop)
    maxPop = 1
    popZ = 0
    testNum += 1
    #master.destroy()
"""Run Tests"""
thing = 1#input("How Many Runs?\n>>> ")
for x in range(int(thing)):
    Test()
    print("\nTest:",testNum)
"""Saved Data Write"""
dataList.append(testNum)
newFile = open(r"Data.txt",mode="w")
newFile.write("dataList = " + str(dataList))
newFile.close()
