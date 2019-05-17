###Import Modules###
import random
import tkinter
import time
from Consumer2 import Consumer, Producer


###Aesthetic Variables###
proColor = "forest green"
conColor = "firebrick3"
resColor = "steelblue"
bacColor = "gainsboro"
W = 1400
H = 600
Z = 20
Si = 6
Sp = 6


###Open Save Data###
dataFile = open(r"Data.txt",mode="r")
exec(dataFile.read())
dataFile.close()
testNum = dataList[-1]
dataList = dataList[:-1]


###Generation Number###
genNum = 50#input("How many generations?\n>>> ")


###Generation Function###
def Gene(gen, cPop, pPop, resources,fruit):
    global proColor, conColor, resColor, bacColor, W, H, Z, Si, Sp, dataList, testNum
    global B, L, L2, C
    gen += 1

    
    ###Stuff###
    cPop.sort()
    for x in cPop:
        x.grow()
        if x.age >= x.deadAge:
            cPop.remove(x)
        elif resources <= 0:
            cPop.pop(x)
        else:
            resources -= 1
    for x in cPop:
        if x.reproductive == 1:
            if resources > 20:
                cPop.append(Consumer())
                resources -= 5
        
    ###Data Add###
    dataList[0].append([int(resources),len(cPop),len(pPop)])


    ###Graphics Update###
    L.config(text="R: " + str(int(resources)) + " C: " + str(len(cPop)) + " P: " + str(len(pPop)))
    L2.config(text="Gen: " + str(gen))
    C.create_rectangle(gen*(3*Si+3)+Sp+Z,(H-20),gen*(3*Si+3)+2*Sp+Z,(H-20)-int(resources)*3,fill=resColor,outline="")
    C.create_rectangle(gen*(3*Si+3)+2*Sp+Z,(H-20),gen*(3*Si+3)+3*Sp+Z,(H-20)-len(cPop)*3,fill=conColor,outline="")
    C.create_rectangle(gen*(3*Si+3)+3*Sp+Z,(H-20),gen*(3*Si+3)+4*Sp+Z,(H-20)-len(pPop)*3,fill=proColor,outline="")
    if (gen)%5 == 0:
        C.create_text(gen*(3*Si+3)+2.5*Sp+Z,H-10,text=gen)
    master.update()
    

    ###Return###
    return gen, cPop, pPop, resources, fruit


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


###Test Function###
def Test():
    global proColor, conColor, resColor, bacColor, W, H, Z, Si, Sp, dataList, testNum
    global B, L, L2, C, genNum
    gen = 0
    resources = 100
    fruit = 0
    pPop = [Producer()]
    cPop = [Consumer()]
    dataList.insert(0,[])
    C.delete("all")
    L.config(text="R: " + str(int(resources)) + " C: " + str(len(cPop)) + " P: " + str(len(pPop)))
    L2.config(text="Gen: " + str(gen))
    for x in range(0,H,50):
        C.create_text(10,H-x*3-20,text=x)
    for x in range(genNum):
        y = Gene(gen, cPop, pPop, resources, fruit)
        gen = y[0]
        cPop = y[1]
        pPop = y[2]
        resources = y[3]
        fruit = y[4]
    testNum += 1


###Run Tests###
testNum = 100#input("How many tests?\n>>> ")
for x in range(int(testNum)):
    Test()


###Write Save Data###
dataList.append(testNum)
newFile = open(r"Data.txt",mode="w")
newFile.write("dataList = " + str(dataList))
newFile.close()

