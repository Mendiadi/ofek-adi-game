from typing import Protocol

from xo.io.input import UserInput


class UserInputConsumer(Protocol):
    def handle_input(self, user_input: UserInput, data: dict | None = None):
        ...
