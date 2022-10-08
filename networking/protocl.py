from typing import Protocol
from mark_enum import Mark

class CommunicationProtocol(Protocol):

    def pack_location_fill(self, location: tuple[int, int], value: Mark):
        ...

    def unpack_location_fill(self, data: bytes) -> tuple[tuple[int, int], Mark]:
        ...