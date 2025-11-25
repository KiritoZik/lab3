from abc import ABC, abstractmethod


class factorialServiceBase(ABC):

    @abstractmethod
    def factorial(self,
                  n: int,
                  recursive: bool) -> int:
        ...

class fibonacciServiceBase(ABC):
    @abstractmethod
    def fibonacci(self,
                  n: int,
                  recursive: bool) -> int:
        ...

class sortWithoutStrServiceBase(ABC):
    @abstractmethod
    def counting_sort(self, a:list[int]) -> list[int]:
        ...

    @abstractmethod
    def radix_sort(self, a:list[int]) -> list[int]:
        ...

    @abstractmethod
    def bucket_sort(self, a:list[int|float], buckets: int|None) -> list[int|float]:
        ...

class sortWithStrServiceBase(ABC):
    @abstractmethod
    def bubble_sort(self, a:list[int]) -> list[int]:
        ...

    @abstractmethod
    def quick_sort(self, a:list[int]) -> list[int]:
        ...

    @abstractmethod
    def heap_sort(self, a:list[int]) -> list[int]:
        ...

class StackServiceBase(ABC):

    @abstractmethod
    def push(self, x: int) -> None:
        ...

    @abstractmethod
    def pop(self) -> int:
        ...

    @abstractmethod
    def peek(self) -> int:
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...

    @abstractmethod
    def min(self) -> int:
        ...

class QueueServiceBase(ABC):
    @abstractmethod
    def enqueue(self, x: int) -> None:
        ...

    @abstractmethod
    def dequeue(self) -> int:
        ...

    @abstractmethod
    def front(self) -> int:
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...
