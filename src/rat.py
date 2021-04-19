import pygame
from load_image import load_image


class Rat(pygame.sprite.Sprite):
    def __init__(self, x_position=0, y_position=0, is_dead=False, is_happy=False):
        super().__init__()

        self.is_dead = is_dead
        self.is_happy = is_happy

        self._images = self._load_images()

        self.image = self._images["rat"]
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

    def update(self):
        if self.is_dead:
            self.image = self._images["dead_rat"]
        else:
            self.image = self._images["rat"]

        if self.is_happy:
            self.image = self._images["happy_rat"]
        else:
            self.image = self._images["rat"]

    def _load_images(self):
        return {
            "rat": load_image("rat.png"),
            "dead_rat": load_image("dead_rat.png"),
            "happy_rat": load_image("happy_rat.png")
        }
