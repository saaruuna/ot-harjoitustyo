import pygame
from ui.game_loop import GameLoop
from ui.renderer import Renderer
from ui.menu import *

SCALE = 20

class Game:
    def __init__(self, labs):
        pygame.init()
        self.labs = labs
        self.renderer = Renderer(self)
        self.game_loop = GameLoop()
        self.running, self.playing = True, False
        self.main_menu = MainMenu(self)
        self.game_over_menu = GameOverMenu(self)
        self.choice = 1
        self.lab = labs[self.choice]
        self.curr_menu = self.main_menu

    def run(self):
        while self.playing:
            self.play()

    def play(self):
        if self.lab.rat_got_cheese():
            self.game_over_menu.status = "You win :)"
            self.curr_menu = self.game_over_menu
            self.lab.reset_lab()
            self.playing = False

        if self.lab.rat_hit_trap():
            self.game_over_menu.status = "You lose :("
            self.curr_menu = self.game_over_menu
            self.lab.reset_lab()
            self.playing = False

        self.game_loop.handle_events()

        if self.game_loop.quit_key:
            self.running, self.playing = False
        if self.game_loop.left_key:
            self.lab.move_rat(x_change=-SCALE)
        if self.game_loop.right_key:
            self.lab.move_rat(x_change=SCALE)
        if self.game_loop.up_key:
            self.lab.move_rat(y_change=-SCALE)
        if self.game_loop.down_key:
            self.lab.move_rat(y_change=SCALE)

        self.renderer.render_lab(self.lab)
