from dataclasses import dataclass

@dataclass
class Message:
    message_to_who: str
    message_string: list[str]
