from src.services.Base import StackServiceBase

class StackService(StackServiceBase):
    def  __init__(self):
        self._lst = []
        self._mini = []

    def push(self, a: int) -> None:
        self._lst.append(a)
        if (not self._mini) or (self.min() >= a):
            self._mini.append(a)

    def pop(self) -> int:
        if  self.min() == self._lst[-1]:
            self._mini.pop()
        if not( self.is_empty() ):
            return self._lst.pop()
        return 0

    def peek(self) -> int:
        if not(self.is_empty()):
            return self._lst[-1]
        return 0

    def is_empty(self) -> bool:
        return len(self._lst) == 0

    def __len__(self) -> int:
        return len(self._lst)

    def min(self) -> int:
        return self._mini[-1]
