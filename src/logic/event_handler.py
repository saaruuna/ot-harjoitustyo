import pygame
from logic.event_queue import EventQueue

class EventHandler:
    def __init__(self):
        pygame.init()
        self.event_queue = EventQueue()
        self.up_key, self.down_key, self.right_key = False, False, False
        self.left_key, self.start_key, self.back_key = False, False, False
        self.quit_key = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_key = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start_key = True
                if event.key == pygame.K_BACKSPACE:
                    self.back_key = True
                if event.key == pygame.K_LEFT:
                    self.left_key = True
                if event.key == pygame.K_RIGHT:
                    self.right_key = True
                if event.key == pygame.K_UP:
                    self.up_key = True
                if event.key == pygame.K_DOWN:
                    self.down_key = True
                if event.key == pygame.K_ESCAPE:
                    self.quit_key = True

    def reset_keys(self):
        self.up_key, self.down_key, self.right_key = False, False, False
        self.left_key, self.start_key, self.back_key = False, False, False
        self.quit_key = False
