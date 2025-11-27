from src.services.Base import factorialServiceBase

class FactorialService(factorialServiceBase):
    def  factorial_recursive(self, number: int) -> int:
        if number == 0:
            return 1
        return number * self.factorial_recursive(number - 1)

    def factorial(self,
                  number: int,
                  recursive: bool) -> int:

        if number < 0:
            raise ValueError("Факториал не определен для отрицательных чисел")
        else:
            if recursive:
                return self.factorial_recursive(number)
            else:
                result = 1
                for i in range(1, number + 1):
                    result *= i
                return result
