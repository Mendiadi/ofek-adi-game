from mark_enum import Mark
import json

class JsonNativeProtocl:
    LOCATION_FIELD = "location"
    FIRST_LOCATION_FIELD = "x"
    SECOND_LOCATION_FIELD = "y"
    VALUE_FIELD = "value"

    def pack_location_fill(self, location: tuple[int, int], value: Mark) -> bytes:
        x, y = location
        return json.dumps({
            self.LOCATION_FIELD : {
                self.FIRST_LOCATION_FIELD: x,
                self.SECOND_LOCATION_FIELD: y,
            },
            self.VALUE_FIELD: value.value
        }).encode()

    def unpack_location_fill(self, data: bytes) -> tuple[tuple[int, int], Mark]:
        try:
            loaded_data = json.loads(data)
            x, y = loaded_data[self.LOCATION_FIELD]
            value = Mark(loaded_data[self.VALUE_FIELD])
        except (KeyError, json.decoder.JSONDecodeError):
            raise ValueError("Invalid data received")
        return (x, y), value
