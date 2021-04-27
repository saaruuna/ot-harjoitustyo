import pygame

class Menu:
    def __init__(self, game):
        self.game = game
        self.run_display = True
        self.game_loop = self.game.game_loop
        self.renderer = self.game.renderer
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

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
            self.game_loop.handle_events()
            self.check_input()
            self.renderer.render_main_menu(self.solvex, self.solvey, self.createx, self.createy)
            self.renderer.draw_cursor(self.cursor_rect.x, self.cursor_rect.y)
            self.renderer.blit_screen()

    def move_cursor(self):
        if self.game_loop.down_key:
            if self.state == "Solve":
                self.cursor_rect.midtop = (self.createx + self.offset, self.createy)
                self.state = "Create"
            elif self.state == "Create":
                self.cursor_rect.midtop = (self.solvex + self.offset, self.solvey)
                self.state = "Solve"
        elif self.game_loop.up_key:
            if self.state == "Solve":
                self.cursor_rect.midtop = (self.createx + self.offset, self.createy)
                self.state = "Create"
            elif self.state == "Create":
                self.cursor_rect.midtop = (self.solvex + self.offset, self.solvey)
                self.state = "Solve"

    def check_input(self):
        self.move_cursor()
        if self.game_loop.start_key:
            if self.state == "Solve":
                self.game.playing = True
                self.run_display = False
            if self.state == "Create":
                self.run_display = False

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
            self.game_loop.handle_events()
            self.check_input()
            self.renderer.render_game_over_menu(self.replayx, self.replayy, self.quitx, self.quity, self.status)
            self.renderer.draw_cursor(self.cursor_rect.x, self.cursor_rect.y)
            self.renderer.blit_screen()

    def move_cursor(self):
        if self.game_loop.right_key:
            if self.state == "Play again":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.replayx + self.offset, self.replayy)
                self.state = "Play again"
        elif self.game_loop.left_key:
            if self.state == "Play again":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.replayx + self.offset, self.replayy)
                self.state = "Play again"

    def check_input(self):
        self.move_cursor()
        if self.game_loop.start_key:
            if self.state == "Play again":
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            elif self.state == "Quit":
                self.game.playing, self.game.running = False, False
                self.run_display = False
