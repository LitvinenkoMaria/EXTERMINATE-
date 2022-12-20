import pygame

from colors import BLACK

class Teleport:
    """
    Портал нужен для перехода на новый уровень
    """
    def __init__(self, screen, tel_x, tel_y):
        """
        Портал появляется на экране screen;
        tel_x, tel_y - координаты портала, которые задаются в зависимости
        от координат ТАРДИС.
        """
        self.x = tel_x
        self.y = tel_y
        self.screen = screen
    def draw(self, scale_tardis, screen):
        """
        Рисует портал.
        """
        k = scale_tardis
        tel_image = pygame.image.load('portal5.jpg')
        tel_size = 120
        tel_image = pygame.transform.scale(tel_image, (tel_size * k, tel_size * k))
        tel_image.set_colorkey(BLACK)
        screen.blit(tel_image, (self.x, self.y))