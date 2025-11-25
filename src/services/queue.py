from typing import Any

from src.services.Base import QueueServiceBase

class QueueService(QueueServiceBase):
    def enqueue(self, item: Any) -> None:
        ...

    def dequeue(self) -> int:
        ...

    def front(self) -> int:
        ...

    def is_empty(self) -> bool:
        ...

    def __len__(self) -> int:
        ...


