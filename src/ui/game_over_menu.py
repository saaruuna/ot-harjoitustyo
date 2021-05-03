import pygame
from ui.menu import Menu

class GameOverMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Play again"
        self.status = ""
        self.replayx, self.replayy = 200, 240
        self.quitx, self.quity = 400, 240
        self.cursor_rect.midtop = (self.replayx + self.offset, self.replayy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.event_handler.handle_events()
            self._check_input()
            self.renderer.render_game_over_menu(self.replayx, self.replayy, self.quitx, self.quity, self.status)
            self.renderer.draw_cursor(self.cursor_rect.x, self.cursor_rect.y)
            self.renderer.blit_screen()

    def _move_cursor(self):
        if self.event_handler.right_key:
            if self.state == "Play again":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.replayx + self.offset, self.replayy)
                self.state = "Play again"
        elif self.event_handler.left_key:
            if self.state == "Play again":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.replayx + self.offset, self.replayy)
                self.state = "Play again"

    def _check_input(self):
        self._move_cursor()
        if self.event_handler.quit_key:
            self.game.playing, self.game.running = False, False
            self.run_display = False
        elif self.event_handler.start_key:
            if self.state == "Play again":
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            elif self.state == "Quit":
                self.game.playing, self.game.running = False, False
                self.run_display = False
