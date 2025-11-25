from src.services.Base import StackServiceBase

class StackService(StackServiceBase):
    def push(self, a: int) -> int:
        ...

    def pop(self) -> int:
        ...

    def peek(self) -> int:
        ...

    def is_empty(self) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def min(self) -> int:
        ...
