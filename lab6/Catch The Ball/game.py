import tkinter as tk
from random import randrange as rnd, choice
import scores


HEIGHT = 400
WIDTH = 400


class Ball:
    def __init__(self):
        ball_colors = ['Blue', 'MediumBlue', 'DarkBlue', 'Navy', 'MidnightBlue']
        self.color = choice(ball_colors)
        self.r = rnd(15, 30)
        self.x = rnd(self.r, WIDTH - self.r)
        self.y = rnd(self.r, HEIGHT - self.r)
        self.dx = rnd(-10, 10)
        self.dy = rnd(-10, 10)
        self.ball_id = canvas.create_oval(self.x-self.r, self.y-self.r,
                                          self.x+self.r, self.y+self.r,
                                          fill=self.color, width=0)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if not self.r <= self.x <= WIDTH - self.r:
            self.dx = -self.dx
        if not self.r <= self.y <= HEIGHT - self.r:
            self.dy = -self.dy
            
    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def ball_tick():
    global root_copy, end
    for ball in balls:
        ball.move()
        ball.show()
    if not end:
        root_copy.after(50, ball_tick)
    else:
        canvas.delete(tk.ALL)
        scores.main(root_copy, result)


def click(event):
    def ball_click(event):
        global canvas, balls, result
        i = 0
        for ball in balls:
            if ((ball.x - event.x) ** 2 + (ball.y - event.y) ** 2) ** 0.5 < ball.r:
                canvas.delete(ball.ball_id)
                new_ball = Ball()
                balls[i] = new_ball
                result += 2
            i += 1

    ball_click(event)


def timer():
    global canvas, time_seconds, time_milliseconds, result, root_copy, end
    if time_milliseconds < 99:
        time_milliseconds += 1
        root_copy.title('0:' + str(time_seconds) + ':' + str(time_milliseconds)
                        + '   ' + "Your score: " + str(result))
    elif time_seconds < 9:
        time_seconds += 1
        time_milliseconds = 0
    else:
        end = 1
    if not end:
        root_copy.after(10, timer)
    

def main(root):
    global canvas, balls, result, time_seconds, time_milliseconds,  root_copy, end
    end = 0
    result = 0
    time_seconds = 0
    time_milliseconds = 0
    root_copy = root

    canvas = tk.Canvas(root, bg="PowderBlue", height=HEIGHT + 35, width=WIDTH)
    canvas.grid(row=0, column=0)

    n = 10
    balls = [Ball() for i in range(n)]
    ball_tick()
    timer()
    canvas.bind('<Button-1>', click)
    root.mainloop()
