import turtle
import math

def paint_polygon(n,r): 
    a=2*r*math.sin( math.radians(180 / n ))/l
    k=(n-2)/n*180
    turtle.forward(a)  
    for i in range ((n-1)//359):
        turtle.left(180-k)
        turtle.forward(a)

turtle.shape('turtle')               
n = 360
l = 50
for r in range (1,5000):
    paint_polygon(n,r)

    
