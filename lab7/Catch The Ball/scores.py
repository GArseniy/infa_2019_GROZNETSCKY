import tkinter as tk
import Catch_The_Ball as Ctb
from saving import saver


HEIGHT = 400
WIDTH = 400


def time_is_up():
    '''1. Надпись "Время вышло"
       2. По истечении 200 единиц времени переключение на одно из меню в зависимости от результата'''
    global root_copy
    fra0 = tk.Frame(root_copy, bg="PowderBlue", bd=5)
    fra0.grid(row=0, column=0)
    tk.Label(fra0, text="Время вышло!", font="Times 26",
                                             bg="PowderBlue", fg="SteelBlue", width=20, height=1).pack()
    fra = tk.Frame(root_copy, width=WIDTH, height=HEIGHT, bg="PowderBlue", bd=84)
    fra.grid(row=1, column=0)
    
    def timer():
        '''Отсчитывает 200 единиц времени и сменяет надпись "Время вышло" на одно из меню в зависимости от результата "'''
        global time_milliseconds, result_copy
        end = 0
        if time_milliseconds < 200:
            time_milliseconds += 1
        else:
            end = 1
            with open("data.txt", mode='r', encoding='utf-8') as data:
                record = data.readline()[0:-1]
            if result_copy < int(record):
                not_saving_menu(root_copy, result_copy)
            else:
                saving_menu(root_copy)
        if not end:
            root_copy.after(10, timer)
    timer()


def saving_menu(root):
    '''Меню сохранения рекорда:
       Включает в себя строку для ввода своего имени, рекорды и кнопку выхода в меню'''
    def button1(event):
        '''Обработчик нажатия на кнопку but1'''
        global root_copy, name, result_copy
        name = name.get()
        saver(result_copy, name)
        Ctb.main(root_copy)
    global name
    canvas = tk.Canvas(root, bg="PowderBlue", height=HEIGHT, width=WIDTH)
    canvas.grid(row=0, column=0)
    
    fra = tk.Frame(canvas, bg="PowderBlue", bd=84)
    fra.grid(row=1, column=0)
    
    fra0 = tk.Frame(canvas, bg="PowderBlue", bd=5)
    fra0.grid(row=0, column=0)
    tk.Label(fra0, text="Ты побил рекорд!\n Введи имя на латинице:", font="Times 26",
             bg="PowderBlue", fg="SteelBlue", width=20).pack()
    
    name = tk.Entry(fra0, width=20, bd=3, bg="SteelBlue", fg="PowderBlue")
    name.pack()
    
    but1 = tk.Button(fra, text="Сохранить", font="Times 15",
                     bg="SteelBlue", fg="PowderBlue", width=20, height=1)
    but1.bind("<Button-1>", button1)
    but1.pack()
    tk.Label(fra, text="", bg="PowderBlue", width=5, height=1).pack()

    root.mainloop()


def not_saving_menu(root, result_copy):
    '''Меню проигрыша:
       Показывает рекорды и предлагает перейти в главное меню'''
    def button2(event):
        '''Обработчик нажатия на кнопку but2'''
        global root_copy
        Ctb.main(root_copy)
    canvas = tk.Canvas(root, bg="PowderBlue", height=HEIGHT, width=WIDTH)
    canvas.grid(row=0, column=0)
    
    fra = tk.Frame(canvas, bg="PowderBlue", bd=84)
    fra.grid(row=1, column=0)

    fra0 = tk.Frame(canvas, bg="PowderBlue", bd=5)
    fra0.grid(row=0, column=0)

    tk.Label(fra0, text="Твой результат:  " + str(result_copy), font="Times 26",
             bg="PowderBlue", fg="SteelBlue", width=20).pack()
    
    with open('data.txt', 'r', encoding='utf-8') as data:
        records = data.readlines()
        
    good_records = records[5][0:-1] + ':  ' + records[4] \
        + records[3][0:-1] + ':  ' + records[2] \
        + records[1][0:-1] + ':  ' + records[0]
    
    tk.Label(fra, text=good_records, font="Times 25",
             bg="PowderBlue", fg="SteelBlue").pack()
    but1 = tk.Button(fra, text="Главное меню", font="Times 15",
                     bg="SteelBlue", fg="PowderBlue", width=20, height=1)
    but1.bind("<Button-1>", button2)
    but1.pack()
    tk.Label(fra, text="", bg="PowderBlue", width=5, height=1).pack()

    root.mainloop()

    
def main(root, result):
    '''Вызов необходимых функций'''
    global root_copy, result_copy, time_milliseconds
    root_copy = root
    result_copy = result
    time_milliseconds = 0
    time_is_up()        
    root.mainloop()
