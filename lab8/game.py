import tkinter as tk
from random import randrange as rnd, choice


HEIGHT = 600
WIDTH = 1200


class Cannon:
    '''Пушка:    вращается вокруг точки - середины ширины пушки;
                 атрибуты:    длина
                              ширина
                              цвет
                              координаты
                              синус и косинус угла между горизонтом и линией пушки'''
    def __init__(self):
        global canvas
        self.length = 75
        self.width = 15
        self.color = 'red'
        sine = self.sine_of_angle_between_the_horizon_line_and_the_cannon_line = 1
        cosine = self.cosine_of_angle_between_the_horizon_line_and_the_cannon_line = 0

        self.x1, self.y1 = 100, HEIGHT - 100
        self.x2, self.y2 = self.x1 - sine * self.length, self.y1 - cosine * self.length
        self.x3, self.y3 = self.x2 + sine * self.width, self.y2 - cosine * self.width
        self.x4, self.y4 = self.x1 + sine * self.width, self.y1 - cosine * self.width
        self.cannon_id = canvas.create_polygon((self.x1, self.y1), (self.x2, self.y2),
                                               (self.x3, self.y3), (self.x4, self.y4), fill=self.color)

    def increasing_the_length_and_color_gradation_of_the_cannon_by_timer(self):
        pass

    def rotation_of_the_cannon(self):
        global canvas
        canvas.delete(self.cannon_id)
        self.cannon_id = canvas.create_polygon((self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3),
                                               (self.x4, self.y4), fill=self.color)


class Cannonball:
    def __init__(self):
        pass

    def move(self):
        pass

    def show(self):
        pass


class Target:
    def __init__(self):
        pass

    def move(self):
        pass

    def show(self):
        pass


def checking_the_destruction_of_targets():
    pass


def cannonball_tick():
    pass


def target_tick():
    pass


def click_and_motion_handler(event):
    quit()


def moving_of_mouse_handler(event):
    global cannon, canvas
    sine = cannon.sine_of_angle_between_the_horizon_line_and_the_cannon_line = (cannon.x1 - event.x) / \
                                                                               (((event.x - cannon.x1)**2 +
                                                                                 (event.y - cannon.y1)**2) ** 0.5)
    cosine = cannon.cosine_of_angle_between_the_horizon_line_and_the_cannon_line = (cannon.y1 - event.y)\
        / (((event.x - cannon.x1) ** 2
           + (event.y - cannon.y1) ** 2) ** 0.5)
    cannon.x1, cannon.y1 = 100, HEIGHT - 100
    cannon.x2, cannon.y2 = cannon.x1 - sine * cannon.length, cannon.y1 - cosine * cannon.length
    cannon.x3, cannon.y3 = cannon.x2 + cosine * cannon.width, cannon.y2 - sine * cannon.width
    cannon.x4, cannon.y4 = cannon.x1 + cosine * cannon.width, cannon.y1 - sine * cannon.width
    cannon.rotation_of_the_cannon()


def main(root):
    global cannon, canvas
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.grid(row=0, column=0)
    cannon = Cannon()
    canvas.bind('<Motion>', moving_of_mouse_handler)
    canvas.bind('<B1-Motion>', click_and_motion_handler)
    root.mainloop()
    cannon_tick()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT) + '+80+50')
    root.title('The Game Cannon')
    main(root)
