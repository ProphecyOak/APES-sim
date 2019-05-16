import tkinter

newFile = open(r"Data.txt",mode="r")
exec(newFile.read())
newFile.close()
def Wipe():
    newFile = open(r"Data.txt",mode="w")
    newFile.write("dataList = [0]")
    newFile.close()
dataList = dataList[:-1]

newData = []
for x in dataList:
    for y in x:
        i = x.index(y)
        if len(newData) <= i:
            newData.append(y)
for x in dataList:
    for y in x:
        i = x.index(y)
        avg0 = (y[0]+newData[i][0])/2
        avg1 = (y[1]+newData[i][1])/2
        newData[i] = [avg0,avg1]
for x in range(len(newData)):
    c = newData[x]
    newData[x] = [int(c[0]),int(c[1])]
#Wipe()
print(newData)
gen = 1
W = 1400
H = 600
Z = 20
def gene():
    global gen, newData, W, H, Z
    L.config(text="R: " + str(int(newData[gen][0])) + " P: " + str(newData[gen][1]))
    L2.config(text="Gen: " + str(gen))
    C.create_rectangle(gen*13+15+Z,(H-20),gen*13+20+Z,(H-20)-int(newData[gen][0])*3,fill="blue")
    C.create_rectangle(gen*13+20+Z,(H-20),gen*13+25+Z,(H-20)-newData[gen][1]*3,fill="red")
    gen += 1
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
C.create_rectangle(gen*13+15+Z,(H-20),gen*13+20+Z,(H-20)-newData[gen][0]*3,fill="blue")
C.create_rectangle(gen*13+20+Z,(H-20),gen*13+25+Z,(H-20)-newData[gen][1]*3,fill="red")
for x in range(100):
    gene()
