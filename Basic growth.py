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
    resources += (100-resources)
    gen += 1
    for x in range(pop):
        if resources > 2:
            resources -= 2
        else:
            pop -= 1
    for x in range(pop):
        if resources > 20 and random.randint(0,1) == 0:
            pop += 1
            resources -= 5
    L.config(text="R: " + str(resources) + " P: " + str(pop))
    L2.config(text="Gen: " + str(gen))
    C.create_rectangle(gen*13+5+20,380,gen*13+10+20,380-resources*3,fill="blue")
    C.create_rectangle(gen*13+20,380,gen*13+5+20,380-pop*3,fill="red")
    if gen%5 == 0:
        C.create_text(gen*13+5+20,390,text=gen)
    master.update()
master = tkinter.Tk()
B = tkinter.Button(master,command=gene,text="Next Gen.")
B.grid(row=1,column=0, sticky="N")
L = tkinter.Label(master,text="R: " + str(resources) + " P: " + str(pop))
L.grid(row=0,column=1, sticky="W")
L2 = tkinter.Label(master,text="Gen: " + str(gen))
L2.grid(row=0,column=0)
C = tkinter.Canvas(master,width=800,height=400)
C.grid(row=1,column=1)
for x in range(0,300,50):
    C.create_text(10,400-x*3-20,text=x)
C.create_rectangle(gen*13+5+10+10,380,gen*13+10+10,380-resources*3,fill="blue")
C.create_rectangle(gen*13+10+10,380,gen*13+5+10,380-pop*3,fill="red")
