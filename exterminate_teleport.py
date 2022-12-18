import pygame

from exterminate_colors import BLACK

class Teleport:
    def __init__(self, screen, tel_x, tel_y):
        self.x = tel_x
        self.y = tel_y
        self.screen = screen
    def draw(self, scale_tardis, screen):
        k = scale_tardis
        tel_image = pygame.image.load('portal5.jpg')
        tel_size = 120
        tel_image = pygame.transform.scale(tel_image, (tel_size * k, tel_size * k))
        tel_image.set_colorkey(BLACK)
        screen.blit(tel_image, (self.x, self.y))