import pygame, random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 850
bcg = (255, 255, 255)
blue = (30, 30, 255)
green = (30, 150, 30)

pygame.init()


# floating words
def floating_words():
    w_x = random.randint(80, 600)
    w_y = 0
    pressed_word = ""
    speed = 0.06
    lines = open('wordlist.txt').read().splitlines()
    chosen_word = random.choice(lines)
    txt = font.render(chosen_word, True, blue)
    return txt, w_x, w_y,speed


# Window creation
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(bcg)
pygame.display.set_caption('SWIFTyping')
a = pygame.image.load('icon.png')
pygame.display.set_icon(a)

# background and text creation
# background = pygame.image.load('lightkey.jpg').convert()
# window.blit(background, (0, 0))
font = pygame.font.SysFont('Arial', 70, bold=True)
# text = font.render('SWIFTyping Test', True, (255, 0, 0))
# sprite = pygame.sprite.Sprite()
# sprite.image = pygame.Surface([700, 100]).convert()
# sprite.rect = (SCREEN_WIDTH / 2 - 250, 0)
# sprite.image.set_colorkey((0, 0, 0))
# sprite.image.blit(text, (0, 0))
# window.blit(sprite.image, sprite.rect)
pygame.display.flip()

text, word_x,word_y, speed = floating_words()

# Main Loop
run = True
while run:

    window.fill(bcg)
    word_y += speed
    window.blit(text, (word_x,word_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if word_y > SCREEN_HEIGHT:
        text, word_x, word_y, speed = floating_words()
    pygame.display.update()
