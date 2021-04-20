import sys
import pygame

class GameLoop:
    def __init__(self, lab, renderer, event_queue, clock, cell_size):
        self._lab = lab
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size

    def start(self):
        while True:
            self._handle_events()

            self._render()

            if self._lab.rat_got_cheese():
                self._renderer.rat_got_cheese = True
                break

            if self._lab.rat_hit_trap():
                self._renderer.rat_hit_trap = True
                break

            self._clock.tick(60)

        self._show_game_over()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._lab.move_rat(x_change=-self._cell_size)
                if event.key == pygame.K_RIGHT:
                    self._lab.move_rat(x_change=self._cell_size)
                if event.key == pygame.K_UP:
                    self._lab.move_rat(y_change=-self._cell_size)
                if event.key == pygame.K_DOWN:
                    self._lab.move_rat(y_change=self._cell_size)

                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.QUIT:
                sys.exit()

    def _show_game_over(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.QUIT:
                    sys.exit()

            self._render()

    def _render(self):
        self._renderer.render()
