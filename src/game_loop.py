import pygame

class GameLoop:
    def __init__(self, lab, renderer, event_queue, clock, SCALE):
        self._lab = lab
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._scale = SCALE

    def start(self):
        while True:
            if self._handle_events() is False:
                break

            if self._lab.rat_got_cheese():
                self._renderer.rat_got_cheese = True
                break

            if self._lab.rat_hit_trap():
                self._renderer.rat_hit_trap = True
                break

            self._render()

            self._clock.tick(60)

        self._show_game_over()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._lab.move_rat(x_change=-self._scale)
                if event.key == pygame.K_RIGHT:
                    self._lab.move_rat(x_change=self._scale)
                if event.key == pygame.K_UP:
                    self._lab.move_rat(y_change=-self._scale)
                if event.key == pygame.K_DOWN:
                    self._lab.move_rat(y_change=self._scale)

                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.QUIT:
                return False

    def _handle_events_game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.QUIT:
                return False


    def _show_game_over(self):
        while True:
            if self._handle_events_game_over() is False:
                break

            self._render()

    def _render(self):
        self._renderer.render()
