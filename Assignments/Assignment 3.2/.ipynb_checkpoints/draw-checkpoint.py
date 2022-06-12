#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import sys

s = turtle.getscreen() 
t = s.turtles()[0]

s.title("Turtle Program!")
t.pen(shown=False)

# Handle CLA here
color, shape, *etc = tuple(sys.argv[1:]) #This can be rewritten using Argparse

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

