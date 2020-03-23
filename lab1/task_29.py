#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    while not wall_is_on_the_right():
        k = 0
        for i in range(3):  
            if cell_is_filled():
                k += 1
                if k == 3: break
                if not wall_is_on_the_right():
                    move_right()
                else: break
        if k == 3: break
        if not wall_is_on_the_right(): move_right()
        else: break

if __name__ == '__main__':
    run_tasks()
