import turtle

def setwindowsize(x=640, y=640):
    turtle.setup(x, y)
    turtle.setworldcoordinates(0,0,x,y)

def drawpixel(x, y, color, pixelsize = 1 ):
    turtle.tracer(0, 0)
    turtle.colormode(255)
    turtle.penup()
    turtle.setpos(x*pixelsize,y*pixelsize)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(pixelsize)
        turtle.right(90)
    turtle.end_fill()

def showimage():
    turtle.hideturtle()
    turtle.update()
    
################
# Example 1

setwindowsize(200, 200)
drawpixel(100, 100, (255,0,0) )
showimage()

################
# Example 2

from random import *

setwindowsize(300,300)

for x in range(30):
    for y in range(30):
        color = (randint(0,255),randint(0,255),randint(0,255))
        drawpixel(x,y,color,10)

while True:
    showimage()