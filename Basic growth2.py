import random
import time
import tkinter
from Consumer2 import Consumer

resources = 100
pop = [Consumer()]
gen = 1
oldResources = 100
maxPop = 1
W = 1400
H = 600
Z = 20
newFile = open(r"Data.txt",mode="r")
exec(newFile.read())
newFile.close()
testNum = dataList[-1]
dataList = dataList[:-1]
def Test():
    global gen, pop, gen, oldResources, maxPop, W, H, Z, resources, dataList, testNum
    dataList.insert(0,[])
    
    def gene():
        global gen,pop, gen, oldResources, maxPop, W, H, Z, resources, dataList, testNum
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
        gen += 1
        if resources < len(pop):
            for y in range(len(pop)-resources):
                maxAge = 0
                oldest = 0
                for x in pop:
                    if x.age > maxAge:
                        oldest = x
                        maxAge = x.age
                pop.remove(oldest)
        for x in pop:
                resources -= 1
                if x.grow() == "D":
                    pop.remove(x)
        for x in pop:
            if resources > 20 and random.randint(0,1) == 0 and x.reproductive == 1:
                pop.append(Consumer())
                resources -= 5
        L.config(text="R: " + str(int(resources)) + " P: " + str(len(pop)))
        L2.config(text="Gen: " + str(gen))
        C.create_rectangle(gen*13+15+Z,(H-20),gen*13+20+Z,(H-20)-int(resources)*3,fill="blue")
        C.create_rectangle(gen*13+20+Z,(H-20),gen*13+25+Z,(H-20)-len(pop)*3,fill="red")

        dataList[0].append([resources,len(pop)])
        
        if (gen)%5 == 0:
            C.create_text(gen*13+20+Z,H-10,text=gen)
        master.update()        
    master = tkinter.Tk()
    master.geometry("%dx%d+%d+%d" % (W+100,H+100,0,0))
    B = tkinter.Button(master,command=gene,text="Next Gen.")
    B.grid(row=1,column=0, sticky="N")
    L = tkinter.Label(master,text="R: " + str(int(resources)) + " P: " + str(int(len(pop))))
    L.grid(row=0,column=1, sticky="W")
    L2 = tkinter.Label(master,text="Gen: " + str(gen))
    L2.grid(row=0,column=0)
    C = tkinter.Canvas(master,width=W,height=H)
    C.grid(row=1,column=1)
    for x in range(0,H,50):
        C.create_text(10,H-x*3-20,text=x)
    C.create_rectangle(gen*13+15+Z,(H-20),gen*13+20+Z,(H-20)-resources*3,fill="blue")
    C.create_rectangle(gen*13+20+Z,(H-20),gen*13+25+Z,(H-20)-len(pop)*3,fill="red")

    
    for x in range(99):
        gene()
    resources = 100
    pop = [Consumer()]
    gen = 1
    oldResources = 100
    print(maxPop)
    maxPop = 1
    W = 1400
    H = 600
    Z = 20
    popZ = 0
    testNum += 1
    master.destroy()
for x in range(1000):
    Test()
    print("\nTest:",testNum)
character = 0
for x in range(len(str(testNum))):
    if dataList[x] == ",":
        character = x
dataList.append(testNum)
newFile = open(r"Data.txt",mode="w")
newFile.write("dataList = " + str(dataList))
newFile.close()
