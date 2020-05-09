import tkinter as tk
import Catch_The_Ball as Ctb

HEIGHT = 400
WIDTH = 400


def button1(event):
    '''По нажатию кнопки but1 вызывается эта функция, а соответственно и Ctb.main -- запуск главного меню'''
    global root_copy, canvas
    canvas.delete(tk.ALL)
    Ctb.main(root_copy)


def init_and_show():
    '''Описание инициализации и отображения виждетов на холсте'''
    global root_copy, canvas
#   '''Инициализация'''
    canvas = tk.Canvas(root_copy, bg="PowderBlue", height=HEIGHT, width=WIDTH)
    fra0 = tk.Frame(canvas, bg="PowderBlue", bd=5)
    fra = tk.Frame(canvas, bg="PowderBlue", bd=84)
    with open('data.txt', 'r', encoding='utf-8') as data:
        records = data.readlines()
    good_records = records[5][0:-1] + ':  ' + records[4] \
                   + records[3][0:-1] + ':  ' + records[2] \
                   + records[1][0:-1] + ':  ' + records[0]
    but1 = tk.Button(fra, text="Главное меню", font="Times 15",
                     bg="SteelBlue", fg="PowderBlue", width=20, height=1)
    but1.bind("<Button-1>", button1)
#   '''Отображение'''
    canvas.grid(row=0, column=0)
    fra0.pack()
    fra.pack()
    tk.Label(fra0, text="Рекорды:", font="Times 26", bg="PowderBlue", fg="SteelBlue", width=20).pack()
    tk.Label(fra, text=good_records, font="Times 25",
             bg="PowderBlue", fg="SteelBlue").pack()
    but1.pack()
    tk.Label(fra, text="", bg="PowderBlue", width=5, height=1).pack()

    root_copy.mainloop()


def main(root):
    '''Запуск инициализации и отображения виджетов на холсте'''
    global root_copy
    root_copy = root
    init_and_show()
