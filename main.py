import pygame
from object import Object

pygame.init()

RED = (139, 0, 0)
WHITE = (255, 255, 255)

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("QUESTION 2")

objectA = Object(WHITE, 10, 10)
objectA.rect.x = 350
objectA.rect.y = 200

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(objectA)

carryOn = True
clock = pygame.time.Clock()

while carryOn:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        objectA.move_up(5)
    if keys[pygame.K_DOWN]:
        objectA.move_down(5)
    if keys[pygame.K_RIGHT]:
        objectA.move_right(5)
    if keys[pygame.K_LEFT]:
        objectA.move_left(5)
    all_sprites_list.update()

    screen.fill(RED)

    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
