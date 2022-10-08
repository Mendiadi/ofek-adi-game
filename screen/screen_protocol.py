from typing import Protocol

from mark_enum import Mark

class Screen(Protocol):

    def fill_location(self, location: tuple[int, int], value: Mark):
        ...

    def start(self):
        ...

    def stop(self):
        ...