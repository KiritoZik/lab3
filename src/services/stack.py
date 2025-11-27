from src.services.Base import StackServiceBase

class StackService(StackServiceBase):
    def  __init__(self):
        self._lst = []
        self._mini = []

    def push(self, a: int|str|float) -> None:
        self._lst.append(a)
        if (not self._mini) or (self.min() >= a):
            self._mini.append(a)

    def pop(self) -> int|str|float:
        if self.is_empty():
            raise IndexError("Стек пуст")
        if self._mini and self.min() == self._lst[-1]:
            self._mini.pop()
        return self._lst.pop()

    def peek(self) -> int|str|float:
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._lst[-1]

    def is_empty(self) -> bool:
        return len(self._lst) == 0

    def __len__(self) -> int:
        return len(self._lst)-1

    def min(self) -> int|str|float:
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._mini[-1]
