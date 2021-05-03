import pygame
from repositories import lab_repository

class Menu:
    def __init__(self, game):
        self.game = game
        self.run_display = True
        self.event_handler = self.game.event_handler
        self.renderer = self.game.renderer
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100
