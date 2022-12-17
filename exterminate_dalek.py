from math import pi
from random import choice
from random import randint as rnd

from pygame.draw import *

from exterminate_bomb import Bomb
from exterminate_colors import *




class Dalek:
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
        "дрожание далека"
        if self.y >= 70:
            self.vx = -self.vx
        else:
            self.vx = -self.vx
        self.x += self.vx

        "движение вдоль оси у"
        if self.y <= 70:
            self.vy = -self.vy

        if self.y >= 500:
            self.vy = -self.vy
        self.y += self.vy

    def draw(self):
        """
        Рисует далеков.
        """
        k = 1 #коэффициент пропорциональности; если его менять, можно менять размер всего далека
        arc(self.screen, LightSteelBlue1,
            (self.x - 52 * k, self.y - 10 * k, 30 * k, 30 * k),
            0, pi, 2 * k)
        line(self.screen, LightSteelBlue1,
             [self.x - 52 * k, self.y + 5 * k],
             [self.x - 23 * k, self.y + 5 * k], 3 * k)
        arc(self.screen, LightSteelBlue1,
            (self.x - 50 * k, self.y - 7 * k, 22 * k, 22 * k),
            0, pi, 21)
        arc(self.screen, LightSteelBlue1,
            (self.x - 52 * k, self.y - 10 * k, 28 * k, 30 * k),
            0, pi, 2 * k)
        arc(self.screen, LightSteelBlue1,
            (self.x - 52 * k, self.y - 10 * k, 26 * k, 30 * k),
            0, pi, 3 * k)
        arc(self.screen, LightSteelBlue1,
            (self.x - 52 * k, self.y - 10 * k, 24 * k, 30 * k),
            0, pi, 3 * k)
        line(self.screen, LightSteelBlue1, [self.x - 35 * k, self.y], [self.x, self.y], 2 * k)
        arc(self.screen, LightSteelBlue3,
            (self.x, self.y - 2 * k, 7 * k, 7 * k),
            0.5 * pi, 1.5 * pi, 10 * k)  # !
        rect(self.screen, SlateGray4, (self.x - 47 * k, self.y + 7 * k, 20 * k, 7 * k))
        rect(self.screen, LightSteelBlue1, (self.x - 52 * k, self.y + 14 * k, 30 * k, 3 * k))
        rect(self.screen, SlateGray4, (self.x - 47 * k, self.y + 7 * k, 20 * k, 7 * k))
        rect(self.screen, LightSteelBlue1, (self.x - 52 * k, self.y + 14 * k, 30 * k, 3 * k))
        rect(self.screen, SlateGray4, (self.x - 47 * k, self.y + 17 * k, 20 * k, 4 * k))
        rect(self.screen, LightSteelBlue1, (self.x - 52 * k, self.y + 20 * k, 30 * k, 3 * k))
        polygon(self.screen, LightSteelBlue3,
                [[self.x - 47 * k, self.y + 24 * k], [self.x - 27 * k, self.y + 24 * k],
                 [self.x - 10 * k, self.y + 65 * k], [self.x - 52 * k, self.y + 65 * k]])
        rect(self.screen, SlateGray4, (self.x - 57 * k, self.y + 65 * k, 53 * k, 12 * k))
        circle(self.screen, SlateGray4,
               (self.x - 20 * k, self.y + 35 * k), 5 * k)
        line(self.screen, LightSteelBlue1, [self.x - 15 * k, self.y + 35 * k], [self.x + 15 * k, self.y + 35 * k], 2 * k)
        rect(self.screen, LightSteelBlue1, (self.x + 15 * k, self.y + 31 * k, 4 * k, 7 * k))
        rect(self.screen, LightSteelBlue1, (self.x - 57 * k, self.y + 77 * k, 52 * k, 2 * k))
        circle(self.screen, SlateGray4,
               (self.x - 35 * k, self.y + 41 * k), 5 * k)
        circle(self.screen, SlateGray4,
               (self.x - 35 * k, self.y + 55 * k), 5 * k)

    def spawn_bomb(self, bombs1):
        """
        Далек каждый тик (или как это называется?) может сбросить бомбу с вероятностью 3%.
        """
        if not rnd(0, 30):
            new_bomb = Bomb(self.screen)
            new_bomb.x = self.x
            new_bomb.y = self.y
            bombs1.append(new_bomb)
