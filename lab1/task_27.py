#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    i = 1
    move_right(1)
    fill_cell()
    while not wall_is_on_the_right():
        fill_cell()
        for k in range(i):
            if not wall_is_on_the_right(): move_right(1)
        i += 1

if __name__ == '__main__':
    run_tasks()
