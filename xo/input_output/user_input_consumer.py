from typing import Protocol

from xo.input_output.user_input_enum import UserInput


class UserInputConsumer(Protocol):
    def handle_input(self, user_input: UserInput, data: dict | None = None):
        ...
