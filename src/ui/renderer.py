import pygame

SCALE = 20

class Renderer:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.display_width, self.display_height = 480, 270
        self.display = pygame.Surface((self.display_width, self.display_height))
        self.window = pygame.display.set_mode((self.display_width, self.display_height))
        #self.font_name = '8-BIT WONDER.TTF'
        self.font = pygame.font.SysFont('arialrounded', 20)
        self.black, self.white = (0, 0, 0), (255, 255, 255)

    def render_lab(self, lab):
        self.display.fill(self.black)

        self._draw_text("You are solving the lab " + lab.name, 20, self.display_width / 2, 20)

        surface_width = SCALE * len(lab.lab_map)
        surface_height = SCALE * len(lab.lab_map[0])
        surface = pygame.Surface((surface_width, surface_height))

        surface_center = (
        (self.display_width - surface_width) / 2,
        (self.display_height - surface_height) / 2,
        )

        lab.all_sprites.draw(surface)
        self.display.blit(surface, surface_center)

        self.blit_screen()

    def render_game_over_menu(self, replayx, replayy, quitx, quity, status):
        self.display.fill(self.black)
        self._draw_text(status, 20, self.display_width / 2, self.display_height / 2)
        self._draw_text("PLAY AGAIN", 20, replayx, replayy)
        self._draw_text("QUIT", 20, quitx, quity)

    def render_main_menu(self, solvex, solvey, createx, createy):
        self.display.fill(self.black)
        self._draw_text("Welcome to LabRat!", 20, self.display_width / 2,
        self.display_height / 2 - 20)
        self._draw_text("SOLVE MAZE", 20, solvex, solvey)
        self._draw_text("CREATE MAZE", 20, createx, createy)

    def render_lab_selection_menu(self, lab_selection):
        self.display.fill(self.black)
        self._draw_text("Choose your lab:", 20, self.display_width / 2,
        self.display_height / 2 - 50)
        mid_width, mid_height = self.display_width / 2, self.display_height / 2
        firstx, firsty = mid_width, mid_height
        secondx, secondy = mid_width, mid_height + 30
        thirdx, thirdy = mid_width, mid_height + 60

        if len(lab_selection) == 1:
            self._draw_text(lab_selection[0].name, 20, firstx, firsty)
        elif len(lab_selection) == 2:
            self._draw_text(lab_selection[0].name, 20, firstx, firsty)
            self._draw_text(lab_selection[1].name, 20, secondx, secondy)
        elif len(lab_selection) == 3:
            self._draw_text(lab_selection[0].name, 20, firstx, firsty)
            self._draw_text(lab_selection[1].name, 20, secondx, secondy)
            self._draw_text(lab_selection[2].name, 20, thirdx, thirdy)

        pygame.draw.polygon(self.display, self.white, ((mid_width+150, mid_height), (mid_width+150, mid_height-20), (mid_width+170, mid_height-10)))
        pygame.draw.polygon(self.display, self.white, ((mid_width-150, mid_height), (mid_width-150, mid_height-20), (mid_width-170, mid_height-10)))


    def _draw_text(self, text, size, x_position, y_position):
        #font = pygame.font.Font(self.font_name,size)
        text_surface = self.font.render(text, True, self.white)
        text_rect = text_surface.get_rect()
        text_rect.center = (x_position, y_position)
        self.display.blit(text_surface, text_rect)

    def draw_cursor(self, x_position, y_position):
        self._draw_text("*", 15, x_position, y_position)

    def blit_screen(self):
        self.window.blit(self.display, (0, 0))
        pygame.display.update()
        self.game.event_handler.reset_keys()
