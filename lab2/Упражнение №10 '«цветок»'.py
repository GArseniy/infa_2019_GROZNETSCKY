import turtle

def paint_circle():

    for i in range(360):
        
        turtle.forward(1)
        turtle.left(1)
turtle.shape('turtle')      
for i in range(6):
    paint_circle()
    turtle.right(360/6)
    
