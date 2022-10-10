from typing import Protocol, Optional

from xo.io.input import UserInput


class UserInputConsumer(Protocol):
    def handle_input(self, user_input: UserInput, data: Optional[dict] = None):
        ...
