#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    width = 27
    height = 12
    move_right()
    for i in range(int(height / 2)):
        for j in range(width - 1):
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        for j in range(width - 1):
            fill_cell()
            move_left()
        fill_cell()
        move_down()

if __name__ == '__main__':
    run_tasks()
