import time
import random
import pygame
from pygame.draw import *

from exterminate_colors import *
from exterminate_dalek import Dalek
from exterminate_tardis import Tardis
from exterminate_teleport import Teleport

FPS = 30
WIDTH = 800
HEIGHT = 600
level = 1

up_key_down = False
down_key_down = False
left_key_down = False
right_key_down = False


def new_dalek():
    """ Инициализация нового далека. Добавление его в массив далеков."""
    global targets
    new_dalek = Dalek(screen, bullets, x_dalek)
    daleks.append(new_dalek)


def display_score():
    """ Отображает текущий счёт."""
    global score, all_time, level
    all_time += 0.03
    if int(score) >= 1:
        score -= 0.03
        font = pygame.font.SysFont('Comic Sans MS', 26)
        text = font.render('LEVEL ' + str(int(level)) + '', False, WHITE)
        textpos = text.get_rect(centerx = 110, y = 25)
        screen.blit(text, textpos)
        text2 = font.render('Time till portal: ' + str(int(score)) + '', False, WHITE)
        textpos2 = text2.get_rect(centerx = 110, y = 55)
        screen.blit(text2, textpos2)
    else:
        font = pygame.font.SysFont('Comic Sans MS', 26)
        text = font.render('LEVEL ' + str(int(level)) + '', False, WHITE)
        textpos = text.get_rect(centerx = 110, y = 25)
        screen.blit(text, textpos)
        font = pygame.font.SysFont('Comic Sans MS', 26)
        text2 = font.render('Run to the portal!', False, WHITE)
        textpos2 = text2.get_rect(centerx = 110, y = 55)
        screen.blit(text2, textpos2)


def display_results():
    """ Если бомба попала в тардис, останавливает игру и выводит соответствующую надпись."""

    polygon(screen, RED, [(tardis.x - 40, tardis.y), (tardis.x - 14, tardis.y - 14), (tardis.x, tardis.y - 40),
                          (tardis.x + 14, tardis.y - 14), (tardis.x + 40, tardis.y),
                          (tardis.x + 14, tardis.y + 14), (tardis.x, tardis.y + 40), (tardis.x - 14, tardis.y + 14)])
    polygon(screen, YELLOW, [(tardis.x - 28, tardis.y + 28), (tardis.x - 10, tardis.y), (tardis.x - 28, tardis.y - 28),
                             (tardis.x, tardis.y - 10), (tardis.x + 28, tardis.y - 28),
                             (tardis.x + 10, tardis.y), (tardis.x + 28, tardis.y + 28), (tardis.x, tardis.y + 10)])

    rect(screen, WHITE, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100))
    rect(screen, BLACK, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100), 2)
    font = pygame.font.SysFont('Verdana', 22)
    text = font.render('Your TARDIS died. You have survived for ' + str(int(all_time)) + ' seconds.', True,
                       (10, 10, 10))
    textpos = text.get_rect(centerx=WIDTH / 2, y=HEIGHT / 2)
    screen.blit(text, textpos)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet_count = 0
daleks = []
bullets = []
bombs = []
x_dalek = 100
clock = pygame.time.Clock()

tardis = Tardis(screen)
new_dalek()

tel_x = random.randint(100, 500)
tel_y = random.randint(100, 500)
if abs(tel_x - tardis.x) <= 65:
    tel_x = 500 - tardis.x
if abs(tel_y - tardis.y) <= 30:
    tel_y = 500 - tardis.y

teleport = Teleport(screen, tel_x, tel_y)
finished = False
first_level_passed = False
score = 6
all_time = 0

# первый уровень
while not finished:
    if not tardis.alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        display_results()
        pygame.display.update()
    else:
        screen.fill(BLACK)
        space = pygame.image.load('SpaceBackGround.bmp')
        screen.blit(space, (0, 0))
        rect(screen, WHITE, (130, 5, 540, 595), 2)
        tardis.move()
        tardis.draw()
        display_score()
        if int(score) <= 0:
            tel_image = pygame.image.load('portal5.jpg')
            tel_image = pygame.transform.scale(tel_image, (120, 120))
            tel_image.set_colorkey(BLACK)
            screen.blit(tel_image, (tel_x, tel_y))
            tardis.draw()
            pygame.display.update()

            if (0 <= (tardis.x - teleport.x) <= 70) and (0 <= (tardis.y - teleport.y) <= 20):
                rect(screen, WHITE, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100))
                rect(screen, BLACK, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100), 2)
                font = pygame.font.SysFont('Verdana', 22)
                text = font.render('Congrats. You have survived for ' + str(int(all_time)) + ' seconds.', True,
                                   BLACK)
                textpos = text.get_rect(centerx=WIDTH / 2, y=HEIGHT / 2)
                screen.blit(text, textpos)
                score = 0
                first_level_passed = True
                pygame.display.update()
                time.sleep(4)
                finished = True
        for dalek in daleks:
            dalek.spawn_bomb(bombs)
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

tardis = Tardis(screen)
tel_x = random.randint(100, 500)
tel_y = random.randint(100, 500)
if abs(tardis.x - tel_x) <= 65:
    tel_x = 500 - tardis.x
if abs(tardis.y - tel_y) <= 30:
    tel_y = 500 - tardis.y

teleport = Teleport(screen, tel_x, tel_y)

level2 = False
score = 6
level += 1
x_dalek = 750
new_dalek()
while not level2 and first_level_passed:
    if not tardis.alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level2 = True
        display_results()
        pygame.display.update()
    else:
        screen.fill(BLACK)
        space = pygame.image.load('SpaceBackGround.bmp')
        screen.blit(space, (0, 0))
        rect(screen, WHITE, (130, 5, 540, 595), 2)
        tardis.move()
        tardis.draw()
        display_score()
        if int(score) <= 0:
            tel_image = pygame.image.load('portal5.jpg')
            tel_image = pygame.transform.scale(tel_image, (120, 120))
            tel_image.set_colorkey(BLACK)
            screen.blit(tel_image, (tel_x, tel_y))
            tardis.draw()
            pygame.display.update()

            if (0 <= (tardis.x - teleport.x) <= 70) and (0 <= (tardis.y - teleport.y) <= 20):
                rect(screen, WHITE, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100))
                rect(screen, BLACK, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100), 2)
                font = pygame.font.SysFont('Verdana', 22)
                text = font.render('Congrats. You have survived for ' + str(int(all_time)) + ' seconds.', True,
                                   BLACK)
                textpos = text.get_rect(centerx=WIDTH / 2, y=HEIGHT / 2)
                screen.blit(text, textpos)
                score = 0
                pygame.display.update()
                time.sleep(4)
                level2 = True
        for dalek in daleks:
            dalek.spawn_bomb(bombs)
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
                level2 = True

pygame.quit()
