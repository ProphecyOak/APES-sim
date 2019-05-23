###Import Modules###
import random
import tkinter
import time
from functools import partial
from Consumer2 import Consumer, Producer


genNum = 50

###Aesthetic Variables###
proColor = "forest green"
conColor = "firebrick3"
conRes = "steelblue"
proRes = "maroon"
bacColor = "gainsboro"
Si = 12
Sp = 30
W = 1800#50+genNum*(3*Sp+3)
H = 600
Z = 20
barNum = 2#int(input("How many bars?\n>>> "))
barCount = 0


###Generation Number###
genNum = 0#int(input("How many generations?\n>>> "))


###Open Save Data###
dataFile = open(r"Data.txt",mode="r")
exec(dataFile.read())
dataFile.close()
testNum = dataList[-1]
dataList = dataList[:-1]


###Start Values###
cType = "K0"#input("K0 or KP or R0 or RP?\n>>> ").upper()
if cType in ["KP","RP"]:
    if barNum == 3:
        barNum = 2
else:
    if barNum > 2:
        barNum = 2
gen = 0
if cType in ["K0","KP"]:
    cPop = [Consumer()]#K
elif cType in ["R0","RP"]:
    cPop = [Consumer(3)]#R
pPop = [Producer()]
cResources = 100
if cType in ["KP","RP"]:
    pResources = 100
fruit  = 0


###Place Holder Function###
def Gene():
    pass
def ThanosSnap():
    pass

###Set-Up Graphics###
master = tkinter.Tk()
master.geometry("%dx%d+%d+%d" % (W,H+30,0,0))
B = tkinter.Button(master,command=Gene,text="Next Gen.")
B.grid(row=0,column=2, sticky="N")
L = tkinter.Label(master)
L.grid(row=0,column=1, sticky="W")
L2 = tkinter.Label(master)
L2.grid(row=0,column=0)
C = tkinter.Canvas(master,width=W,height=H,bg=bacColor)
C.grid(row=1,column=0,columnspan=30)

def barMake(num,co,gen):
    global C, barNum, Si, Sp, Z, H, barCount
    C.create_rectangle(gen*(barNum*Si+Sp)+barCount*Si+Z,(H-20),gen*(barNum*Si+Sp)+(barCount+1)*Si+Z,(H-20)-(int(num)*3),fill=co,outline="")
    barCount += 1

###Generation Function###
def Gene(gen, cPop, pPop, cResources, fruit,pResources):
    global proColor, conColor, conRes, proRes, bacColor, W, H, Z, Si, Sp, dataList, testNum
    global B, B2, L, L2, C, cType, barNum, barCount
    gen += 1
    print(gen)

    ### K cResources Generation###
    if cType == "K0":
        cResources += 100 - cResources + random.randint(0,1)


    ### R Resource Generation###
    elif cType == "R0":
        if gen%10 == 0:
            cResources += 50 + random.randint(-5,5)
        else:
            cResources += 2 + random.randint(0,1)
            if cResources < 0:
                cResources = 0

    
    ###Producer Resources Generation###
    if cType in ["KP","RP"]:
        pResources += (gen%10)*10 + random.randint(0,5)
        for x in pPop:
            if pResources > 0:
                cResources += 2
                pResources -= 1
        
        
    ###Consumer Growth###
    cPop.sort(reverse=True)
    for x in cPop:
        x.grow()
        if cResources > 0:
            cResources -= 1
            if x.age >= x.deadAge:
                cPop.remove(x)
        else:
            cPop.remove(x)


    ###Producer Growth###
    if cType in ["KP","RP"]:
        pPop.sort(reverse=True)
        for x in pPop:
            x.grow()
            if pResources > 0:
                pResources -= 1
                if x.age > x.deadAge:
                    pPop.remove(x)
            else:
                pPop.remove(x)


    ### K Consumer Reproduction###
    if cType in ["K0","KP"]:
        for x in cPop:
            if x.reproductive == 1 and cResources > 20 and random.randint(0,1) == 0:
                cPop.append(Consumer())
                if cType in ["K0","KP"]:
                    cResources -= 5

                
    ### R Consumer Reproduction###
    elif cType in ["R0","RP"]:
        z = 0
        while cResources > 0 and z < len(cPop):
            cPop.append(Consumer())
            cResources -= 1
            z += 1


    ###Producer Reproduction###
    for x in pPop:
        if x.reproductive == 1 and pResources > 10:
            for x in range(random.randint(0,10)):
                pPop.append(Producer())
                pResources -= 1
    
        
    ###Data Add###
    dataList[0].append([int(cResources),len(cPop),len(pPop),int(pResources)])


    ###Graphics Update###
    L.config(text="pR: " + str(int(pResources)) + " cR: " + str(int(cResources)) + " C: " + str(len(cPop)) + " P: " + str(len(pPop)))
    L2.config(text="Gen: " + str(gen))
    B.config(command=partial(Gene, gen, cPop, pPop, cResources, fruit, pResources))
    barMake(len(cPop),conColor, gen)
    if barNum > 1 and cType not in ["KP","RP"]:
        barMake(cResources,conRes, gen)
    elif barNum > 1:
        barMake(len(pPop),proColor, gen)
    if barNum > 3:
        barMake(cResources,conRes, gen)
        barMake(pResources,proRes, gen)
    barCount = 0
    barCount = 0
    if (gen)%5 == 0:
        C.create_text(gen*(barNum*Si+Sp)+barNum*Si/2+Z,H-10,text=gen)
    B.config(command=partial(Gene, gen, cPop, pPop, cResources, fruit, pResources))
    B2.config(command=partial(ThanosSnap,gen))
    master.update()
    

    ###Return###
    return gen, cPop, pPop, cResources, fruit, pResources


def ThanosSnap(gen):
    global proColor, conColor, conRes, proRes, bacColor, W, H, Z, Si, Sp, dataList, testNum
    global B, B2, L, L2, C, genNum, cPop, pPop, cResources, fruit, cType, pResources, barCount
    gen += 1
    print(gen)
    print(len(cPop),len(pPop))
    #pPop = random.choices(pPop,k=len(pPop)//2)
    cPop = random.choices(cPop,k=len(cPop)//2)
    print(len(cPop),len(pPop))

    ###Data Add###
    dataList[0].append([int(cResources),len(cPop),len(pPop),int(pResources)])


    ###Graphics Update###
    L.config(text="pR: " + str(int(pResources)) + " cR: " + str(int(cResources)) + " C: " + str(len(cPop)) + " P: " + str(len(pPop)))
    L2.config(text="Gen: " + str(gen))
    B.config(command=partial(Gene, gen, cPop, pPop, cResources, fruit, pResources))
    barMake(len(cPop),conColor, gen)
    if barNum > 1 and cType not in ["KP","RP"]:
        barMake(cResources,conRes, gen)
    elif barNum > 1:
        barMake(len(pPop),proColor, gen)
    if barNum > 3:
        barMake(cResources,conRes, gen)
        barMake(pResources,proRes, gen)
    barCount  = 0
    B.config(command=partial(Gene, gen, cPop, pPop, cResources, fruit, pResources))
    B2.config(command=partial(ThanosSnap,gen))
    if (gen)%5 == 0:
        C.create_text(gen*(barNum*Si+Sp)+barNum*Si/2+Z,H-10,text=gen)
    master.update()
    return gen


B2 = tkinter.Button(master,command=partial(ThanosSnap,gen),text="Thanos Snap!")
B2.grid(row=0,column=3, sticky="N")


###Test Function###
def Test():
    global proColor, conColor, conRes, proRes, bacColor, W, H, Z, Si, Sp, dataList, testNum
    global B, B2, L, L2, C, genNum, gen, cPop, pPop, cResources, fruit, cType, pResources
    dataList.insert(0,[])
    C.delete("all")
    L.config(text="pR: " + str(int(pResources)) + " cR: " + str(int(cResources)) + " C: " + str(len(cPop)) + " P: " + str(len(pPop)))
    L2.config(text="Gen: " + str(gen))
    B.config(command=partial(Gene, gen, cPop, pPop, cResources, fruit,pResources))
    for x in range(0,H,50):
        C.create_text(20,H-x*3-20,text=x)
    for x in range(genNum):
        y = Gene(gen, cPop, pPop, cResources, fruit, pResources)
        gen = y[0]
        cPop = y[1]
        pPop = y[2]
        cResources = y[3]
        pResources = y[5]
        fruit = y[4]
        if len(cPop) <= 0 or len(pPop) <= 0:
            break
    testNum += 1


###Run Tests###
testNum = 1#int(input("How many tests?\n>>> "))
for x in range(int(testNum)):
    cPop = []
    if cType in ["K0","KP"]:
        cPop = [Consumer()]
    elif cType in ["R0","RP"]:
        cPop = [Consumer(3)]
    pPop = [Producer()]
    cResources = 100
    pResources = 0
    if cType in ["KP","RP"]:
        pResources = 100
    fruit  = 0
    gen = 0
    #time.sleep(0.01)
    print(x)
    Test()
    B2.config(command=partial(ThanosSnap,gen))


###Write Save Data###
dataList.append(testNum)
newFile = open(r"Data.txt",mode="w")
newFile.write("dataList = " + str(dataList))
newFile.close()

