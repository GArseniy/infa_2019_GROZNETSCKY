#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_2_2():
    def cross(x, y):
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
    y = 2
    for x in range(1, 21, 4):
        cross(x, y)
    move_right(x - 1)
    move_down(y - 1)
    
if __name__ == '__main__':
    run_tasks()
