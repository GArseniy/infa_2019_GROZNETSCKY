from graph import*
import math
import random
def sun(x0, y0, radius_of_sun, n, percent):
    A = [(0,0)] * n * 2
    for k in range(n):
        A[k * 2] = (x0 + radius_of_sun * math.cos(2 * math.pi * k / n), y0 + radius_of_sun * math.sin(2 * math.pi * k / n))
        A[k * 2 + 1] = (x0 + radius_of_sun * percent * math.cos(2 * math.pi * k / n + math.pi / n), y0 + radius_of_sun * percent * math.sin(2 * math.pi * k / n + math.pi / n))
    penColor("black")
    brushColor("yellow")
    polygon(A)
def tree(x_t, y_t, age):
    penColor("black")
    brushColor("saddlebrown")
    rectangle(x_t - age / 2, y_t - age * 5, x_t + age / 2, y_t)
    penColor("black")
    brushColor("green")
    circle(x_t, y_t - age * 9, age * 1.5)
    circle(x_t + age * 1.7, y_t - age * 7.5, age * 1.5)
    circle(x_t - age * 1.7, y_t - age * 7.5, age * 1.5)
    circle(x_t, y_t - age * 6.5, age * 1.5)
    circle(x_t - age * 1.5, y_t - age * 5, age * 1.5)
    circle(x_t + age * 1.5, y_t - age * 5, age * 1.5)
def house(x_h, y_h, width, height):
    penColor("black")
    brushColor("darkgoldenrod")
    rectangle(x_h - width / 2, y_h - height, x_h + width / 2, y_h)
    penColor("black")
    brushColor("darkcyan")
    rectangle(x_h - width / 8, y_h - height * 5 / 8, x_h + width / 8, y_h - height * 3 / 8)
    penColor("black")
    brushColor("brown")
    polygon([(x_h - width/2, y_h - height), (x_h, y_h - height * 1.7), (x_h + width / 2, y_h - height), (x_h - width/2, y_h - height)])
def cloud(x_c, y_c, radius):
    penColor("black")
    brushColor("white") 
    return circle(x_c, y_c, radius), circle(x_c + radius, y_c, radius), circle(x_c + radius * 2, y_c, radius), circle(x_c + radius * 3, y_c, radius), circle(x_c + radius * 2, y_c - radius * 0.8, radius), circle(x_c + radius, y_c - radius * 0.8, radius)
def motion_of_clouds():
    for i in range(quantity):
        for j in range(6):
            moveObjectBy(clouds[i][j], 5, 0)
            if xCoord(clouds[i][1]) > x_of_window + 18:
                clouds[i] = (cloud(-3 * radiusis[i], random.randrange(20, 130), radiusis[i]))
                house(110, 220, 110, 80)
                tree(200, 210, 10)
                house(300, 200, 70, 50)
                tree(360, 190, 7)
x_of_window = 455
y_of_window = 300
windowSize(x_of_window, y_of_window)
canvasSize(x_of_window, y_of_window)
penColor("lightskyblue")
brushColor("lightskyblue")
rectangle(0, 0, x_of_window, y_of_window / 2)
penColor("forestgreen")
brushColor("forestgreen")
rectangle(0, y_of_window / 2, x_of_window, y_of_window)
sun(50, 50, 40, 20, 0.3)
quantity = 7
radiusis = []
clouds = []
for i in range(quantity):
    radiusis.append(random.randrange(10, 18))
    clouds.append(cloud(-x_of_window * (i + 1) / quantity, random.randrange(20, 130), radiusis[i]))
house(110, 220, 110, 80)
tree(200, 210, 10)
house(300, 200, 70, 50)
tree(360, 190, 7)
onTimer(motion_of_clouds, 40)
run()
