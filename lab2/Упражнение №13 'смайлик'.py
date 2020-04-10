import turtle

def paint_spring(size):       
    turtle.color('red')
    for i in range(18):
        turtle.forward(size)
        turtle.right(10)

def paint_circle(size,color):
    turtle.begin_fill()        
    turtle.color('red', color)
    for i in range(36):
        turtle.left(10)
        turtle.forward(size)
    turtle.end_fill()
turtle.shape('turtle')        
paint_circle(10,'yellow')
turtle.end_fill()

turtle.penup()
turtle.left(115)
turtle.forward(72)
turtle.right(115)
turtle.pendown()

paint_circle(2,'red')

turtle.penup()
turtle.forward(54)
turtle.pendown()

paint_circle(2,'red')

turtle.penup()
turtle.right(170)
turtle.forward(28)
turtle.left(80)
turtle.pendown()

turtle.width(3)
turtle.forward(28)

turtle.penup()
turtle.left(80)
turtle.forward(22)
turtle.right(85)
turtle.pendown()

paint_spring(4)

turtle.penup()
turtle.goto(1000,1000)
turtle.pendown()
