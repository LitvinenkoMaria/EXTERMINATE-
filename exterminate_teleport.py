from exterminate_colors import *
from pygame.draw import *
from math import pi

import pygame
import time
from pygame import draw

class Teleport:
    def __init__(self, screen, tel_x, tel_y):
        self.x = tel_x
        self.y = tel_y
        self.screen = screen