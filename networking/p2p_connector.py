from typing import Protocol

from mark_enum import Mark

class P2PConnector(Protocol):

    def connect(self, addr: tuple[str, int]):
        ...

    def send_location_fill(self, location: tuple[int, int], value: Mark):
        ...

    def wait_for_peer_location_fill(self) -> tuple[tuple[int, int], Mark]:
        ...