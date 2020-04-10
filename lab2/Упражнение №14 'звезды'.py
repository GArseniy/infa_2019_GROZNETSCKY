import turtle
import math

def paint_polygon(n):
    
    a=100
    k=180/n

    turtle.left(180)
    turtle.forward(a)
       
    for i in range (n-1):
        turtle.left(180-k)
        turtle.forward(a)

    turtle.right(k)
    
turtle.shape('turtle')
paint_polygon(5)

turtle.penup()
turtle.forward(200)
turtle.pendown()

paint_polygon(11)
