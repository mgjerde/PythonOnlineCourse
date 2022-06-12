#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import sys
import argparse

s = turtle.getscreen() 
t = s.turtles()[0]

s.title("Turtle Program!")
t.pen(shown=False)

# Handle CLA here
def checkshape(shape):
    if shape in ["square","circle","triangle"]:
        return shape
    else:
        print("Unrecognised shape, defaulting to square")
        return "square"

def checkcolor(color):
    if color in ["red","white","blue"]:
        return color
    else:
        print("Unrecognised color, defaulting to black")
        return "black"

parser = argparse.ArgumentParser()
parser.add_argument("color", help="What color to fill the inner shape with.")
parser.add_argument("shape", help="What kind of shape to be drawn. (supported shapes: square, circle and triangle)", type=checkshape)
parser.add_argument("--pencolor", default="black", help="What color to use for the outer pen.",type=checkcolor)

args = parser.parse_args()

color = args.color
shape = args.shape
pencolor = args.pencolor
t.pencolor(pencolor)

t.pensize(2)
t.fillcolor(color) # Use help(turtle.Turtle.fillcolor) to see what are acceptable colors!

if (shape=="square"):  
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.end_fill()

elif (shape=="circle"):
    t.begin_fill()
    t.circle(50)
    t.end_fill()

elif (shape=="triangle"):
    t.begin_fill()
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.end_fill()

else:
    print("Unknown shape!")

turtle.done()
quit()


# %%
