# Created a game in pygame to improve typing speed


import pygame
import random
from pygame.locals import *

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 850

# Colors
blue = (30, 30, 255)
green = (30, 150, 30)
red = (255, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
silver = (192, 192, 192)
maroon = (128, 0, 0)
teal = (0, 128, 128)

pygame.init()
game_sound = pygame.mixer.music.load('Down_Time_In_My_Soul.wav')  # music for the game window
# Font Styles
font = pygame.font.SysFont('Arial', 80, bold=True)  # print(pygame.font.get_fonts()) for all fonts available
font_intro = pygame.font.SysFont('calibri', 60, bold=True)
font_gamer_msg = pygame.font.SysFont('Comicsansms', 25, bold=False)
font_score = pygame.font.SysFont('calibri', 100, bold=True)
speed = 0.06


# floating words
def floating_words(speed):
    w_x = random.randint(80, 600)
    w_y = 0
    pressed_word = ""
    speed = speed + 0.06
    lines = open('wordlist.txt').read().splitlines()
    chosen_word = random.choice(lines)
    txt = font.render(chosen_word, True, blue)
    return txt, w_x, w_y, speed, chosen_word, pressed_word


# Main Window creation with background image
def window_creation():
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    window.fill(white)
    pygame.display.set_caption('SWIFTyping')
    a = pygame.image.load('icon.png')
    pygame.display.set_icon(a)
    background = pygame.image.load('black_keyboard.jpg')
    background = pygame.transform.scale(background, (1000, 850))

    window.blit(background, (0, 0))
    welcome_text = font.render('SWIFTyping Test', True, red)
    intro_msg = font_intro.render('Press any key to play', True, white)
    gamer_msg = font_gamer_msg.render('Press ESC to return to Main Menu', True, yellow)

    window.blit(welcome_text, (SCREEN_WIDTH / 2 - 250, 0))
    window.blit(intro_msg, (SCREEN_WIDTH / 2 - 250, 300))
    window.blit(gamer_msg, (SCREEN_WIDTH / 2 - 210, 800))
    pygame.display.flip()
    return window


# Game window creation


def game_window():
    global word_x, speed, word_y, text, pressed_word, chosen_word
    run = True
    point = 0
    pygame.mixer.music.play()

    while run:

        window.fill(silver)
        word_y += speed
        window.blit(text, (word_x, word_y))
        pointtitle = font.render(str(point), True, maroon)
        window.blit(pointtitle, (5, 10))
        pygame.display.flip()

        # Fail condition
        if word_y > SCREEN_HEIGHT:
            break

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # press escape key to come back to main window
                    run = False

            elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                pressed_word += pygame.key.name(event.key)
                if chosen_word.startswith(pressed_word):
                    if chosen_word == pressed_word:
                        point += len(chosen_word)
                        text, word_x, word_y, speed, chosen_word, pressed_word = floating_words(speed)

                else:
                    pressed_word = ""

    game_result(point)


# Score window creation

def game_result(val):
    pygame.mixer.music.stop()
    run = True
    game_score = pygame.image.load('score.jpg')
    game_score = pygame.transform.scale(game_score, (1000, 850))
    window.blit(game_score, (0, 0))
    score_text = font.render('Your Score is ', True, green)

    while run:
        score = font_score.render(str(val), True, red)
        window.blit(score_text, (SCREEN_WIDTH / 2 - 250, 200))
        window.blit(score, (SCREEN_WIDTH / 2 - 85, 300))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()


# Main Loop

run = True
window = window_creation()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:  # press any key to enter game window
            text, word_x, word_y, speed, chosen_word, pressed_word = floating_words(speed)
            game_window()

pygame.display.update()
