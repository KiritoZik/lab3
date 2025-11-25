
from src.services.Base import QueueServiceBase

class QueueService(QueueServiceBase):

    def __init__(self):
        self._lst = []
        self._mini = []

    def enqueue(self, x: int) -> None:
        self._lst.append(x)

    def dequeue(self) -> int:
        if not self.is_empty():
            return self._lst.pop(0)
        return 0

    def front(self) -> int:
        if not self.is_empty():
            return self._lst[0]
        return 0

    def is_empty(self) -> bool:
        return len(self._lst) == 0

    def __len__(self) -> int:
        return len(self._lst)
