from src.services.Base import QueueServiceBase

class QueueService(QueueServiceBase):

    def __init__(self):
        self._lst = []

    def enqueue(self, x: int|str|float) -> None:
        self._lst.append(x)

    def dequeue(self) -> int|str|float:
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._lst.pop(0)

    def front(self) -> int|str|float:
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._lst[0]

    def is_empty(self) -> bool:
        return len(self._lst) == 0

    def __len__(self) -> int:
        return len(self._lst)
