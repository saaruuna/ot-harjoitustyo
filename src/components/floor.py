import pygame
from load_image import load_image

class Floor(pygame.sprite.Sprite):
    def __init__(self, x_position=0, y_position=0):
        super().__init__()

        self.image = load_image("floor.png")

        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position
