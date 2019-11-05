import turtle
import math

def paint_polygon(n,r):
    
    a=2*r*math.sin( math.radians(180 / n ))
    k=(n-2)/n*180

    turtle.left(180-k/2)
    turtle.forward(a)
       
    for i in range (n-1):
        turtle.left(180-k)
        turtle.forward(a)

    turtle.right(k/2)
    
turtle.shape('turtle')              
r=10
for j in range (3,12):
    paint_polygon(j,r)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    r+=10
    
