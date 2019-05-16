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

maxGen = 0
for x in dataList:
    if len(x) > maxGen:
        maxGen = len(x)

newData = [[0,0,0] for x in range(maxGen)]
for x in dataList:
    for y in x:
        i = x.index(y)
        if newData[i] != [0,0,0]:
            avg0 = (y[0]+newData[i][0])/2
            avg1 = (y[1]+newData[i][1])/2
            avg2 = (y[2]+newData[i][2])/2
            newData[i] = [avg0,avg1,avg2]
        else:
            newData[i] = y
for x in range(len(newData)):
    c = newData[x]
    newData[x] = [int(c[0]),int(c[1]),int(c[2])]
staDev = [[0,0,0,0,0,0] for x in range(len(newData))]
for x in range(len(newData)):
    for y in dataList:
        if len(y) > x:
            staDev[x][0] += (y[x][0]-newData[x][0])**2
            staDev[x][3] += 1
            staDev[x][1] += (y[x][1]-newData[x][1])**2
            staDev[x][4] += 1
            staDev[x][2] += (y[x][2]-newData[x][2])**2
            staDev[x][5] += 1
        else:
            #pass
            staDev[x][0] += (0)**2
            staDev[x][1] += (0)**2
            staDev[x][2] += (0)**2
for x in range(len(staDev)):
    staDev[x][0] = int(math.sqrt(staDev[x][0]/staDev[x][3]))
    staDev[x][1] = int(math.sqrt(staDev[x][1]/staDev[x][4]))
    staDev[x][2] = int(math.sqrt(staDev[x][2]/staDev[x][5]))
#Wipe()
gen = 0
W = 1400
H = 600
Z = 20
def gene():
    global gen, newData, W, H, Z, staDev
    L.config(text="R: " + str(int(newData[gen][0])) + " C: " + str(newData[1]) + " P: " + str(newData[2]))
    L2.config(text="Gen: " + str(gen))
    C.create_rectangle(gen*18+15+Z,  (H-20),                                      gen*18+20+Z,  (H-20)-int(newData[gen][0])*3,               fill="blue")
    C.create_line(     gen*18+17.5+Z,(H-20-int(newData[gen][0])*3),               gen*18+17.5+Z,(H-20-int(newData[gen][0])*3)-staDev[gen][0],fill="blue")
    C.create_line(     gen*18+15+Z,  (H-20-int(newData[gen][0])*3)-staDev[gen][0],gen*18+20+Z,  (H-20-int(newData[gen][0])*3)-staDev[gen][0],fill="blue")
    
    C.create_rectangle(gen*18+20+Z,  (H-20),                                      gen*18+25+Z,  (H-20)-int(newData[gen][1])*3,               fill="red")
    C.create_line(     gen*18+22.5+Z,(H-20-int(newData[gen][1])*3),               gen*18+22.5+Z,(H-20-int(newData[gen][1])*3)-staDev[gen][1],fill="red")
    C.create_line(     gen*18+20+Z,  (H-20-int(newData[gen][1])*3)-staDev[gen][1],gen*18+25+Z,  (H-20-int(newData[gen][1])*3)-staDev[gen][1],fill="red")
    
    C.create_rectangle(gen*18+25+Z,  (H-20),                                      gen*18+30+Z,  (H-20)-int(newData[gen][2])*3,               fill="green")
    C.create_line(     gen*18+27.5+Z,(H-20-int(newData[gen][2])*3),               gen*18+27.5+Z,(H-20-int(newData[gen][2])*3)-staDev[gen][2],fill="green")
    C.create_line(     gen*18+25+Z,  (H-20-int(newData[gen][2])*3)-staDev[gen][2],gen*18+30+Z,  (H-20-int(newData[gen][2])*3)-staDev[gen][2],fill="green")
    
    gen += 1
    if (gen)%5 == 0:
        C.create_text(gen*18+20+Z,H-10,text=gen)
    master.update()
master = tkinter.Tk()
master.geometry("%dx%d+%d+%d" % (W+100,H+100,0,0))
B = tkinter.Button(master,command=gene,text="Next Gen.")
B.grid(row=1,column=0, sticky="N")
L = tkinter.Label(master,text="R: " + str(int(newData[gen][0])) + " P: " + str(int(newData[gen][1])))
L.grid(row=0,column=1, sticky="W")
L2 = tkinter.Label(master,text="Gen: " + str(gen))
L2.grid(row=0,column=0)
C = tkinter.Canvas(master,width=W,height=H)
C.grid(row=1,column=1)
for x in range(0,H,50):
    C.create_text(10,H-x*3-20,text=x)
C.create_rectangle(gen*18+15+Z,(H-20),gen*18+20+Z,(H-20)-newData[gen][0]*3,fill="blue")
C.create_rectangle(gen*18+20+Z,(H-20),gen*18+25+Z,(H-20)-newData[gen][1]*3,fill="red")
C.create_rectangle(gen*18+25+Z,(H-20),gen*18+30+Z,(H-20)-newData[gen][2]*3,fill="green")
for x in range(len(newData)):
    gene()
print(gen)
