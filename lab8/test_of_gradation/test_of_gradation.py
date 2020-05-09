from graph import *

x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
rectangle (x1, y1, x2, y2)
h = (x2 - x1) / (N + 1)
hc = 255 // N
x = x1
c = 0
for i in range(N):
  brushColor(c, 0, 0)
  rectangle(x, y1, x+h, y2)
  x += h
  c += hc

run()
