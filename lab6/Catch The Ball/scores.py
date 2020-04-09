import tkinter as tk
import Catch_The_Ball as ctb
from saving import saver

HEIGHT = 400
WIDTH = 400

def button1(event):
    global root_copy, name, result_copy
    name = name.get()
    saver(result_copy, name)
    ctb.main(root_copy)

def button2(event):
    global root_copy
    ctb.main(root_copy)

def time_is_up():
    global root_copy
    fra0 = tk.Frame(root_copy, bg = "PowderBlue", bd = 5)
    fra0.grid(row=0,column=0)
    tk.Label(fra0, text = "Время вышло!", font = "Times 26",
                 bg = "PowderBlue", fg = "SteelBlue", width = 20, height = 1).pack()
    fra = tk.Frame(root_copy, width = WIDTH, height = HEIGHT, bg = "PowderBlue", bd = 84)
    fra.grid(row=1,column=0)
    
    def timer():
        global time_miliseconds, result_copy
        end = 0
        if time_miliseconds < 200: time_miliseconds += 1
        else:
            end = 1
            with open("data.txt", mode = 'r', encoding = 'utf-8') as data:
                record = data.readline()[0:-1]
            if result_copy < int(record): not_saving_menu(root_copy, result_copy)
            else: saving_menu(root_copy, result_copy)
        if not end: root_copy.after(10, timer)
    timer()


def saving_menu(root, result):
    global name
    canvas = tk.Canvas(root, bg = "PowderBlue", height = HEIGHT, width = WIDTH)
    canvas.grid(row=0,column=0)
    
    fra = tk.Frame(canvas, bg = "PowderBlue", bd = 84)
    fra.grid(row=1,column=0)
    
    fra0 = tk.Frame(canvas, bg = "PowderBlue", bd = 5)
    fra0.grid(row=0,column=0)
    tk.Label(fra0, text = "Ты побил рекорд!\n Введи имя на латинице:", font = "Times 26",
             bg = "PowderBlue", fg = "SteelBlue", width = 20).pack()
    
    name = tk.Entry(fra0, width = 20, bd = 3,bg="SteelBlue",fg="PowderBlue")
    name.pack()
    
    but1 = tk.Button(fra,text="Сохранить",font = "Times 15",
                      bg="SteelBlue",fg="PowderBlue",width = 20, height = 1)
    but1.bind("<Button-1>",button1)
    but1.pack()
    tk.Label(fra, text = "", bg = "PowderBlue",width = 5, height = 1).pack()

    root.mainloop()
def not_saving_menu(root, result_copy):
    
    canvas = tk.Canvas(root, bg = "PowderBlue", height = HEIGHT, width = WIDTH)
    canvas.grid(row=0,column=0)
    
    fra = tk.Frame(canvas, bg = "PowderBlue", bd = 84)
    fra.grid(row=1,column=0)

    fra0 = tk.Frame(canvas, bg = "PowderBlue", bd = 5)
    fra0.grid(row=0,column=0)

    tk.Label(fra0, text = "Твой результат:  " + str(result_copy), font = "Times 26",
             bg = "PowderBlue", fg = "SteelBlue", width = 20).pack()
    
    with open('data.txt','r',encoding = 'utf-8') as data:
        records = data.readlines()
        
    good_records = records[5][0:-1] + ':  ' + records[4] + records[3][0:-1] + ':  ' + records[2] + records[1][0:-1] + ':  ' + records[0]
    
    tk.Label(fra, text = good_records, font = "Times 25",
             bg = "PowderBlue", fg = "SteelBlue").pack()
    but1 = tk.Button(fra,text="Главное меню",font = "Times 15",
                      bg="SteelBlue",fg="PowderBlue",width = 20, height = 1)
    but1.bind("<Button-1>",button2)
    but1.pack()
    tk.Label(fra, text = "", bg = "PowderBlue",width = 5, height = 1).pack()

    root.mainloop()

    
def main(root, result):
    global root_copy, result_copy, time_miliseconds
    root_copy = root
    result_copy = result
    time_miliseconds = 0
    time_is_up()        
    root.mainloop()

    
if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(0, 0)
    main(root, 0)
