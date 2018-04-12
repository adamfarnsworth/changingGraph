# Tkinter animate via canvas.move(obj, xAmount, yAmount)
import tkinter as tk
import time
from random import *
import random



class nodeCordinates:
    x = 0
    y = 0
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

class nLine:
    #nodes its connected to
    n1 = 0
    n2 = 0

    def __init__(self, a, b):
        self.n1 = a
        self.n2 = b

class equation:
    ##slope, but might not need it
    #m = 0

    #distances for movement
    xd = 0
    yd = 0
    def __init__(self, x1, y1, x2, y2):
        #self.m = (y1 -y2)/(x1 - x2)
        self.xd = x2 - x1
        self.yd = y2 - y1



#------------------
# Globals
#------------------
w = 400
h = 400
a = 25
b = 35
c = 45
d = 55
nSize = 4 # remove
root = tk.Tk()
canvas = tk.Canvas(root, width=w, height=h, bg = "black")
canvas.pack()
rctList = []# remove

# holds all nodes
cList = []

# hold cordinates of corresponding node
start = []
end = []

# holds equations for movement
movement = []

# holds all lines
lList = []

# holds all line cordinates
lcList = []
#------------------
#------------------


# canvas.create_rectangle(x0, y0, x1, y1, option, ...  )
# x0, y0, x1, y1 are corner coordinates of ulc to lrc diagonal

#------------------
# remove all this
#------------------
#rc1 = canvas.create_rectangle(20, 260, 120, 360, outline='white', fill='blue')
#rctList.append(rc1)
#rc1 = canvas.create_rectangle(20, 10, 120, 110, outline='white', fill='red')
#rctList.append(rc1)
#line = canvas.create_line(25, 35, 45, 55, fill = "green", width = 5)
#------------------
#------------------
def node(x,y):
    size = 5
    return canvas.create_oval(x + size, y + size, x - size, y - size, fill = "green2")

def newCords():
    x = randint(5, w - 5)
    y = randint(5, h - 5)
    return nodeCordinates(x,y)



#------------------
# Creating initial graph
#------------------
for i in range(6):
    x = randint(5, w - 5)
    y = randint(5, h - 5)
    circle = node(x,y)
    #circle = canvas.create_oval(x0 + nSize, y0 + nSize, x0 - nSize, y0 -
    #nSize, fill = "green")
    cList.append(circle)
    cord = nodeCordinates(x,y)
    start.append(cord)
end = start


# creating line cordinates
availableNodes = list(range(0, int(len(cList))))
master = availableNodes[:]
for i in range(0, len(cList)):
    curNode = random.choice(availableNodes)
    availableNodes.remove(curNode)
    temp = master[:]
    temp.remove(curNode)
    shuffle(temp)
    n = randint(2, 5)
    for j in range(0,n):
        lcList.append(nLine(j, temp.pop()))

# creating lines
for i in range(0, len(lcList)):
    s = lcList[i].n1
    e = lcList[i].n2
    lList.append(canvas.create_line(start[s].x, start[s].y, end[e].x, end[e].y, fill = "green2", width = 2))
    #lList.append(lineNew)


#------------------
#------------------
a1 = 22
a2 = 33
a3 = 44
a4 = 55
adam = canvas.create_line(a1, a2, a3, a4, fill = "blue", width = 5)

while True:

    start = end
    end = []
    movement = []

    # creating endpoints for nodes
    for i in range(0, len(start)):
        end.append(newCords())
        movement.append(equation(start[i].x, start[i].y, end[i].x, end[i].y))

    # moving everything
    for x in range(50):
        y = x = 5

        #a+=x
        #b+=x
        #c+=x
        #d+=x
        time.sleep(0.025)
        #if x == 40:
        #canvas.delete(line)
        #line = canvas.create_line(a, b, c, d, fill = "green", width = 5)
        a1+=5
        a2+=5
        a3+=5
        a4+=5
        canvas.coords(adam, a1, a2, a3, a4)
                

        # moving nodes
        for i in range(0, len(cList)):
            canvas.move(cList[i], movement[i].xd / 50, movement[i].yd / 50)
            
        #moving lines
       # tempLineList = lList[:]
        for j in range(0, len(lList)):
            #canvas.delete(lList[j])
            s = lcList[j].n1
            e = lcList[j].n2
            a = start[s].x + i * movement[s].xd / 50
            b = start[s].y + i * movement[s].yd / 50
            c = end[e].x + i * movement[e].xd / 50
            d = end[e].y + i * movement[e].yd / 50
            
            canvas.coords(lList[j], a, b, c, d)
            canvas.coords(adam, a1, a2, a3, a4)
            #lList[j] = canvas.create_line(a, b, c, d, fill = "blue", width =
            #5)
            #lList[j] = line
            
        

        canvas.update()
    time.sleep(1)
root.mainloop()



