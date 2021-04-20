import unittest
import pygame

from lab import Lab
from game_loop import GameLoop


class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        pass


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def __init__(self):
        self.rat_got_cheese = False
        self.rat_hit_trap = False

    def render(self):
        pass

LAB_MAP =   [[1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 3, 2, 4, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]]

SCALE = 20


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.lab = Lab("TEST", LAB_MAP, SCALE)

    def test_can_get_cheese(self):
        pygame.init()

        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_UP),
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
            StubEvent(pygame.KEYDOWN, pygame.K_DOWN),
        ]

        game_loop = GameLoop(
            self.lab,
            StubRenderer(),
            StubEventQueue(events),
            StubClock(),
            SCALE
        )

        game_loop.start()

        self.assertTrue(self.lab.rat_got_cheese())

    def test_can_hit_trap(self):
        pygame.init()

        events = [
            StubEvent(pygame.KEYDOWN, pygame.K_LEFT),
        ]

        game_loop = GameLoop(
            self.lab,
            StubRenderer(),
            StubEventQueue(events),
            StubClock(),
            SCALE
        )

        game_loop.start()

        self.assertTrue(self.lab.rat_hit_trap())
