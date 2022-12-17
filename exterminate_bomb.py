from pygame import draw

from exterminate_colors import *


class Bomb:
    def __init__(self, screen, bullets):
        """
        Конструктор класса Bomb.
        """
        self.r = 10
        self.screen = screen
        self.bullets = bullets
        self.vx = 15
        self.color = WHITE

    def move(self):
        """
        Двигается горизонтально вправо без ускорения.
        Если достигла правой границы, удаляется из массива.
        """
        global bombs, WIDTH
        self.x += self.vx
        if len(self.bullets) > 0 and self.x >= WIDTH:
            bombs.remove(self)

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
