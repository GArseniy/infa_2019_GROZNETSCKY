import turtle
import math

def paint_polygon(n,r): 
    a=2*r*math.sin( math.radians(180 / n ))/m
    k=(n-2)/n*180
    turtle.forward(a)  
    turtle.left(180-k)

turtle.shape('turtle')               
n = 360
m = 10
for r in range (1,5000):
    paint_polygon(n,r)
# m - the inverse pitch of the helix
# r - the radius of the spiral, it increases evenly
# n - the number of vertices of a polygon inscribed in a circle of radius r
# k - the angle of rotation of a turtle
                  
