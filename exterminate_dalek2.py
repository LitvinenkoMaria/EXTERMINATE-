from math import pi
from random import choice
from random import randint as rnd

from pygame.draw import *

from exterminate_bomb import Bomb
from exterminate_colors import *

WIDTH = 800


class Dalek2:
    """далек выпускает бомбы на тардис; далек может летать снизу вверх"""

    def __init__(self, screen, x_dalek):
        """
        Конструктор класса Dalek.
        """
        self.alive = True
        self.screen = screen
        self.x = x_dalek
        self.y = rnd(69, 500)
        self.r = rnd(20, 40)
        self.vx = rnd(3, 5) * choice([-1, 1])
        self.vy = rnd(7, 9)

    def move(self):

        if self.y >= 70:
            self.vx = -self.vx
        else:
            self.vx = -self.vx
        self.x += self.vx

        if self.y <= 70:
            self.vy = -self.vy

        if self.y >= 500:
            self.vy = -self.vy
        self.y += self.vy

    def draw(self):
        """
        Рисует далеков.
        """
        arc(self.screen, LightSteelBlue1,
            (self.x - 52, self.y - 10, 30, 30),
            0, pi, 2)
        line(self.screen, LightSteelBlue1,
             [self.x - 52, self.y + 5],
             [self.x - 23, self.y + 5], 3)
        arc(self.screen, LightSteelBlue1,
            (self.x - 50, self.y - 7, 22, 22),
            0, pi, 21)
        arc(self.screen, LightSteelBlue1,
            (self.x - 52, self.y - 10, 28, 30),
            0, pi, 2)
        arc(self.screen, LightSteelBlue1,
            (self.x - 52, self.y - 10, 26, 30),
            0, pi, 3)
        arc(self.screen, LightSteelBlue1,
            (self.x - 52, self.y - 10, 24, 30),
            0, pi, 3)
        line(self.screen, LightSteelBlue1, [self.x - 70, self.y], [self.x - 35, self.y], 2)
        arc(self.screen, LightSteelBlue3,
            (self.x - 75, self.y - 3, 7, 7),
            1.5 * pi, 0 * pi, 10)  # !
        rect(self.screen, SlateGray4, (self.x - 47, self.y + 7, 20, 7))
        rect(self.screen, LightSteelBlue1, (self.x - 52, self.y + 14, 30, 3))
        rect(self.screen, SlateGray4, (self.x - 47, self.y + 7, 20, 7))
        rect(self.screen, LightSteelBlue1, (self.x - 52, self.y + 14, 30, 3))
        rect(self.screen, SlateGray4, (self.x - 47, self.y + 17, 20, 4))
        rect(self.screen, LightSteelBlue1, (self.x - 52, self.y + 20, 30, 3))
        polygon(self.screen, LightSteelBlue3,
                [[self.x - 27, self.y + 24], [self.x - 47, self.y + 24],
                 [self.x - 65, self.y + 65], [self.x - 22, self.y + 65]])
        rect(self.screen, SlateGray4, (self.x - 70, self.y + 65, 53, 12))
        circle(self.screen, SlateGray4,
               (self.x - 50, self.y + 35), 5)
        line(self.screen, LightSteelBlue1, [self.x - 55, self.y + 35], [self.x - 80, self.y + 35], 2)
        rect(self.screen, LightSteelBlue1, (self.x - 80, self.y + 31, 4, 7))
        rect(self.screen, LightSteelBlue1, (self.x - 70, self.y + 77, 52, 2))
        circle(self.screen, SlateGray4,
               (self.x - 35, self.y + 41), 5)
        circle(self.screen, SlateGray4,
               (self.x - 35, self.y + 55), 5)

    def spawn_bomb(self, bombs2):
        """
        Далек каждый тик (или как это называется?) может сбросить бомбу с вероятностью 3%.
        """
        if not rnd(0, 30):
            new_bomb = Bomb(self.screen)
            new_bomb.x = self.x
            new_bomb.y = self.y
            bombs2.append(new_bomb)
