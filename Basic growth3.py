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
Si = 4
Sp = 8
W = 50+genNum*(3*Sp+3)#1400
H = 600
Z = 20


###Generation Number###
genNum = 50#input("How many generations?\n>>> ")


###Open Save Data###
dataFile = open(r"Data.txt",mode="r")
exec(dataFile.read())
dataFile.close()
testNum = dataList[-1]
dataList = dataList[:-1]


###Start Values###
cType = "K0"#input("K or R?\n>>> ").upper()
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


###Generation Function###
def Gene(gen, cPop, pPop, cResources, fruit,pResources):
    global proColor, conColor, conRes, proRes, bacColor, W, H, Z, Si, Sp, dataList, testNum
    global B, L, L2, C, cType
    gen += 1


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
    C.create_rectangle(gen*(3*Sp+3)+Si+Z,(H-20),gen*(3*Sp+3)+2*Si+Z,(H-20)-(int(pResources)*3),fill=proRes,outline="")
    C.create_rectangle(gen*(3*Sp+3)+2*Si+Z,(H-20),gen*(3*Sp+3)+3*Si+Z,(H-20)-(int(cResources)*3),fill=conRes,outline="")
    C.create_rectangle(gen*(3*Sp+3)+3*Si+Z,(H-20),gen*(3*Sp+3)+4*Si+Z,(H-20)-len(cPop)*3,fill=conColor,outline="")
    C.create_rectangle(gen*(3*Sp+3)+4*Si+Z,(H-20),gen*(3*Sp+3)+5*Si+Z,(H-20)-len(pPop)*3,fill=proColor,outline="")
    if (gen)%5 == 0:
        C.create_text(gen*(3*Sp+3)+3*Si+Z,H-10,text=gen)
    master.update()
    

    ###Return###
    return gen, cPop, pPop, cResources, fruit, pResources


###Test Function###
def Test():
    global proColor, conColor, conRes, proRes, bacColor, W, H, Z, Si, Sp, dataList, testNum
    global B, L, L2, C, genNum, gen, cPop, pPop, cResources, fruit, cType, pResources
    dataList.insert(0,[])
    C.delete("all")
    L.config(text="pR: " + str(int(pResources)) + " cR: " + str(int(cResources)) + " C: " + str(len(cPop)) + " P: " + str(len(pPop)))
    L2.config(text="Gen: " + str(gen))
    B.config(command=partial(Gene, gen, cPop, pPop, cResources, fruit,pResources))
    for x in range(0,H,50):
        C.create_text(10,H-x*3-20,text=x)
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
testNum = int(input("How many tests?\n>>> "))
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


###Write Save Data###
dataList.append(testNum)
newFile = open(r"Data.txt",mode="w")
newFile.write("dataList = " + str(dataList))
newFile.close()

