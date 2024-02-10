import tkinter as tk
import math
import copy
#import numpy

#creating the window and canvas using the tkinter library
window = tk.Tk()
window.geometry("1000x500")
canvas = tk.Canvas(window, width=1000, height=500, bg="white")
canvas.grid(column=0, row=0)

t = 0


def line(x,z):
    global t
    #y = ((math.sin(0.05*x + 10*z + 10*t) *11) + (math.sin(0.1*z + 10*z + 0.1*t) * 10)  + (math.sin(0.01*x + 10*z + 10*t) * 10) + (math.sin(2*z + 10*z + 10*t) * 5) + (math.sin(0.1*x + 10*z + 10*t) * 5)+ (math.sin(0.2*x + 10*z + 10*t) * 3)+ (math.sin(0.05*x + 10*z + 10*t) * 15))*1.5 + 250 + 5*z
    y = ((math.sin(0.05*x*0.05*t + z + 10*t) *11) + (math.sin(0.1*z + z + 0.1*t) * 10)  + (math.sin(0.01*x + z + 10*t) * 10) + (math.sin(2*z + z + 10*t) * 5) + (math.sin(0.1*x + z + 10*t) * 5)+ (math.sin(0.2*x + z + 10*t) * 3)+ (math.sin(0.05*x + z + 10*t) * 15))*0.08*z + 350 + 4*z
    return y


def wave():
    global t,lineArray
    canvas.delete("wave")
    for z in range(10):
        lineArray = [ [None]*2 for i in range(250)]
        for x in range(250):
            y = line(x,z)
            #lineArray.append([x*4,y])
            lineArray[x][0] = copy.deepcopy(x*4)
            lineArray[x][1] = copy.deepcopy(int(y))
            #print(lineArray)
            #print(lineArray)
            canvas.create_rectangle(x*4-2,y,x*4+2,500,fill="#17dce3",outline="#17dce3",tag="wave")
            #canvas.create_rectangle(x*4-2,y,x*4+2,500,fill="#0d5fa6",outline="#0d5fa6",tag="wave")
            #canvas.create_rectangle(x*4-2,y,x*4+2,y+50,fill="#338ec2",outline="#338ec2",tag="wave")
            #canvas.create_rectangle(x*4-2,y,x*4+2,y+30,fill="#5abddf",outline="#5abddf",tag="wave")
            #canvas.create_rectangle(x*4-2,y,x*4+2,y+10,fill="#81ecfc",outline="#81ecfc",tag="wave")
        
        canvas.create_line(lineArray,fill="#0a35f7",width = 2,tag="wave")
        #canvas.create_line(lineArray,fill="#72daf1",width = 2,tag="wave")
        
    t += 0.02
    canvas.after(2,wave)

wave()

