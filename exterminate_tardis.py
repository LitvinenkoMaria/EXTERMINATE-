import pygame
from pygame.draw import rect, line

from exterminate_colors import *


class Tardis:
    """
    Tardis летает и пытается выжить.
    """
    def __init__(self, screen):
        """
        задаем координаты (x, y),скорость v, состояние (alive) у тардис;
        тардис рисуем на экране screen.
        """

        self.alive = True
        self.screen = screen
        self.x = 330
        self.y = 370
        self.v = 15

    def draw(self, scale_tardis):
        """
        Рисует Тардис на экране screen
        """
        k = scale_tardis  #коэффициент пропорциональности; если его менять, можно менять размер всей Тардис

        my_font = pygame.font.SysFont('Comic Sans MS', round(7 * k))
        text = my_font.render('Police box', False, WHITE)

        rect(self.screen, BLUE, (self.x, self.y, round(50 * k), round(88 * k)))
        rect(self.screen, BLACK, (self.x, self.y, round(50 * k), round(88 * k)), round(2 * k))

        rect(self.screen, BLUE, (self.x + round(7 * k), self.y - round(9 * k), round(35 * k), round(10 * k)))
        rect(self.screen, BLACK, (self.x + round(7 * k), self.y - round(9 * k), round(35 * k), round(10 * k)), round(2 * k))

        rect(self.screen, GREY, (self.x + round(10 * k), self.y + round(25 * k), round(10 * k), round(10 * k)))
        rect(self.screen, BLACK, (self.x + round(10 * k), self.y + round(25 * k), round(10 * k), round(10 * k)), round(2 * k))

        rect(self.screen, GREY, (self.x + round(30 * k), self.y + round(25 * k), round(10 * k), round(10 * k)))
        rect(self.screen, BLACK, (self.x + round(30 * k), self.y + round(25 * k), round(10 * k), round(10 * k)), round(2 * k))

        rect(self.screen, BLUE, (self.x - round(5 * k), self.y + round(85 * k), round(60 * k), round(10 * k)))
        rect(self.screen, BLACK, (self.x - round(5 * k), self.y + round(85 * k), round(60 * k), round(10 * k)), round(2 * k))

        rect(self.screen, BLACK, (self.x + round(30 * k), self.y + round(40 * k), round(10 * k), round(10 * k)), round(2 * k))

        rect(self.screen, BLACK, (self.x + round(10 * k), self.y + round(40 * k), round(10 * k), round(10 * k)), round(2 * k))

        rect(self.screen, BLACK, (self.x + round(30 * k), self.y + round(55 * k), round(10 * k), round(10 * k)), round(2 * k))

        rect(self.screen, BLACK, (self.x + round(10 * k), self.y + round(55 * k), round(10 * k), round(10 * k)), round(2 * k))

        rect(self.screen, BLACK, (self.x + round(30 * k), self.y + round(70 * k), round(10 * k), round(10 * k)), round(2 * k))

        rect(self.screen, BLACK, (self.x + round(10 * k), self.y + round(70 * k), round(10 * k), round(10 * k)), round(2 * k))

        rect(self.screen, BLACK, (self.x + round(5 * k), self.y + round(20 * k), round(40 * k), round(65 * k)), round(2 * k))

        rect(self.screen, BLACK, (self.x + round(5 * k), self.y + round(5 * k), round(40 * k), round(10 * k)))

        rect(self.screen, YELLOW, (self.x + round(22 * k), self.y - round(13 * k), round(5 * k), round(5 * k)))
        rect(self.screen, BLACK, (self.x + round(22 * k), self.y - round(13 * k), round(5 * k), round(5 * k)), round(1 * k))

        self.screen.blit(text, (self.x + round(7 * k), self.y + round(4 * k)))

        line(self.screen, BLACK,
             [self.x + round(25 * k), self.y + round(20 * k)],
             [self.x + round(25 * k), self.y + round(85 * k)], round(2 * k))

    def move(self, HEIGHT, WIDTH):
        """.
        Движение происходит с помощью стрелочек вверх, вниз, вправо, влево.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y >= 0.05 * HEIGHT:
            self.y -= self.v
        if keys[pygame.K_DOWN] and self.y <= 0.82 * HEIGHT:
            self.y += self.v
        if keys[pygame.K_RIGHT] and self.x <= 0.75 * WIDTH:
            self.x += self.v
        if keys[pygame.K_LEFT] and self.x >= 0.19 * WIDTH:
            self.x -= self.v
