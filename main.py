import time
import random
import pygame
import sys

from pygame.draw import rect

from colors import *
from dalek import Dalek
from dalek2 import Dalek2
from tardis import Tardis
from teleport import Teleport

FPS = 30
WIDTH = 1540
HEIGHT = 800

up_key_down = False
down_key_down = False
left_key_down = False
right_key_down = False

scale_tardis = 1


def display_score(score, level):
    """ Отображает текущий счёт."""
    global all_time
    all_time += 0.03

    text_x = 0.2 * HEIGHT
    text_y = 0.04 * WIDTH
    font = pygame.font.SysFont('Comic Sans MS', 26)
    text = font.render('LEVEL ' + str(int(level + 1)) + '', False, RED)
    textpos = text.get_rect(centerx=text_x, y=text_y)
    screen.blit(text, textpos)

    if int(score) >= 1:
        text2 = font.render('Time till portal: ' + str(int(score)) + '', False, WHITE)

    else:
        text2 = font.render('Run to the portal!', False, RED)
    textpos2 = text2.get_rect(centerx=text_x, y=2 * text_y)
    screen.blit(text2, textpos2)


def display_results():
    """ Если бомба попала в тардис, останавливает игру и выводит соответствующую надпись."""

    size_bang = 160 * scale_tardis  # размер картинки
    bang = pygame.image.load("blow_up.png")
    bang = pygame.transform.scale(bang, (size_bang, size_bang))
    screen.blit(bang, (tardis.x - 25, tardis.y - 35))

    rect(screen, WHITE, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100))
    rect(screen, BLACK, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100), 2)
    font = pygame.font.SysFont('Verdana', 22)
    text = font.render('Your TARDIS died. You have survived for ' + str(int(all_time)) + ' seconds.', True,
                       BLACK)
    textpos = text.get_rect(centerx=WIDTH / 2, y=HEIGHT / 2)
    screen.blit(text, textpos)


def portal_escape():
    """
    Поздравляет игрока с пройденным уровнем.
    """
    rect(screen, WHITE, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100))
    rect(screen, BLACK, (WIDTH / 2 - 350, HEIGHT / 2 - 40, 700, 100), 2)
    font = pygame.font.SysFont('Verdana', 22)
    text = font.render('Congrats. You have survived for ' + str(int(all_time)) + ' seconds.', True,
                       BLACK)
    textpos = text.get_rect(centerx=WIDTH / 2, y=HEIGHT / 2)
    screen.blit(text, textpos)


def coordinates_teleport(tard):
    """
    Координаты портала задаем взависимости от того, где находится тардис
    """
    k = min(HEIGHT, WIDTH)
    tel = random.randint(int(0.3 * k), int(0.7 * k))
    if abs(tel - tard) <= 0.1 * k:
        tel = 0.9 * k - tard
    return tel


def new_level(tardis, level, finished, number_l_daleks, number_r_daleks):
    """
    Новый уровень
    """
    global bombs1, bombs2
    score = 8  # время каждого уровня (до появления портала)
    time_passed = 0
    left_daleks = []
    right_daleks = []
    x_left_dalek = 0.125 * WIDTH
    x_right_dalek = 0.94 * WIDTH
    for i in range(number_l_daleks):
        dalek = Dalek(screen, x_left_dalek)
        left_daleks.append(dalek)
    for i in range(number_r_daleks):
        dalek = Dalek2(screen, x_right_dalek)
        right_daleks.append(dalek)
    while not finished:
        if not tardis.alive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    sys.exit()
            display_results()
            pygame.display.update()
        else:
            score -= 0.03
            time_passed += 0.03
            space = pygame.image.load('SpaceBackGround.bmp')
            screen.blit(space, (0, 0))
            field_x, field_y = 0.16 * WIDTH, 0.008 * HEIGHT
            field_width, field_height = 0.675 * WIDTH, 0.99 * HEIGHT
            rect(screen, WHITE, (field_x, field_y, field_width, field_height), 2)
            tardis.move(HEIGHT, WIDTH, scale_tardis)
            tardis.draw(scale_tardis)
            display_score(score, level)
            if int(score) <= 0:
                sound = pygame.mixer.Sound('portal.wav')
                sound.play()
                teleport.draw(scale_tardis, screen)
                tardis.draw(scale_tardis)
                pygame.display.update()
                if (0 <= (tardis.x - teleport.x) <= 70 * scale_tardis) and (
                        0 <= (tardis.y - teleport.y) <= 20 * scale_tardis):
                    portal_escape()
                    bombs1 = []
                    bombs2 = []
                    score = 0
                    pygame.display.update()
                    time.sleep(1.5)
                    finished = True
            for dalek in left_daleks:
                if time_passed >= 1:
                    dalek.spawn_bomb(bombs1)
                dalek.move(HEIGHT)
                dalek.draw()
            for dalek in right_daleks:
                if time_passed >= 1:
                    dalek.spawn_bomb(bombs2)
                dalek.move(HEIGHT)
                dalek.draw()
            for bomb in bombs1:
                bomb.hit_tardis(score, tardis, scale_tardis)
                bomb.move_right()
                bomb.draw(score)
            for bomb in bombs2:
                bomb.hit_tardis(score, tardis, scale_tardis)
                bomb.move_left()
                bomb.draw(score)
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
                    sys.exit()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bombs1 = []
bombs2 = []
tardis = Tardis(screen)

clock = pygame.time.Clock()

tel_x = coordinates_teleport(tardis.x)
tel_y = coordinates_teleport(tardis.y)
teleport = Teleport(screen, tel_x, tel_y)
finished = False

all_time = 0

level_number = 10  # число уровней
number_r_daleks = 0
number_l_daleks = 1

for level in range(level_number):
    new_level(tardis, level, finished, number_l_daleks, number_r_daleks)
    number_l_daleks += level % 2
    number_r_daleks += (level + 1) % 2
pygame.quit()
