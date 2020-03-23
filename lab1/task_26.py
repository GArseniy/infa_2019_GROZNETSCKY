#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_2_4():
    def cross(x, y):
        if y > 1:
            move_down(y-1)
        move_right(x)
        fill_cell()
        move_right()
        move_down()
        fill_cell()
        move_down()
        move_left()
        fill_cell()
        move_left()
        move_up()
        fill_cell()
        move_right()
        fill_cell()
        move_up(y)
        move_left(x)
    n = 10
    k = 5
    for x in range(1, 1 + (n - 1) * 4 + 1, 4):
        for y in range(1, 1 + (k - 1) * 4 + 1, 4):
            cross(x, y)
    move_down(y - 1)


if __name__ == '__main__':
    run_tasks()
