#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_9_3():
    n = 1
    while not wall_is_on_the_right():
        move_right()
        n += 1
    for j in range(n-2, 0, -2):
        for i in range(j):
            move_down()
            fill_cell()
        move_down()
        for i in range(j):
            move_left()
            fill_cell()
        move_left()
        for i in range(j):
            move_up()
            fill_cell()
        move_up()
        for i in range(j):
            move_right() 
            fill_cell()
        move_down()
    move_down(int((n - 1) / 2))
    move_left(int((n - 1) / 2))

if __name__ == '__main__':
    run_tasks()
