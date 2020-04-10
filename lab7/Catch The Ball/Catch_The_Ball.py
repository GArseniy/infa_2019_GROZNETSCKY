import tkinter as tk
import game
import records


HEIGHT = 400
WIDTH = 400


def button1(event):
    '''Запуск игры по функции game.main по нажатию кнопки but1'''
    global canvas, root_copy
    canvas.delete(tk.ALL)
    game.main(root_copy)


def button2(event):
    '''Запуск меню "Рекорды" по функции records.main по нажатию кнопки but2'''
    global canvas, root_copy
    canvas.delete(tk.ALL)
    records.main(root_copy)


def button3(event):
    '''Закрытие программы по нажатию кнопки but3'''
    quit()


def init_and_show():
    '''Описание инициализации и отображениия виджетов на холсте'''
    global canvas, root_copy
#   '''Инициализация'''
    canvas = tk.Canvas(root_copy, bg="PowderBlue", height=HEIGHT, width=WIDTH)
    fra0 = tk.Frame(canvas, width=WIDTH, height=HEIGHT, bg="PowderBlue", bd=5)
    fra = tk.Frame(canvas, width=WIDTH, height=HEIGHT, bg="PowderBlue", bd=84)
    but1 = tk.Button(fra, text="Играть", font="Times 15", bg="SteelBlue", fg="PowderBlue", width=20, height=1)
    but1.bind("<Button-1>", button1)
    but2 = tk.Button(fra, text="Рекорды", font="Times 15", bg="SteelBlue", fg="PowderBlue", width=20, height=1)
    but2.bind("<Button-1>", button2)
    but3 = tk.Button(fra, text="Выход", font="Times 15", bg="SteelBlue", fg="PowderBlue", width=20, height=1)
    but3.bind("<Button-1>", button3)
#   '''Отображение'''
    canvas.grid(row=0, column=0)
    fra0.grid(row=0, column=0)
    fra.grid(row=1, column=0)
    tk.Label(fra0, text="THE GAME: Catch The Ball", font="Times 25", bg="PowderBlue", fg="SteelBlue").pack()
    but1.pack()
    tk.Label(fra, text="", bg="PowderBlue", width=5, height=1).pack()
    but2.pack()
    tk.Label(fra, text="", bg="PowderBlue", width=5, height=1).pack()
    but3.pack()
    tk.Label(fra, text="", bg="PowderBlue", width=5, height=3).pack()
    root_copy.mainloop()


def main(root):
    '''Вызов инициализации и отбражения на холсте виджетов'''
    global root_copy
    root_copy = root
    init_and_show()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT) + "+100+100")
    root.resizable(0, 0)
    root.title('Catch The Ball')
    main(root)
