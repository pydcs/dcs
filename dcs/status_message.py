from enum import IntEnum


class MessageSeverity(IntEnum):
    INFO = 0
    WARN = 1
    ERROR = 2


class MessageType(IntEnum):
    ONBOARD_NUM_DUPLICATE = 0
    PARKING_SLOT_NOT_VALID = 1
    PARKING_SLOTS_FULL = 3
    MISSION_FORMAT_OLD = 4


class StatusMessage:
    def __init__(self, message: str, type_: MessageType, severity: MessageSeverity = MessageSeverity.ERROR):
        self._message = message
        self._type = type_
        self._severity = severity

    @property
    def type(self) -> MessageType:
        return self._type

    @property
    def severity(self) -> MessageSeverity:
        return self._severity

    @property
    def message(self) -> str:
        return self._message
