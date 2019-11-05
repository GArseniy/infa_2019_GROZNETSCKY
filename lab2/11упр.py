import turtle

def paint_circle_left(size):
    for i in range(36):
        turtle.forward(size)
        turtle.left(10)
def paint_circle_right(size):
    for i in range(36):
        turtle.forward(size)
        turtle.right(10)

turtle.shape('turtle')       
turtle.left(90)
for k in range(1,10):
    paint_circle_left(k)
    paint_circle_right(k)
