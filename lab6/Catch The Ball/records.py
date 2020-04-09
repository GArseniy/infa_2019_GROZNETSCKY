import tkinter as tk
import Catch_The_Ball as ctb

HEIGHT = 400
WIDTH = 400

def button1(event):
    global root_copy, canvas
    canvas.delete(tk.ALL)
    ctb.main(root_copy)

def main(root):
    global root_copy, canvas
    root_copy = root
    canvas = tk.Canvas(root, bg = "PowderBlue", height = HEIGHT, width = WIDTH)
    canvas.grid(row=0,column=0)
    
    fra0 = tk.Frame(canvas, bg = "PowderBlue", bd = 5)
    fra0.pack()

    fra = tk.Frame(canvas, bg = "PowderBlue", bd = 84)
    fra.pack()
    
    tk.Label(fra0, text = "Рекорды:", font = "Times 26",
             bg = "PowderBlue", fg = "SteelBlue", width = 20).pack()

    with open('data.txt','r',encoding = 'utf-8') as data:
        records = data.readlines()
        
    good_records = records[5][0:-1] + ':  ' + records[4] + records[3][0:-1] + ':  ' + records[2] + records[1][0:-1] + ':  ' + records[0]
    
    tk.Label(fra, text = good_records, font = "Times 25",
             bg = "PowderBlue", fg = "SteelBlue").pack()
    but1 = tk.Button(fra,text="Главное меню",font = "Times 15",
                      bg="SteelBlue",fg="PowderBlue",width = 20, height = 1)
    but1.bind("<Button-1>",button1)
    but1.pack()
    tk.Label(fra, text = "", bg = "PowderBlue",width = 5, height = 1).pack()

    root.mainloop()
if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(0, 0)
    main(root)
