import math
import time
from random import choice
from random import randint as rnd
from pygame.draw import *
from math import pi

import pygame
import time
from pygame import draw


FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (170, 170, 180)
BLUE = (34, 70, 185)
YELLOW = (255, 255, 0)
SeaGreen4 = (46, 139, 87)
SeaGreen1 = (84, 255, 159)
SeaGreen3 = (67, 205, 128)
SlateGray4 = (108, 123, 139) # самый тёмный
LightSteelBlue3 = (162, 181, 205)
LightSteelBlue2 = (188, 210, 238)
LightSteelBlue1 = (202, 225, 255) # самый светлый


WIDTH = 800
HEIGHT = 600

up_key_down = False
down_key_down = False
left_key_down = False
right_key_down = False
score = 5
all_time = 0

class Gun:
    def __init__(self, screen):
        """
        Конструктор класса Gun. ВОЗМОЖНО здесь потом появится оружие у тардис в виде звуковой отвертки.
        """
        self.screen = screen
        self.f2_power = 10
        self.f2_on = False
        self.an = pi
        self.color = GREY
        self.x1 = 330
        self.y1 = 370
        self.r = 30
        self.x2 = 70
        self.y2 = 550

    def move(self):
        """.
        Движение происходит с помощью стрелочек вверх, вниз, вправо, влево.
        """
        global up_key_down, down_key_down
        if up_key_down and self.y1 >= 30:
            self.y1 -= 10
        if down_key_down and self.y1 <= 490:
            self.y1 += 10
        if right_key_down and self.x1 <= 720:
            self.x1 += 10
        if left_key_down and self.x1 >= 150:
            self.x1 -= 10


class Dalek:
    """ далек выпускает бомбы на тардис; далек может летать снизу вверх"""
    def __init__(self):
        """
        Конструктор класса Dalek.
        """
        self.alive = True
        self.screen = pygame.Surface
        self.x = 100
        self.y = rnd(70, 500)
        self.r = rnd(20, 40)
        self.vx = rnd(3, 5) * choice([-1, 1])
        self.vy = rnd(7,9)


    def move(self):
        
        if self.y >= 50:
            self.vx = -self.vx
        else:
            self.vx = -self.vx
        self.x += self.vx
        
        if self.y <= 70:
            self.vy = -self.vy
        
        if self.y >= 500:
            self.vy = -self.vy
        self.y += self.vy
        
        
        
        
        """if self.y >= 50:
            self.vx = -self.vx
        else:
            self.vx = -self.vx
        self.x += self.vx
        if self.y <= 70:
            self.vy = -self.vy
        else:
            self.vy = -self.vy
        self.y += self.vy"""

        

    def draw(self):
        """
        Рисует далеков.
        """
        arc(screen,LightSteelBlue1 ,
                (self.x - 52, self.y - 10, 30, 30),
                0, pi, 2)
        line(screen,LightSteelBlue1 , 
                 [self.x - 52, self.y + 5], 
                 [self.x - 23, self.y + 5], 3)
        arc(screen,LightSteelBlue1 ,
                (self.x - 50, self.y - 7, 22, 22),
                0, pi, 21)
        arc(screen,LightSteelBlue1 ,
                (self.x - 52, self.y - 10, 28, 30),
                0, pi, 2)
        arc(screen,LightSteelBlue1 ,
                (self.x - 52, self.y - 10, 26, 30),
                0, pi, 3)
        arc(screen,LightSteelBlue1 ,
                (self.x - 52, self.y - 10, 24, 30),
                0, pi, 3)
        line(screen,LightSteelBlue1 , [self.x - 35, self.y], [self.x, self.y], 2) 
        arc(screen,LightSteelBlue3 ,
                (self.x, self.y - 2, 7, 7),
                0.5*pi, 1.5*pi, 10) #!
        rect(screen, SlateGray4 , (self.x - 47, self.y + 7, 20, 7))
        rect(screen, LightSteelBlue1 , (self.x - 52, self.y + 14, 30, 3))
        rect(screen, SlateGray4 , (self.x - 47, self.y + 7, 20, 7))
        rect(screen, LightSteelBlue1 , (self.x - 52, self.y + 14, 30, 3))
        rect(screen, SlateGray4 , (self.x - 47, self.y + 17, 20, 4))
        rect(screen, LightSteelBlue1 , (self.x - 52, self.y + 20, 30, 3))
        polygon(screen, LightSteelBlue3 , 
                    [[self.x - 47, self.y + 24], [self.x - 27, self.y + 24], 
                     [self.x - 10, self.y + 65], [self.x - 52, self.y + 65]])
        rect(screen,SlateGray4  , (self.x - 57, self.y + 65, 53, 12))
        circle(screen,SlateGray4  , 
                   (self.x - 20, self.y + 35), 5)
        line(screen, LightSteelBlue1, [self.x - 15, self.y + 35],[self.x + 15, self.y + 35], 2)
        rect(screen, LightSteelBlue1, (self.x + 15, self.y + 31, 4, 7))
        rect(screen, LightSteelBlue1, (self.x - 57, self.y + 77, 52, 2))
        circle(screen, SlateGray4, 
                   (self.x - 35, self.y + 41), 5)
        circle(screen,SlateGray4, 
                   (self.x - 35, self.y + 55), 5)

    def spawn_bomb(self):
        """
        Далек каждый тик (или как это называется?) может сбросить бомбу с вероятностью 1%.
        """
        global bombs
        if not rnd(0,99):
            new_bomb = Bomb()
            new_bomb.x = self.x
            new_bomb.y = self.y
            bombs.append(new_bomb)


class Tardis:
    def __init__(self):
        """
        Конструктор класса Tardis. Летает и пытается выжить.
        """
        self.alive = True
        self.screen = pygame.Surface
        self.r = 15
        self.x = gun.x1
        self.y = gun.y1

    def draw(self):
        
        my_font = pygame.font.SysFont('Comic Sans MS', 7)
        text = my_font.render('Police box', False, WHITE)

        rect(screen, BLUE, (self.x, self.y, 50, 88))
        rect(screen, BLACK, (self.x, self.y, 50, 88), 2)

        rect(screen, BLUE, (self.x + 7, self.y - 9, 35, 10))
        rect(screen, BLACK, (self.x + 7, self.y - 9, 35, 10), 2)

        rect(screen, GREY, (self.x + 10, self.y + 25, 10, 10))
        rect(screen, BLACK, (self.x + 10, self.y + 25, 10, 10), 2)

        rect(screen, GREY, (self.x + 30, self.y + 25, 10, 10))
        rect(screen, BLACK, (self.x + 30, self.y + 25, 10, 10), 2)

        rect(screen, BLUE, (self.x - 5, self.y + 85, 60, 10))
        rect(screen, BLACK, (self.x - 5, self.y + 85, 60, 10), 2)

        rect(screen, BLACK, (self.x + 30, self.y + 40, 10, 10), 2)

        rect(screen, BLACK, (self.x + 10, self.y + 40, 10, 10), 2)

        rect(screen, BLACK, (self.x + 30, self.y + 55, 10, 10), 2)

        rect(screen, BLACK, (self.x + 10, self.y + 55, 10, 10), 2)

        rect(screen, BLACK, (self.x + 30, self.y + 70, 10, 10), 2)

        rect(screen, BLACK, (self.x + 10, self.y + 70, 10, 10), 2)

        rect(screen, BLACK, (self.x + 5, self.y + 20, 40, 65), 2)

        rect(screen, BLACK, (self.x + 5, self.y + 5, 40, 10))

        rect(screen, YELLOW, (self.x + 22, self.y - 13, 5, 5))
        rect(screen, BLACK, (self.x + 22, self.y - 13, 5, 5), 1)

        screen.blit(text, (self.x + 7, self.y + 4))

        line(screen, BLACK, 
                         [self.x + 25, self.y + 20], 
                         [self.x + 25, self.y + 85], 2)


    def pos_update(self):
        """
        Обновляет координаты тардис, чтобы они совпадали с координатами начала
        """
        self.x = gun.x1
        self.y = gun.y1


class Bomb:
    def __init__(self):
        """
        Конструктор класса Bomb.
        """
        self.r = 10
        self.vx = 15
        self.color = WHITE

    def move(self):
        """
        Двигается горизонтально вправо без ускорения.
        Если достигла правой границы, удаляется из массива.
        """
        global bombs
        self.x += self.vx
        if len(bullets) > 0 and self.x >= WIDTH:
            bombs.remove(self)

    def draw(self):
        """
        Рисует бомбу.
        """
        draw.circle(screen, self.color, (self.x, self.y), self.r, 0)

    def hit_tardis(self, obj):
        """
        Проверяет, столкнулась ли бомба с тардис.
        """
        if abs(self.x - obj.x) < 14 and (obj.y <= self.y and (obj.y + 95) >= self.y):
            obj.alive = False


def new_dalek():
    """ Инициализация нового далека. Добавление его в массив далеков."""
    global targets
    new_dalek = Dalek()
    daleks.append(new_dalek)


def display_score():
    """ Отображает текущий счёт."""
    global score

    score -= 0.03
    font = pygame.font.SysFont('Comic Sans MS', 26)
    text = font.render('Time: ' + str(int(score)) + '', False, WHITE)
    textpos = text.get_rect(centerx=75, y=25)
    screen.blit(text, textpos)

def display_score():
    """ Отображает текущий счёт."""
    global score

    score -= 0.03
    font = pygame.font.SysFont('Comic Sans MS', 26)
    text = font.render('Time: ' + str(int(score)) + '', False, WHITE)
    textpos = text.get_rect(centerx=75, y=25)
    screen.blit(text, textpos)

def display_results():
    """ Если бомба попала в тардис, останавливает игру и выводит соответствующую надпись."""
    
    polygon(screen, RED, [(tardis.x - 40, tardis.y), (tardis.x - 14, tardis.y - 14), (tardis.x, tardis.y - 40), (tardis.x + 14, tardis.y - 14), (tardis.x + 40, tardis.y), 
                             (tardis.x + 14, tardis.y + 14), (tardis.x, tardis.y + 40), (tardis.x - 14, tardis.y + 14)])
    polygon(screen, YELLOW, [(tardis.x - 28, tardis.y + 28), (tardis.x - 10, tardis.y), (tardis.x - 28, tardis.y - 28), (tardis.x, tardis.y - 10), (tardis.x + 28, tardis.y - 28), 
                             (tardis.x + 10, tardis.y), (tardis.x + 28, tardis.y + 28), (tardis.x, tardis.y + 10)])
    
    rect(screen, WHITE, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100))
    rect(screen, BLACK, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100), 2)
    font = pygame.font.SysFont('Verdana', 22)
    text = font.render('Your TARDIS died. You have survived for '+str(60 - int(score))+' seconds.', True, (10, 10, 10))
    textpos = text.get_rect(centerx=WIDTH/2, y=HEIGHT/2)
    screen.blit(text, textpos)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet_count = 0
daleks = []
bullets = []
bombs = []

clock = pygame.time.Clock()
gun = Gun(screen)

tardis = Tardis()
new_dalek()

finished = False


#первый уровень
while not finished:
    if not tardis.alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        display_results()
        pygame.display.update()
    else:
        screen.fill(BLACK)
        gun.move()
        tardis.pos_update()
        tardis.draw()
        display_score()
        if int(score) <= 0:
            rect(screen, WHITE, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100))
            rect(screen, BLACK, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100), 2)
            font = pygame.font.SysFont('Verdana', 22)
            text = font.render('Congrats. You have survived for '+str(60 - int(score))+' seconds.', True, (10, 10, 10))
            textpos = text.get_rect(centerx=WIDTH/2, y=HEIGHT/2)
            screen.blit(text, textpos)
            score = 0
            pygame.display.update()
            time.sleep(2)
            finished = True
        for dalek in daleks:
            dalek.spawn_bomb()
            dalek.move()
            dalek.draw()
        for bomb in bombs:
            bomb.hit_tardis(tardis)
            bomb.move()
            bomb.draw()
        for bullet in bullets:
            bullet.aging()
            bullet.draw()
        pygame.display.update()

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up_key_down = True
                if event.key == pygame.K_DOWN:
                    down_key_down = True
                if event.key == pygame.K_RIGHT:
                    right_key_down = True
                if event.key == pygame.K_LEFT:
                    left_key_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up_key_down = False
                if event.key == pygame.K_DOWN:
                    down_key_down = False
                if event.key == pygame.K_RIGHT:
                    right_key_down = False
                if event.key == pygame.K_LEFT:
                    left_key_down = False
            if event.type == pygame.QUIT:
                finished = True
            
            


pygame.quit()
