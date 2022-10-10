from typing import Protocol, TYPE_CHECKING

from xo.mark_enum import Mark

if TYPE_CHECKING:
    from xo.io.user_input_consumer import UserInputConsumer


class UserIO(Protocol):
    def start_game(self):
        ...

    def stop_game(self):
        ...

    def set_alert(self, alert: str):
        ...

    def stop_alert(self):
        ...

    def mark(self, location: tuple[int, int], value: Mark):
        ...

    def subscribe_consumer(self, consumer: UserInputConsumer):
        ...
