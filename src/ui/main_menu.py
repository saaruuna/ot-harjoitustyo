import pygame
from ui.menu import Menu

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Solve"
        mid_width, mid_height = self.renderer.display_width / 2, self.renderer.display_height / 2
        self.solvex, self.solvey = mid_width, mid_height + 30
        self.createx, self.createy = mid_width, mid_height + 50
        self.cursor_rect.midtop = (self.solvex + self.offset, self.solvey)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.event_handler.handle_events()
            self._check_input()
            self.renderer.render_main_menu(self.solvex, self.solvey, self.createx, self.createy)
            self.renderer.draw_cursor(self.cursor_rect.x, self.cursor_rect.y)
            self.renderer.blit_screen()

    def _move_cursor(self):
        if self.event_handler.down_key:
            if self.state == "Solve":
                self.cursor_rect.midtop = (self.createx + self.offset, self.createy)
                self.state = "Create"
            elif self.state == "Create":
                self.cursor_rect.midtop = (self.solvex + self.offset, self.solvey)
                self.state = "Solve"
        elif self.event_handler.up_key:
            if self.state == "Solve":
                self.cursor_rect.midtop = (self.createx + self.offset, self.createy)
                self.state = "Create"
            elif self.state == "Create":
                self.cursor_rect.midtop = (self.solvex + self.offset, self.solvey)
                self.state = "Solve"

    def _check_input(self):
        self._move_cursor()
        if self.event_handler.quit_key:
            self.game.playing, self.game.running = False, False
            self.run_display = False
        elif self.event_handler.start_key:
            if self.state == "Solve":
                self.game.curr_menu = self.game.lab_selection_menu
                self.run_display = False
            if self.state == "Create":
                self.run_display = False
