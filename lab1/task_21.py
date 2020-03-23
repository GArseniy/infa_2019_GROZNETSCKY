#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down()
    for i in range(1,14):
        for k in range(i):
            move_right()
            fill_cell()
        for k in range(i):
            move_left()
        move_down()
    move_right()
    
if __name__ == '__main__':
    run_tasks()
