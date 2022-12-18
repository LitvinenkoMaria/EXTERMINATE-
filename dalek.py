from math import pi
from random import choice
from random import randint as rnd

from pygame.draw import arc, line, rect, polygon, circle

from bomb import Bomb
from colors import *


class Dalek:
    """далек выпускает бомбы на тардис; далек может летать снизу вверх"""

    def __init__(self, screen, x_dalek):
        """
        Задаем координату y далека, координата x_dalek - константа;
        задаем скорость vx, vy далека;
        Далек рисуется на экране screen.
        """
        self.screen = screen
        self.x = x_dalek
        self.y = rnd(69, 500)
        self.vx = rnd(3, 5) * choice([-1, 1])
        self.vy = rnd(7, 9)

    def move(self, HEIGHT):
        """дрожание далека"""
        if self.y >= 70:
            self.vx = -self.vx
        else:
            self.vx = -self.vx
        self.x += self.vx

        "движение вдоль оси у"
        if self.y <= 0.12 * HEIGHT:
            self.vy = -self.vy

        if self.y >= 0.83 * HEIGHT:
            self.vy = -self.vy
        self.y += self.vy

    def draw(self):
        """
        Рисует далека на экране screen.
        """
        k = 1 #коэффициент пропорциональности; если его менять, можно менять размер всего далека
        arc(self.screen, LightSteelBlue1,
            (self.x - round(52 * k), self.y - round(10 * k), round(30 * k), round(30 * k)),
            0, pi, round(2 * k))
        line(self.screen, LightSteelBlue1,
             [self.x - round(52 * k), self.y + round(5 * k)],
             [self.x - round(23 * k), self.y + round(5 * k)], round(3 * k))
        arc(self.screen, LightSteelBlue1,
            (self.x - round(50 * k), self.y - round(7 * k), round(22 * k), round(22 * k)),
            0, pi, round(21 * k))
        arc(self.screen, LightSteelBlue1,
            (self.x - round(52 * k), self.y - round(10 * k), round(28 * k), round(30 * k)),
            0, pi, round(2 * k))
        arc(self.screen, LightSteelBlue1,
            (self.x - round(52 * k), self.y - round(10 * k), round(26 * k), round(30 * k)),
            0, pi, round(3 * k))
        arc(self.screen, LightSteelBlue1,
            (self.x - round(52 * k), self.y - round(10 * k), round(24 * k), round(30 * k)),
            0, pi, round(3 * k))
        line(self.screen, LightSteelBlue1, [self.x - round(35 * k), self.y], [self.x, self.y], round(2 * k))
        arc(self.screen, LightSteelBlue3,
            (self.x, self.y - round(2 * k), round(7 * k), round(7 * k)),
            0.5 * pi, 1.5 * pi, round(10 * k))
        rect(self.screen, SlateGray4, (self.x - round(47 * k), self.y + round(7 * k), round(20 * k), round(7 * k)))
        rect(self.screen, LightSteelBlue1, (self.x - round(52 * k), self.y + round(14 * k), round(30 * k), round(3 * k)))
        rect(self.screen, SlateGray4, (self.x - round(47 * k), self.y + round(7 * k), round(20 * k), round(7 * k)))
        rect(self.screen, LightSteelBlue1, (self.x - round(52 * k), self.y + round(14 * k), round(30 * k), round(3 * k)))
        rect(self.screen, SlateGray4, (self.x - round(47 * k), self.y + round(17 * k), round(20 * k), round(4 * k)))
        rect(self.screen, LightSteelBlue1, (self.x - round(52 * k), self.y + round(20 * k), round(30 * k), round(3 * k)))
        polygon(self.screen, LightSteelBlue3,
                [[self.x - round(47 * k), self.y + round(24 * k)], [self.x - round(27 * k), self.y + round(24 * k)],
                 [self.x - round(10 * k), self.y + round(65 * k)], [self.x - round(52 * k), self.y + round(65 * k)]])
        rect(self.screen, SlateGray4, (self.x - round(57 * k), self.y + round(65 * k), round(53 * k), round(12 * k)))
        circle(self.screen, SlateGray4,
               (self.x - round(20 * k), self.y + round(35 * k)), round(5 * k))
        line(self.screen, LightSteelBlue1, [self.x - round(15 * k), self.y + round(35 * k)], [self.x + round(15 * k), self.y + round(35 * k)], round(2 * k))
        rect(self.screen, LightSteelBlue1, (self.x + round(15 * k), self.y + round(31 * k), round(4 * k), round(7 * k)))
        rect(self.screen, LightSteelBlue1, (self.x - round(57 * k), self.y + round(77 * k), round(52 * k), round(2 * k)))
        circle(self.screen, SlateGray4,
               (self.x - round(35 * k), self.y + round(41 * k)), round(5 * k))
        circle(self.screen, SlateGray4,
               (self.x - round(35 * k), self.y + round(55 * k)), round(5 * k))

    def spawn_bomb(self, bombs1):
        """
        Далек каждый тик может сбросить бомбу с вероятностью 2%
        bombs1 - массив, в котором будут содержаться все бомбы, выпускаемые далеком.
        """
        if not rnd(0, 50):
            new_bomb = Bomb(self.screen)
            new_bomb.x = self.x
            new_bomb.y = self.y
            bombs1.append(new_bomb)