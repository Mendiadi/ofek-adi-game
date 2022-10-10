import os
import time
from xo.mark_enum import Mark


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Console:
    PRINTING_RATE = 10
    def __init__(self):
        self._grid: list[list[Mark]] = [
            [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
            [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
            [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
        ]
        self._is_running = False

    def fill_location(self, location: tuple[int, int], value: Mark):
        x, y = location
        self._grid[x][y] = value

    def start(self):
        self._is_running = True
        while self._is_running:
            self._print_screen()
            time.sleep(1 / self.PRINTING_RATE)
            cls()

    def stop(self):
        self._is_running = False

    def _print_screen(self):
        print(f"""
{self._grid[0][0].value} | {self._grid[0][1].value} | {self._grid[0][2].value}
--------
{self._grid[1][0].value} | {self._grid[1][1].value} | {self._grid[1][2].value}
--------
{self._grid[2][0].value} | {self._grid[2][1].value} | {self._grid[2][2].value} 
            """)