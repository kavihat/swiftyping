import pygame, random
from pygame.locals import *

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 850

blue = (30, 30, 255)
green = (30, 150, 30)
red = (255, 0, 0)
white = (255, 255, 255)
yellow=(255,255,0)
silver=(192,192,192)
maroon=(128,0,0)
teal=(0,128,128)

pygame.init()
font = pygame.font.SysFont('Arial', 80, bold=True)   #print(pygame.font.get_fonts()) for all fonts available
font_intro=pygame.font.SysFont('calibri',60,bold=True)
font_gamer_msg=pygame.font.SysFont('Comicsansms',25,bold=False)


# floating words
def floating_words():
    w_x = random.randint(80, 600)
    w_y = 0
    pressed_word = ""
    speed = 0.06
    lines = open('wordlist.txt').read().splitlines()
    chosen_word = random.choice(lines)
    txt = font.render(chosen_word, True, blue)
    return txt, w_x, w_y, speed


# Main Window creation with background image
def window_creation():
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    window.fill(white)
    pygame.display.set_caption('SWIFTyping')
    a = pygame.image.load('icon.png')
    pygame.display.set_icon(a)
    # background and text creation
    #background = pygame.image.load('lightkey.jpg').convert()
    background = pygame.image.load('black_keyboard.jpg')
    background=pygame.transform.scale(background,(1000,850))

    window.blit(background, (0, 0))
    welcome_text = font.render('SWIFTyping Test', True, red)
    intro_msg = font_intro.render('Press any key to play', True, white)
    gamer_msg=font_gamer_msg.render('Press ESC to return to Main Menu',True,yellow)

    window.blit(welcome_text, (SCREEN_WIDTH / 2 - 250, 0))
    window.blit(intro_msg,(SCREEN_WIDTH/2-250,300))
    window.blit(gamer_msg, (SCREEN_WIDTH / 2 -210, 800))
    pygame.display.flip()
    return window


# Game window creation



def game_window():
    run = True
    #word_y = 0
    text, word_x, word_y, speed = floating_words()

    while run:

        window.fill(white)
        word_y += speed
        window.blit(text, (word_x, word_y))
        if word_y > SCREEN_HEIGHT:
            text, word_x, word_y, speed = floating_words()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # press escape key to come back to main window
                    run = False



# Main Loop
run = True
while run:
    window = window_creation()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:  # press any key to enter game window
            game_window()

    pygame.display.update()
