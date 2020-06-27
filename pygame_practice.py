import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 850
bcg = (255, 255, 255)
pygame.init()


# Window creation
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(bcg)
pygame.display.set_caption('SWIFTyping')
a = pygame.image.load('icon.png')
pygame.display.set_icon(a)


# background and text creation
background = pygame.image.load('lightkey.jpg').convert()
window.blit(background, (0, 0))
font = pygame.font.SysFont('Ariel', 70, bold=True)
text = font.render('SWIFTyping Test', True, (255, 0, 0))
sprite = pygame.sprite.Sprite()
sprite.image = pygame.Surface([700, 100]).convert()
sprite.rect = (SCREEN_WIDTH / 2 - 250, 0)
sprite.image.set_colorkey((0, 0, 0))
sprite.image.blit(text, (0, 0))
window.blit(sprite.image, sprite.rect)
pygame.display.flip()

# Main Loop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # pygame.display.update()
