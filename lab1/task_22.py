#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    height = 1
    while not wall_is_beneath():
        move_down()
        height += 1
    while not wall_is_above():
        move_up()
    width = 1
    while not wall_is_on_the_right():
        move_right()
        width += 1
    while not wall_is_on_the_left():
        move_left()
    for i in range(height):
        for j in range(width - 1):
            fill_cell()
            move_right()
        fill_cell()
        for j in range(width - 1):
            move_left()
        if not wall_is_beneath(): move_down()
        
if __name__ == '__main__':
    run_tasks()
