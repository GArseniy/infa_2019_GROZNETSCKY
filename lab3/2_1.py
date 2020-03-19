from graph import*
from math import*
""" Фон """
windowSize(455, 300)
canvasSize(455, 300)
penColor("lightskyblue")
brushColor("lightskyblue")
rectangle(0, 0, 455, 150)
penColor("forestgreen")
brushColor("forestgreen")
rectangle(0, 150, 455, 300)
""" Домик """
penColor("black")
brushColor("darkgoldenrod")
rectangle(70, 120, 180, 197)
penColor("black")
brushColor("darkcyan")
rectangle(70 + 40, 120 + 25, 180 - 40, 197 - 25)
penColor("black")
brushColor("brown")
polygon([(70, 120), (125, 70), (180, 120), (70, 120)])
""" Дерево """
penColor("black")
brushColor("saddlebrown")
rectangle(345, 140, 355, 190)
penColor("black")
brushColor("green")
circle(350, 100, 15)
circle(333, 115, 15)
circle(367, 115, 15)
circle(350, 125, 15)
circle(335, 140, 15)
circle(365, 140, 15)
""" Рисование звезды по рассчитанным координатам вершин """
n = 20
r = 40
r1 = 0.8 * r
A = [(0,0)]*n*2
for k in range(n):
    x = 400 + r * cos(2 * pi * k / n)
    y = 50 + r * sin(2 * pi * k / n)
    A[k*2] = (x,y)
    x1 = 400 + r1 * cos(2 * pi * k / n + pi / n)
    y1 = 50 + r1 * sin(2 * pi * k / n + pi / n)
    A[k*2+1] = (x1,y1)
penColor("black")
brushColor("yellow")
polygon(A)
""" Облако """
penColor("black")
brushColor("white")
circle(200, 50, 15)
circle(215, 50, 15)
circle(230, 50, 15)
circle(245, 50, 15)
circle(230, 38, 15)
circle(215, 38, 15)
run()
