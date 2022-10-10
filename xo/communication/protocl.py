from __future__ import annotations

from typing import Protocol

from xo.mark_enum import Mark


class CommunicationProtocol(Protocol):
    @classmethod
    def connect(cls, addr: str) -> CommunicationProtocol:
        ...

    def send_movement(self, location: tuple[int, int], value: Mark):
        ...

    def recv_movment(
        self,
    ) -> tuple[tuple[int, int], Mark]:
        ...
