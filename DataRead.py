import tkinter
import math

newFile = open(r"Data.txt",mode="r")
exec(newFile.read())
newFile.close()
def Wipe():
    newFile = open(r"Data.txt",mode="w")
    newFile.write("dataList = [0]")
    newFile.close()
dataList = dataList[:-1]
proColor = "forest green"
conColor = "firebrick3"
conRes = "steelblue"
proRes = "maroon"
bacColor = "gainsboro"
maxGen = 0
for x in dataList:
    if len(x) > maxGen:
        maxGen = len(x)

newData = [[0,0,0,0] for x in range(maxGen)]
for x in dataList:
    for y in x:
        i = x.index(y)
        if newData[i] != [0,0,0,0]:
            avg0 = (y[0]+newData[i][0])/2
            avg1 = (y[1]+newData[i][1])/2
            avg2 = (y[2]+newData[i][2])/2
            avg3 = (y[3]+newData[i][3])/2
            newData[i] = [avg0,avg1,avg2,avg3]
        else:
            newData[i] = y
for x in range(len(newData)):
    c = newData[x]
    newData[x] = [int(c[0]),int(c[1]),int(c[2]),int(c[3])]
staDev = [[0,0,0,0,0,0,0,0] for x in range(len(newData))]
for x in range(len(newData)):
    for y in dataList:
        if len(y) > x:
            staDev[x][0] += (y[x][0]-newData[x][0])**2
            staDev[x][4] += 1
            staDev[x][1] += (y[x][1]-newData[x][1])**2
            staDev[x][5] += 1
            staDev[x][2] += (y[x][2]-newData[x][2])**2
            staDev[x][6] += 1
            staDev[x][3] += (y[x][3]-newData[x][3])**2
            staDev[x][7] += 1
        else:
            staDev[x][0] += (0)**2
            staDev[x][1] += (0)**2
            staDev[x][2] += (0)**2
            staDev[x][3] += (0)**2
for x in range(len(staDev)):
    staDev[x][0] = int(math.sqrt(staDev[x][0]/staDev[x][4]))
    staDev[x][1] = int(math.sqrt(staDev[x][1]/staDev[x][5]))
    staDev[x][2] = int(math.sqrt(staDev[x][2]/staDev[x][6]))
    staDev[x][3] = int(math.sqrt(staDev[x][3]/staDev[x][7]))

Avgs = [[],[],[],[]]
for x in range(5,len(newData)):
    for y in dataList:
        if len(y) > x:
            Avgs[0].append(y[x][0])
            Avgs[1].append(y[x][1])
            Avgs[2].append(y[x][2])
            Avgs[3].append(y[x][3])
Avgs[0] = sum(Avgs[0])/len(Avgs[0])
Avgs[1] = sum(Avgs[1])/len(Avgs[1])
Avgs[2] = sum(Avgs[2])/len(Avgs[2])
Avgs[3] = sum(Avgs[3])/len(Avgs[3])
print(Avgs)
#Wipe()
gen = 0
W = 2155
H = 600
Z = 20
Si = 8
Sp = 4
def gene():
    global gen, newData, W, H, Z, staDev
    L.config(text="R: " + str(int(newData[gen][0])) + " C: " + str(newData[gen][1]) + " P: " + str(newData[gen][2]))
    L2.config(text="Gen: " + str(gen))
    C.create_rectangle(gen*(3*Si+3)+Sp+Z,(H-20),gen*(3*Si+3)+2*Sp+Z,(H-20)-int(newData[gen][0])*3,fill=conRes,outline="")
    C.create_line(gen*(3*Si+3)+1.5*Sp+Z,(H-20-int(newData[gen][0])*3),gen*(3*Si+3)+Sp*1.5+Z,(H-20-int(newData[gen][0])*3)-staDev[gen][0],fill=conRes)
    C.create_line(gen*(3*Si+3)+Sp+Z,(H-20-int(newData[gen][0])*3)-staDev[gen][0],gen*(3*Si+3)+2*Sp+Z,(H-20-int(newData[gen][0])*3)-staDev[gen][0],fill=conRes)
    
    C.create_rectangle(gen*(3*Si+3)+2*Sp+Z,(H-20),gen*(3*Si+3)+3*Sp+Z,(H-20)-int(newData[gen][1])*3,fill=conColor,outline="")
    C.create_line(gen*(3*Si+3)+2.5*Sp+Z,(H-20-int(newData[gen][1])*3),gen*(3*Si+3)+2.5*Sp+Z,(H-20-int(newData[gen][1])*3)-staDev[gen][1],fill=conColor)
    C.create_line(gen*(3*Si+3)+2*Sp+Z,(H-20-int(newData[gen][1])*3)-staDev[gen][1],gen*(3*Si+3)+3*Sp+Z,(H-20-int(newData[gen][1])*3)-staDev[gen][1],fill=conColor)
    
    C.create_rectangle(gen*(3*Si+3)+3*Sp+Z,(H-20),gen*(3*Si+3)+4*Sp+Z,(H-20)-int(newData[gen][2])*3,fill=proColor,outline="")
    C.create_line(gen*(3*Si+3)+3.5*Sp+Z,(H-20-int(newData[gen][2])*3),gen*(3*Si+3)+3.5*Sp+Z,(H-20-int(newData[gen][2])*3)-staDev[gen][2],fill=proColor)
    C.create_line(gen*(3*Si+3)+3*Sp+Z,(H-20-int(newData[gen][2])*3)-staDev[gen][2],gen*(3*Si+3)+4*Sp+Z,(H-20-int(newData[gen][2])*3)-staDev[gen][2],fill=proColor)

    C.create_rectangle(gen*(3*Si+3)+4*Sp+Z,(H-20),gen*(3*Si+3)+5*Sp+Z,(H-20)-int(newData[gen][3])*3,fill=proRes,outline="")
    C.create_line(gen*(3*Si+3)+4.5*Sp+Z,(H-20-int(newData[gen][3])*3),gen*(3*Si+3)+4.5*Sp+Z,(H-20-int(newData[gen][3])*3)-staDev[gen][3],fill=proRes)
    C.create_line(gen*(3*Si+3)+4*Sp+Z,(H-20-int(newData[gen][3])*3)-staDev[gen][3],gen*(3*Si+3)+5*Sp+Z,(H-20-int(newData[gen][3])*3)-staDev[gen][3],fill=proRes)
    
    gen += 1
    if (gen)%5 == 0:
        C.create_text(gen*(3*Si+3)+3*Sp+Z,H-10,text=gen)
    master.update()
master = tkinter.Tk()
master.geometry("%dx%d+%d+%d" % (W,H+30,0,0))
B = tkinter.Button(master,command=gene,text="Next Gen.")
B.grid(row=0,column=2, sticky="N")
L = tkinter.Label(master,text="R: " + str(int(newData[gen][0])) + " P: " + str(int(newData[gen][1])))
L.grid(row=0,column=1, sticky="W")
L2 = tkinter.Label(master,text="Gen: " + str(gen))
L2.grid(row=0,column=0)
C = tkinter.Canvas(master,width=W,height=H,bg=bacColor)
C.grid(row=1,column=0,columnspan=30)
for x in range(0,H,50):
    C.create_text(10,H-x*3-20,text=x)
C.create_rectangle(gen*(3*Si+3)+Sp+Z,(H-20),gen*(3*Si+3)+2*Sp+Z,(H-20)-newData[gen][0]*3,fill=conRes,outline="")
C.create_rectangle(gen*(3*Si+3)+2*Sp+Z,(H-20),gen*(3*Si+3)+3*Sp+Z,(H-20)-newData[gen][1]*3,fill=conColor,outline="")
C.create_rectangle(gen*(3*Si+3)+3*Sp+Z,(H-20),gen*(3*Si+3)+4*Sp+Z,(H-20)-newData[gen][2]*3,fill=proColor,outline="")
C.create_rectangle(gen*(3*Si+3)+4*Sp+Z,(H-20),gen*(3*Si+3)+4*Sp+Z,(H-20)-newData[gen][2]*3,fill=proRes,outline="")
C.create_text(gen*(3*Si+3)+3*Sp+Z,H-10,text=gen)
for x in range(len(newData)):
    gene()
C.create_line(5*(3*Si+3)+Sp+Z,(H-20)-Avgs[0]*3,W,(H-20)-Avgs[0]*3,fill=conRes)
C.create_line(5*(3*Si+3)+Sp+Z,(H-20)-Avgs[1]*3,W,(H-20)-Avgs[1]*3,fill=conColor)
C.create_line(5*(3*Si+3)+Sp+Z,(H-20)-Avgs[2]*3,W,(H-20)-Avgs[2]*3,fill=proColor)
C.create_line(5*(3*Si+3)+Sp+Z,(H-20)-Avgs[3]*3,W,(H-20)-Avgs[3]*3,fill=proRes)
