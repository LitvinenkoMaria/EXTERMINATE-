import pygame
from pygame.draw import rect, line

from exterminate_colors import *


class Tardis:
    def __init__(self, screen):
        """
        Конструктор класса Tardis. Летает и пытается выжить.
        """
        self.alive = True
        self.screen = screen
        self.r = 15
        self.x = 330
        self.y = 370

    def draw(self):
        """
        Рисует Тардис
        """
        my_font = pygame.font.SysFont('Comic Sans MS', 7)
        text = my_font.render('Police box', False, WHITE)



        rect(self.screen, BLUE, (self.x, self.y, 50, 88))
        rect(self.screen, BLACK, (self.x, self.y, 50, 88), 2)

        rect(self.screen, BLUE, (self.x + 7, self.y - 9, 35, 10))
        rect(self.screen, BLACK, (self.x + 7, self.y - 9, 35, 10), 2)

        rect(self.screen, GREY, (self.x + 10, self.y + 25, 10, 10))
        rect(self.screen, BLACK, (self.x + 10, self.y + 25, 10, 10), 2)

        rect(self.screen, GREY, (self.x + 30, self.y + 25, 10, 10))
        rect(self.screen, BLACK, (self.x + 30, self.y + 25, 10, 10), 2)

        rect(self.screen, BLUE, (self.x - 5, self.y + 85, 60, 10))
        rect(self.screen, BLACK, (self.x - 5, self.y + 85, 60, 10), 2)

        rect(self.screen, BLACK, (self.x + 30, self.y + 40, 10, 10), 2)

        rect(self.screen, BLACK, (self.x + 10, self.y + 40, 10, 10), 2)

        rect(self.screen, BLACK, (self.x + 30, self.y + 55, 10, 10), 2)

        rect(self.screen, BLACK, (self.x + 10, self.y + 55, 10, 10), 2)

        rect(self.screen, BLACK, (self.x + 30, self.y + 70, 10, 10), 2)

        rect(self.screen, BLACK, (self.x + 10, self.y + 70, 10, 10), 2)

        rect(self.screen, BLACK, (self.x + 5, self.y + 20, 40, 65), 2)

        rect(self.screen, BLACK, (self.x + 5, self.y + 5, 40, 10))

        rect(self.screen, YELLOW, (self.x + 22, self.y - 13, 5, 5))
        rect(self.screen, BLACK, (self.x + 22, self.y - 13, 5, 5), 1)

        self.screen.blit(text, (self.x + 7, self.y + 4))

        line(self.screen, BLACK,
             [self.x + 25, self.y + 20],
             [self.x + 25, self.y + 85], 2)

    def move(self):
        """.
        Движение происходит с помощью стрелочек вверх, вниз, вправо, влево.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y >= 30:
            self.y -= 15
        if keys[pygame.K_DOWN] and self.y <= 490:
            self.y += 15
        if keys[pygame.K_RIGHT] and self.x <= 600:
            self.x += 15
        if keys[pygame.K_LEFT] and self.x >= 150:
            self.x -= 15
