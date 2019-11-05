import turtle
n=0
r=10
turtle.shape('turtle')
for i in range(10):    
    turtle.penup()
    turtle.right(90)
    turtle.forward(r)
    turtle.right(90)
    turtle.forward(r)
    turtle.right(180)
    turtle.pendown()
    turtle.forward(n+2*r)
    turtle.left(90)    
    turtle.forward(n+2*r)
    turtle.left(90)
    turtle.forward(n+2*r)
    turtle.left(90)
    turtle.forward(n+2*r)
    turtle.left(90)
    n=n+2*r
