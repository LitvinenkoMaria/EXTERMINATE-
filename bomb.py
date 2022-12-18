from pygame import draw

from colors import *

WIDTH = 800

class Bomb:
    def __init__(self, screen):
        """
        Задаем параметры бомбы: скорость, радиус, цвет;
        Бомба рисуется на экране screen.
        """
        self.r = 10
        self.screen = screen
        self.vx = 15
        self.color = WHITE

    def move_right(self):
        """
        Нужно для ЛЕВОГО далека.
        Бомба двигается горизонтально вправо без ускорения.
        """
        global bombs1, WIDTH
        self.x += self.vx

    def move_left(self):
        """
        Нужно для ПРАВОГО далека.
        Бомба двигается горизонтально влево без ускорения.
        """
        global bombs2, WIDTH
        self.x -= self.vx


    def draw(self, score):
        """
        Рисует бомб на экране screen.
        """
        draw.circle(self.screen, self.color, (self.x, self.y), self.r, 0)

    def hit_tardis(self, score, obj, scale_tardis):
        """
        Проверяет, столкнулась ли бомба с тардис.
        """
        k = scale_tardis
        if abs(self.x - obj.x) < round(14 * k) and (obj.y <= self.y) and (obj.y + round(95 * k)) >= self.y:
            obj.alive = False