from pygame import draw

from exterminate_colors import *

WIDTH = 800

class Bomb:
    def __init__(self, screen):
        """
        Конструктор класса Bomb.
        """
        self.r = 10
        self.screen = screen
        self.vx = 15
        self.color = WHITE

    def move_right(self):
        """
        Нужно для ЛЕВОГО далека.
        Двигается горизонтально вправо без ускорения.
        """
        global bombs1, WIDTH
        self.x += self.vx

    def move_left(self):
        """
        Нужно для ПРАВОГО далека.
        Двигается горизонтально влево без ускорения.
        """
        global bombs2, WIDTH
        self.x -= self.vx


    def draw(self):
        """
        Рисует бомбу.
        """
        draw.circle(self.screen, self.color, (self.x, self.y), self.r, 0)

    def hit_tardis(self, obj):
        """
        Проверяет, столкнулась ли бомба с тардис.
        """
        if abs(self.x - obj.x) < 14 and (obj.y <= self.y and (obj.y + 95) >= self.y):
            obj.alive = False
