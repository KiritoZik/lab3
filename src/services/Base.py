from abc import ABC, abstractmethod


class factorialServiceBase(ABC):
    """Абстрактный класс для сервиса факториала."""

    @abstractmethod
    def factorial(self,
                  n: int,
                  recursive: bool) -> int:
        """
        Вычисление факториала числа
        :param n: неотрицательное целое число
        :param recursive: флаг для использования рекурсивного метода
        :return: факториал числа
        """
        ...


class fibonacciServiceBase(ABC):
    """Абстрактный класс для сервиса Фибоначчи."""

    @abstractmethod
    def fibonacci(self,
                  n: int,
                  recursive: bool) -> int:
        """
        Вычисление числа Фибоначчи
        :param n: порядковый номер числа Фибоначчи
        :param recursive: флаг для использования рекурсивного метода
        :return: число Фибоначчи
        """
        ...


class sortWithoutStrServiceBase(ABC):
    """Абстрактный базовый класс для сортировок числовых массивов."""

    @abstractmethod
    def counting_sort(self, a: list[int]) -> list[int]:
        """
        Сортировка подсчетом
        :param a: список неотрицательных целых чисел
        :return: отсортированный список
        """
        ...

    @abstractmethod
    def radix_sort(self, a: list[int]) -> list[int]:
        """
        Поразрядная сортировка
        :param a: список неотрицательных целых чисел
        :return: отсортированный список
        """
        ...

    @abstractmethod
    def bucket_sort(self, a: list[int | float], buckets: int | None) -> list[int | float]:
        """
        Блочная сортировка
        :param a: список чисел
        :param buckets: количество блоков
        :return: отсортированный список
        """
        ...


class sortWithStrServiceBase(ABC):
    """Абстрактный базовый класс для сортировок числовых и строковых массивов."""

    @abstractmethod
    def bubble_sort(self, a: list[int | str]) -> list[int | str]:
        """
        Сортировка пузырьком.
        :param a: Список целых чисел или строк
        :return: отсортированный список
        """
        ...

    @abstractmethod
    def quick_sort(self, a: list[int | str]) -> list[int | str]:
        """
        Быстрая сортировка.
        :param a: Список целых чисел или строк
        :return: отсортированный список
        """
        ...

    @abstractmethod
    def heap_sort(self, a: list[int | str]) -> list[int | str]:
        """
        Пирамидальная сортировка.
        :param a: Список целых чисел или строк
        :return: отсортированный список
        """
        ...


class StackServiceBase(ABC):
    """Абстрактный базовый класс для стека."""

    @abstractmethod
    def push(self, x: int | str | float) -> None:
        """
        Добавление элемента в стек.
        :param x: Элемент для добавления
        :return: None
        """
        ...

    @abstractmethod
    def pop(self) -> int | str | float:
        """
        Извлечение верхнего элемента из стека.
        :return: Верхний элемент стека
        """
        ...

    @abstractmethod
    def peek(self) -> int | str | float:
        """
        Получение верхнего элемента без удаления.
        :return: Верхний элемент стека
        """
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Проверка стека на пустоту.
        :return: True если стек пуст, иначе False
        """
        ...

    @abstractmethod
    def __len__(self) -> int:
        """
        Получение размера стека.
        :return: Количество элементов в стеке
        """
        ...

    @abstractmethod
    def min(self) -> int | str | float:
        """
        Получение минимального элемента стека
        :return: минимальный элемент
        """
        ...


class QueueServiceBase(ABC):
    """Абстрактный базовый класс для очереди."""

    @abstractmethod
    def enqueue(self, x: int | str | float) -> None:
        """
        Добавление элемента в конец очереди
        :param x: элемент для добавления
        :return: None
        """
        ...

    @abstractmethod
    def dequeue(self) -> int | str | float:
        """
        Извлечение элемента из начала очереди.
        :return: Первый элемент очереди
        """
        ...

    @abstractmethod
    def front(self) -> int | str | float:
        """
        Получение первого элемента без удаления
        :return: первый элемент очереди
        """
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Проверка очереди на пустоту.
        :return: True если очередь пуста, иначе False
        """
        ...

    @abstractmethod
    def __len__(self) -> int:
        """
        Получение размера очереди
        :return: Количество элементов в очереди
        """
        ...
