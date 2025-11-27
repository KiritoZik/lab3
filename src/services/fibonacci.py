from src.services.Base import fibonacciServiceBase
from functools import lru_cache

class FibonacciService(fibonacciServiceBase):
    @lru_cache(maxsize=None)
    def fibonacci_recursive(self, number: int) -> int:
        if number == 0:
            return 0
        if number == 1:
            return 1
        return self.fibonacci_recursive(number - 1) + self.fibonacci_recursive(number - 2)

    def fibonacci(self, number: int, recursive: bool) -> int:
        if number < 0:
            raise ValueError("Введенное число не может быть отрицательным")
        else:
            if recursive:
                return self.fibonacci_recursive(number)
            else:
                if number == 0:
                    return 0
                if number == 1:
                    return 1
                a, b = 0, 1
                for _ in range(2, number + 1):
                    a, b = b, a + b
                return b
