import turtle

def paint_spring(size):

    for i in range(180):
        turtle.forward(size)
        turtle.right(1)
        
turtle.shape('turtle')        
turtle.left(90)     
i=0
while i < 10:
    i+=1
    if i%2 == 1:
        paint_spring(1)

    else:
        paint_spring(0.2)
    
