import random
import time
import tkinter

resources = 100
pop = 1
gen = 0
def gene():
    global gen
    global pop
    global resources
    resources += 10
    gen += 1
    for x in range(pop):
        if resources > 2:
            resources -= 2
        else:
            pop -= 1
    for x in range(pop):
        if resources > 5:
            pop += 1
            resources -= 5
    L.config(text="R: " + str(resources) + " P: " + str(pop))
    master.update()
master = tkinter.Tk()
B = tkinter.Button(master,command=gene,text="Next Gen.")
B.grid(row=1,column=0, sticky="N")
L = tkinter.Label(master,text="R: " + str(resources) + " P: " + str(pop))
L.grid(row=0,column=1, sticky="W")
L2 = tkinter.Label(master,text="Gen: " + str(gen))
L2.grid(row=0,column=0)
C = tkinter.Canvas(master,width=400,height=400)
C.grid(row=1,column=1)
