import typer
from rich.console import Console
from typer import Typer, Argument, Option
from typing_extensions import Annotated
from src.services.factorial import FactorialService
from src.services.fibonacci import FibonacciService
from src.services.sort_without_str import SortWithoutStrService
from src.services.sort_with_str import SortWithStrService

app = Typer()
console = Console()

@app.command()
def factorial(
        number: Annotated[int, Argument(exists=False, readable=False, help="Вычисление факториала числа")],
        recursive: Annotated[bool, Option("--recursive", "-r", help="Активация рекурсии")] = False
) -> None:
    result = FactorialService().factorial(number, recursive)
    console.print(result)



@app.command()
def fibonacci(
        number: Annotated[int, Argument(exists=False, readable=False, help="Вычисление числа Фибоначчи")],
        recursive: Annotated[bool, Option("--recursive", "-r", help="Активация рекурсии")] = False
) -> None:
    result = FibonacciService().fibonacci(number, recursive)
    console.print(result)


@app.command()
def counting_sort(a: Annotated[list[int], Argument(exists=False, readable=False, help="Сортировка пузырьком")]) -> None:
    result = SortWithoutStrService().counting_sort(a)
    console.print(result)

@app.command()
def radix_sort(a: Annotated[list[int], Argument(exists=False, readable=False, help="sighsjgsjgsfndjff")]) -> None:
    result = SortWithoutStrService().radix_sort(a)
    console.print(result)

@app.command()
def bucket_sort(a: Annotated[list[float], Argument(exists=False, readable=False, help="slfsdfnsdfnsdfnsdfnsdf")],
                buckets: Annotated[int|None, Option("--buckets", "-b" ,help="jskdjsadkjasds")] = None) -> None:
    result = SortWithoutStrService().bucket_sort(a, buckets)
    console.print(result)

# Со строкой

@app.command()
def bubble_sort(a: list[int]) -> None:
    result = SortWithStrService().bubble_sort(a)
    console.print(result)

@app.command()
def quick_sort(a: list[int]) -> None:
    result = SortWithStrService().quick_sort(a)
    console.print(result)

@app.command()
def heap_sort(a: list[int]) -> None:
    result  = SortWithStrService().heap_sort(a)
    console.print(result)



if __name__ == "__main__":
    app()
