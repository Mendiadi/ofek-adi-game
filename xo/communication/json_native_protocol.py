from __future__ import annotations

import json
import socket

from xo.mark_enum import Mark


class JsonNativeProtocol:
    LOCATION_FIELD = "location"
    FIRST_LOCATION_FIELD = "x"
    SECOND_LOCATION_FIELD = "y"
    VALUE_FIELD = "value"
    BUFFER_SIZE = 2048

    @classmethod
    def connect(cls, addr: str) -> JsonNativeProtocol:
        # return cls(None)
        ...

    def __init__(self, sock: socket.socket):
        self._sock = sock

    def send_movement(self, location: tuple[int, int], value: Mark):
        x, y = location
        data = json.dumps(
            {
                self.LOCATION_FIELD: {
                    self.FIRST_LOCATION_FIELD: x,
                    self.SECOND_LOCATION_FIELD: y,
                },
                self.VALUE_FIELD: value.value,
            }
        ).encode()
        self._sock.sendall(data)

    def recv_movement(self) -> tuple[tuple[int, int], Mark]:
        try:
            loaded_data = json.loads(self._sock.recv(self.BUFFER_SIZE))
            x, y = loaded_data[self.LOCATION_FIELD]
            value = Mark(loaded_data[self.VALUE_FIELD])
        except (TypeError, KeyError, json.decoder.JSONDecodeError):
            raise ValueError("Invalid data received")
        return (x, y), value
