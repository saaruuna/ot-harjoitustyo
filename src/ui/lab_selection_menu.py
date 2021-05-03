import pygame
from ui.menu import Menu

class LabSelectionMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "0"
        self.lab_selection = []

        j = 0
        while j < len(self.game.labs):
            self.lab_selection.append(self.game.labs[j:j+3])
            j += 3

        self.page = 0
        mid_width, mid_height = self.renderer.display_width / 2, self.renderer.display_height / 2
        self.firstx, self.firsty = mid_width, mid_height
        self.secondx, self.secondy = mid_width, mid_height + 30
        self.thirdx, self.thirdy = mid_width, mid_height + 60
        self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)

    def display_menu(self):
        self.page = 0
        self.state = "0"
        self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)
        self.run_display = True
        while self.run_display:
            self.event_handler.handle_events()
            self._check_input()
            self.renderer.render_lab_selection_menu(self.lab_selection[self.page])
            self.renderer.draw_cursor(self.cursor_rect.x, self.cursor_rect.y)
            self.renderer.blit_screen()

    def _move_cursor(self):
        if self.event_handler.down_key:
            if self.state == "0":
                if (len(self.lab_selection[self.page]) > 1):
                    self.cursor_rect.midtop = (self.secondx + self.offset, self.secondy)
                    self.state = "1"
            elif self.state == "1":
                if (len(self.lab_selection[self.page]) > 2):
                    self.cursor_rect.midtop = (self.thirdx + self.offset, self.thirdy)
                    self.state = "2"
            elif self.state == "2":
                if (len(self.lab_selection[self.page]) > 2):
                    self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)
                    self.state = "0"
        elif self.event_handler.up_key:
            if self.state == "0":
                if (len(self.lab_selection[self.page]) > 2):
                    self.cursor_rect.midtop = (self.thirdx + self.offset, self.thirdy)
                    self.state = "2"
            elif self.state == "1":
                if (len(self.lab_selection[self.page]) > 1):
                    self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)
                    self.state = "0"
            elif self.state == "2":
                if (len(self.lab_selection[self.page]) > 2):
                    self.cursor_rect.midtop = (self.secondx + self.offset, self.secondy)
                    self.state = "1"
        elif self.game.event_handler.left_key:
            self.state = "0"
            self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)
        elif self.game.event_handler.right_key:
            self.state = "0"
            self.cursor_rect.midtop = (self.firstx + self.offset, self.firsty)

    def _check_input(self):
        self._move_cursor()
        if self.event_handler.quit_key:
            self.game.playing, self.game.running = False, False
            self.run_display = False
        elif self.event_handler.start_key:
            if self.state == "0":
                choice = self.page*3
                self.game.lab = self.game.labs[choice]
                self.game.playing = True
                self.run_display = False
            elif self.state == "1":
                choice = self.page*3 + 1
                self.game.lab = self.game.labs[choice]
                self.game.playing = True
                self.run_display = False
            elif self.state == "2":
                choice = self.page*3 + 2
                self.game.lab = self.game.labs[choice]
                self.game.playing = True
                self.run_display = False
        elif self.event_handler.left_key:
            if (self.page > 0):
                self.page -= 1
        elif self.event_handler.right_key:
            if (self.page + 1 < len(self.lab_selection)):
                self.page += 1
