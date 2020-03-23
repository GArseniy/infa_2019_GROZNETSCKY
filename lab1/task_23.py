#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_6_6():
    lenght = 0
    while not wall_is_on_the_right():
        move_right()
        lenght += 1
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                fill_cell()
            while not wall_is_beneath():
                move_down()
    move_left(lenght)
        
if __name__ == '__main__':
    run_tasks()
