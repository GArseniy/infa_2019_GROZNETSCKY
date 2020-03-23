#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
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
    cross(2, 2)
    move_down()
    move_right()
if __name__ == '__main__':
    run_tasks()
