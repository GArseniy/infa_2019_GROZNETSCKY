import tkinter as tk
from random import randrange as rnd, choice


HEIGHT = 600
WIDTH = 1200


class Cannon:
    '''Пушка:    вращается вокруг точки - середины ширины пушки;
                 атрибуты:    id,
                              длина,
                              ширина,
                              цвет,
                              координаты,
                              синус и косинус угла между горизонтом и линией пушки.'''
    def __init__(self):
        '''Инициализация пушки:
           id,
           длина,
           ширина,
           цвет,
           координаты расчитываются по формулам - получается прямоугольник.'''
        global canvas
        self.length = 50
        self.width = 15
        self.color = 'black'
        sine = self.sine_of_angle_between_the_horizon_line_and_the_cannon_line = 1
        cosine = self.cosine_of_angle_between_the_horizon_line_and_the_cannon_line = 0

        self.x1, self.y1 = 100, HEIGHT - 100
        self.x2, self.y2 = self.x1 - sine * self.length, self.y1 - cosine * self.length
        self.x3, self.y3 = self.x2 + sine * self.width, self.y2 - cosine * self.width
        self.x4, self.y4 = self.x1 + sine * self.width, self.y1 - cosine * self.width
        self.cannon_id = canvas.create_polygon((self.x1, self.y1), (self.x2, self.y2),
                                               (self.x3, self.y3), (self.x4, self.y4), fill=self.color)

    def increasing_the_length_and_color_gradation_of_the_cannon(self):
        '''По нажатию левой кнопки мыши: плавное изменение цвета с черного на красный,
                                         увеличение длины пушки.
           По ее отпусканию возвращаются изначальные показатели'''
        global button_released, root_copy, red, cannonballs

        def from_rgb(rgb):
            """Конвертирует RGB."""
            return "#%02x%02x%02x" % rgb
        if not button_released:
            if self.length < 135:
                self.length += 1
                self.color = from_rgb((red, 0, 0))
                red += 3
            root_copy.after(20, self.increasing_the_length_and_color_gradation_of_the_cannon)
        else:
            cannonballs.append(Cannonball())
            self.length = 50
            red = 0
            self.color = 'black'


class Cannonball:
    def __init__(self):
        global cannon, canvas
        self.color = cannon.color
        self.r = 10
        sine = cannon.sine_of_angle_between_the_horizon_line_and_the_cannon_line
        cosine = cannon.cosine_of_angle_between_the_horizon_line_and_the_cannon_line
        self.x, self.y = cannon.x3 - cosine * cannon.width / 2, cannon.y3 + sine * cannon.width / 2
        self.dx, self.dy = (cannon.x3 - cosine * cannon.width / 2 - 100) // 12, \
                           (cannon.y3 + sine * cannon.width / 2 - HEIGHT + 100) // 12

        self.cannonball_id = canvas.create_oval(self.x - self.r, self.y - self.r,
                                                self.x + self.r, self.y + self.r, fill=self.color, width=0)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if not self.r <= self.x <= WIDTH - self.r:
            self.dx = -self.dx
        if not self.r <= self.y <= HEIGHT - self.r:
            self.dy = -self.dy

    def show(self):
        global canvas
        canvas.move(self.cannonball_id, self.dx, self.dy)


class Target:
    def __init__(self):
        pass

    def move(self):
        pass

    def show(self):
        pass


def checking_the_destruction_of_targets():
    pass


def cannon_tick():
    '''Тикер пушки:
                   по таймеру происходит расчет координат и отрисовка.'''
    global canvas, cannon, root_copy
    sine = cannon.sine_of_angle_between_the_horizon_line_and_the_cannon_line
    cosine = cannon.cosine_of_angle_between_the_horizon_line_and_the_cannon_line
    cannon.x1, cannon.y1 = 100 - cosine * cannon.width / 2, HEIGHT - 100 + sine * cannon.width / 2
    cannon.x2, cannon.y2 = cannon.x1 + cosine * cannon.width, cannon.y1 - sine * cannon.width
    cannon.x3, cannon.y3 = cannon.x2 - sine * cannon.length, cannon.y2 - cosine * cannon.length
    cannon.x4, cannon.y4 = cannon.x1 - sine * cannon.length, cannon.y1 - cosine * cannon.length

    canvas.delete(cannon.cannon_id)
    cannon.cannon_id = canvas.create_polygon((cannon.x1, cannon.y1), (cannon.x2, cannon.y2),
                                             (cannon.x3, cannon.y3), (cannon.x4, cannon.y4),
                                             fill=cannon.color)
    root_copy.after(25, cannon_tick)


def cannonball_tick():
    global canvas, cannon, root_copy, cannonballs
    for cannonball in cannonballs:
        cannonball.move()
        cannonball.show()
    root_copy.after(25, cannonball_tick)


def target_tick():
    pass


def click_handler(event):
    '''Нажатие левой кнопкой мыши на холст.'''
    global cannon, button_released
    button_released = 0
    cannon.increasing_the_length_and_color_gradation_of_the_cannon()


def motion_of_mouse_handler(event):
    '''Движение курсора по холсту.'''
    global cannon, canvas
    cannon.sine_of_angle_between_the_horizon_line_and_the_cannon_line = (100 - event.x) / \
                                                                        (((event.x - 100) ** 2 +
                                                                          (event.y - HEIGHT + 100) ** 2) ** 0.5)
    cannon.cosine_of_angle_between_the_horizon_line_and_the_cannon_line = (HEIGHT - 100 - event.y) / \
                                                                          (((event.x - 100) ** 2 +
                                                                            (event.y - HEIGHT + 100) ** 2) ** 0.5)


def button_released_handler(event):
    '''Отпускание левой кнопки мыши.'''
    global button_released
    button_released = 1


def main(root):
    '''Инициализация холста, bindов; отображение холста.'''
    global cannon, canvas, root_copy, red, cannonballs
    cannonballs = []
    red = 0
    root_copy = root
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.grid(row=0, column=0)
    cannon = Cannon()
    cannon_tick()
    cannonball_tick()
    canvas.bind('<Motion>', motion_of_mouse_handler)
    canvas.bind('<Button-1>', click_handler)
    canvas.bind('<ButtonRelease-1>', button_released_handler)
    root.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT) + '+80+50')
    root.title('The Game Cannon')
    main(root)
