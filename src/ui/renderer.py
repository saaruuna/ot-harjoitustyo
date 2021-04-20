import pygame


class Renderer:
    def __init__(self, display, lab):
        pygame.init()

        self._display = display
        self._lab = lab
        self._font = pygame.font.SysFont('arialrounded', 24)
        self.rat_got_cheese = False
        self.rat_hit_trap = False

    def render(self):
        self._display.fill((0, 0, 0))

        display_width, display_height = pygame.display.get_window_size()

        title = self._font.render("Welcome to LabRat!", True, (255, 0, 0))
        self._display.blit(title, (0, 0))

        title = self._font.render("You are solving the lab "
        + str(self._lab.name), True, (255, 0, 0))
        self._display.blit(title, (0, 20))

        quit = self._font.render("Press Esc to quit.", True, (255, 0, 0))
        self._display.blit(quit, (0, 40))

        surface_width = self._lab.cell_size * len(self._lab.lab_map)
        surface_height = self._lab.cell_size * len(self._lab.lab_map[0])
        surface = pygame.Surface((surface_width, surface_height))

        surface_center = (
        (display_width - surface_width) / 2,
        (display_height - surface_height) / 2,
        )

        self._lab.all_sprites.draw(surface)
        self._display.blit(surface, surface_center)

        if self.rat_got_cheese:
            youwin = self._font.render("You win!", True, (255, 0, 0))
            self._display.blit(youwin, (0, 400))

        if self.rat_hit_trap:
            youlose = self._font.render("You lose...", True, (255, 0, 0))
            self._display.blit(youlose, (0, 400))

        pygame.display.flip()
