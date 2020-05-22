import pygame

BLACK = (0, 0, 0)


class Object(pygame.sprite.Sprite):

    def __init__(self, color, width, heigt):
        super().__init__()

        self.image = pygame.Surface([width, heigt])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, heigt])

        self.rect = self.image.get_rect()

    def move_up(self, pixel):
        self.rect.y = self.rect.y - pixel

        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixel):

        self.rect.y = self.rect.y + pixel

        if self.rect.y > 700:
            self.rect.y = 0

    def move_right(self, pixel):

        self.rect.x = self.rect.x + pixel

        if self.rect.x > 700:
            self.rect.x = 0

    def move_left(self, pixel):

        self.rect.x = self.rect.x - pixel

        if self.rect.x < 0:
            self.rect.x = 0
