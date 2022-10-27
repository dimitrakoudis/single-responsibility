from dataclasses import dataclass
from typing import Optional, Self


@dataclass
class Post:
    id: int
    title: str
    body: Optional[str] = None

    @classmethod
    def create(cls, id, title, body) -> Self:
        pass

    def get_body_word_count(self) -> int:
        pass

    def to_json(self) -> dict:
        pass

    def publish(self) -> None:
        pass
