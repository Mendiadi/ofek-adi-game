import socket
from mark_enum import Mark
from typing import Optional

class TCPP2PConnector:

    def __init__(self):
        self._socket: Optional[socket.socket] = None

    def connect(self, addr: tuple[str, int]):
        self._socket = socket.socket()
        self._socket.connect(addr)

    def send_location_fill(self, location: tuple[int, int], value: Mark):
        ...

    def wait_for_peer_location_fill(self) -> tuple[tuple[int, int], Mark]:
        ...