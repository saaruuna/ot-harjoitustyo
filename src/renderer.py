import pygame


class Renderer:
    def __init__(self, display, lab):
        self._display = display
        self._lab = lab

    def render(self):
        self._lab.all_sprites.draw(self._display)

        pygame.display.update()
