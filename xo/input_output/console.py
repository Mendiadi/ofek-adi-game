from __future__ import annotations

import os
import time
from typing import TYPE_CHECKING

from xo.input_output.user_input_enum import UserInput
from xo.mark_enum import Mark


def cls():
    os.system("cls" if os.name == "nt" else "clear")


if TYPE_CHECKING:
    from xo.input_output.user_input_consumer import UserInputConsumer


class Console:
    PRINTING_RATE = 10

    def __init__(self):
        self._grid: list[list[Mark]] = [
            [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
            [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
            [Mark.EMPTY, Mark.EMPTY, Mark.EMPTY],
        ]
        self._is_running = False
        self._alert = ""
        self._input_consumers: list[UserInputConsumer] = []

    def mark(self, location: tuple[int, int], value: Mark):
        x, y = location
        self._grid[x][y] = value

    def start_game(self):
        self._is_running = True
        while self._is_running:
            self._print_screen()
            time.sleep(1 / self.PRINTING_RATE)
            cls()

    def stop_game(self):
        self._is_running = False

    def set_alert(self, alert: str):
        self._alert = alert
        if not self._is_running:
            print(alert)

    def stop_alert(self):
        self._alert = ""

    def subscribe_consumer(self, consumer: UserInputConsumer):
        ...

    def _print_screen(self):
        print(
            f"""
{self._grid[0][0].value} | {self._grid[0][1].value} | {self._grid[0][2].value}
--------
{self._grid[1][0].value} | {self._grid[1][1].value} | {self._grid[1][2].value}
--------
{self._grid[2][0].value} | {self._grid[2][1].value} | {self._grid[2][2].value}

{self._alert}
            """
        )

    def _send_input_to_consumers(self, user_input: UserInput, data: dict | None = None):
        for consumer in self._input_consumers:
            consumer.handle_input(user_input, data)

    def _handle_quit_input(self):
        self._send_input_to_consumer(UserInput.QUIT)

    def _handle_game_start_input(self):
        if not self._is_running:
            self._send_input_to_consumers(UserInput.START_GANE)

    def _handle_game_stop_input(self):
        if self._is_running:
            self._send_input_to_consumers(UserInput.STOP_GAME)

    def _handle_mark_input(self):
        if self._is_running:
            return

        # self._send_input_to_consumers(UserInput.MARKING, {
        #     consts.MARK_LOCATION_INPUT_DATA_KEY: location
        # })

    def _input_thread(self):
        # input_handler_resolver = {
        #     UserInput.MARKING: self._handle_mark_input,
        #     UserInput.
        # }
        # while True:
        #     user_input = input()
        #     if
        ...
