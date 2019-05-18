###Import Modules###
import random
import tkinter
import time
from functools import partial
from Consumer2 import Consumer, Producer


###Generation Number###
genNum = 100#input("How many generations?\n>>> ")


###Aesthetic Variables###
proColor = "forest green"
conColor = "firebrick3"
resColor = "steelblue"
bacColor = "gainsboro"
Si = 6
Sp = 7
W = 50+genNum*(3*Sp+3)#1400
H = 600
Z = 20
#genNum = 50


###Open Save Data###
dataFile = open(r"Data.txt",mode="r")
exec(dataFile.read())
dataFile.close()
testNum = dataList[-1]
dataList = dataList[:-1]


###Start Values###
gen = 0
cPop = [Consumer()]
pPop = [Producer()]
resources = 100
fruit  = 0

def Gene():
    print("oof")

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
def Gene(gen, cPop, pPop, resources, fruit):
    global proColor, conColor, resColor, bacColor, W, H, Z, Si, Sp, dataList, testNum
    global B, L, L2, C
    gen += 1


    ### K Resources Generation###
    #resources += 100- resources


    ### R Resource Generation###
    resources += random.randint(0,30)
    
    
    ###Consumer Growth###
    cPop.sort()
    for x in cPop:
        x.grow()
        if x.age >= x.deadAge:
            cPop.remove(x)
        elif resources <= 0:
            cPop.remove(x)
        else:
            resources -= 1


    ### K Consumer Reproduction###
    """
    for x in cPop:
        if x.reproductive == 1:
            if resources > 20 and random.randint(0,1) == 0:
                cPop.append(Consumer())
                resources -= 5
    """
    ### R Consumer Reproduction###

    z = 0
    while resources > 0 and z < len(cPop)*5:
        cPop.append(Consumer())
        resources -= 1
        z += 1

        
    ###Data Add###
    dataList[0].append([int(resources),len(cPop),len(pPop)])


    ###Graphics Update###
    L.config(text="R: " + str(int(resources)) + " C: " + str(len(cPop)) + " P: " + str(len(pPop)))
    L2.config(text="Gen: " + str(gen))
    B.config(command=partial(Gene, gen, cPop, pPop, resources, fruit))
    C.create_rectangle(gen*(3*Sp+3)+Si+Z,(H-20),gen*(3*Sp+3)+2*Si+Z,(H-20)-int(resources)*3,fill=resColor,outline="")
    C.create_rectangle(gen*(3*Sp+3)+2*Si+Z,(H-20),gen*(3*Sp+3)+3*Si+Z,(H-20)-len(cPop)*3,fill=conColor,outline="")
    C.create_rectangle(gen*(3*Sp+3)+3*Si+Z,(H-20),gen*(3*Sp+3)+4*Si+Z,(H-20)-len(pPop)*3,fill=proColor,outline="")
    if (gen)%5 == 0:
        C.create_text(gen*(3*Sp+3)+2.5*Si+Z,H-10,text=gen)
    master.update()
    

    ###Return###
    return gen, cPop, pPop, resources, fruit


###Test Function###
def Test():
    global proColor, conColor, resColor, bacColor, W, H, Z, Si, Sp, dataList, testNum
    global B, L, L2, C, genNum, gen, cPop, pPop, resources, fruit
    dataList.insert(0,[])
    C.delete("all")
    L.config(text="R: " + str(int(resources)) + " C: " + str(len(cPop)) + " P: " + str(len(pPop)))
    L2.config(text="Gen: " + str(gen))
    B.config(command=partial(Gene, gen, cPop, pPop, resources, fruit))
    for x in range(0,H,50):
        C.create_text(10,H-x*3-20,text=x)
    for x in range(genNum):
        y = Gene(gen, cPop, pPop, resources, fruit)
        gen = y[0]
        cPop = y[1]
        pPop = y[2]
        resources = y[3]
        fruit = y[4]
        if len(cPop) <= 0:
            break
    testNum += 1


###Run Tests###
testNum = 100#input("How many tests?\n>>> ")
for x in range(int(testNum)):
    Test()
    gen = 0
    cPop = [Consumer()]
    pPop = [Producer()]
    resources = 100
    fruit  = 0
    time.sleep(0.01)


###Write Save Data###
dataList.append(testNum)
newFile = open(r"Data.txt",mode="w")
newFile.write("dataList = " + str(dataList))
newFile.close()

