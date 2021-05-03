import pygame
from logic.event_handler import EventHandler
from ui.renderer import Renderer
from ui.menu import Menu
from ui.main_menu import MainMenu
from ui.game_over_menu import GameOverMenu
from ui.lab_selection_menu import LabSelectionMenu

SCALE = 20

class Game:
    def __init__(self, labs):
        pygame.init()
        self.labs = labs
        self.renderer = Renderer(self)
        self.event_handler = EventHandler()
        self.running, self.playing = True, False
        self.main_menu = MainMenu(self)
        self.game_over_menu = GameOverMenu(self)
        self.lab_selection_menu = LabSelectionMenu(self)
        self.lab = labs[0]
        self.curr_menu = self.main_menu

    def run(self):
        while self.playing:
            self._play()

        self.lab.reset_lab()

    def _play(self):
        if self.lab.rat_got_cheese():
            self.game_over_menu.status = "You win :)"
            self.curr_menu = self.game_over_menu
            self.playing = False

        if self.lab.rat_hit_trap():
            self.game_over_menu.status = "You lose :("
            self.curr_menu = self.game_over_menu
            self.playing = False

        self.event_handler.handle_events()

        if self.event_handler.quit_key:
            self.running, self.playing = False, False
        if self.event_handler.left_key:
            self.lab.move_rat(x_change=-SCALE)
        if self.event_handler.right_key:
            self.lab.move_rat(x_change=SCALE)
        if self.event_handler.up_key:
            self.lab.move_rat(y_change=-SCALE)
        if self.event_handler.down_key:
            self.lab.move_rat(y_change=SCALE)

        self.renderer.render_lab(self.lab)
