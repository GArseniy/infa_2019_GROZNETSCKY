#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if wall_is_above():
        if wall_is_beneath():
            if wall_is_on_the_left():
                if wall_is_on_the_right():
                    print('error')
                else: move_right()
            else: move_left()
        else: move_down()
    else: move_up()

if __name__ == '__main__':
    run_tasks()
