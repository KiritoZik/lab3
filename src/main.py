import typer
from rich.console import Console
from typer import Typer, Argument, Option
from typing_extensions import Annotated
from typing import cast
from src.services.factorial import FactorialService
from src.services.fibonacci import FibonacciService
from src.services.sort_without_str import SortWithoutStrService
from src.services.sort_with_str import SortWithStrService
from src.services.stack import StackService
from src.services.queue import QueueService
from src.utils import get_list_type

app = Typer()
console = Console()

@app.command()
def factorial(
        number: Annotated[int, Argument(exists=False, readable=False, help="Вычисление факториала числа")],
        recursive: Annotated[bool, Option("--recursive", "-r", help="Активация рекурсии")] = False
) -> None:
    """
    Вычисление факториала числа.
    :param number: Неотрицательное целое число
    :param recursive: флаг для использования рекурсивного метода
    :return: None
    """
    try:
        result = FactorialService().factorial(number, recursive)
        console.print(result)
    except ValueError as e:
        console.print(f"[red]{e}")



@app.command()
def fibonacci(
        number: Annotated[int, Argument(exists=False, readable=False, help="Вычисление числа Фибоначчи")],
        recursive: Annotated[bool, Option("--recursive", "-r", help="Активация рекурсии")] = False
) -> None:
    """
    Вычисление числа Фибоначчи.
    :param number: Порядковый номер числа Фибоначчи
    :param recursive: флаг для использования рекурсивного метода
    :return: None
    """
    try:
        result = FibonacciService().fibonacci(number, recursive)
        console.print(result)
    except ValueError as e:
        console.print(f"[red]{e}")


@app.command()
def counting_sort(a: Annotated[list[int], Argument(exists=False, readable=False, help="Сортировка подсчетом")]) -> None:
    """
    Сортировка подсчетом.
    :param a: Список неотрицательных целых чисел
    :return: None
    """
    try:
        result = SortWithoutStrService().counting_sort(a)
        typer.echo(result)
    except ValueError as e:
        console.print(f"[red]{e}")


@app.command()
def radix_sort(a: Annotated[list[int], Argument(exists=False, readable=False, help="Поразрядная сортировка")]) -> None:
    """
    Поразрядная сортировка
    :param a: список неотрицательных целых чисел
    :return: None
    """
    try:
        result = SortWithoutStrService().radix_sort(a)
        typer.echo(result)
    except ValueError as e:
        console.print(f"[red]{e}")


@app.command()
def bucket_sort(a: Annotated[list[float], Argument(exists=False, readable=False, help="Блочная сортировка")],
                buckets: Annotated[int | None, Option("--buckets", "-b", help="Количество блоков")] = None) -> None:
    """
    Блочная сортировка
    :param a: список чисел с плавающей точкой
    :param buckets: количество блоков
    :return: None
    """
    result = SortWithoutStrService().bucket_sort(a, buckets)
    typer.echo(result)


# Со строкой
@app.command()
def bubble_sort(a: list[str]) -> None:
    """
    Сортировка пузырьком, принимающая список строк, а далее проверяет тип
    :param a: список строк
    :return: None
    """
    match get_list_type(a):
        case 'int':
            numbers: list[int] = [int(x) for x in a]
            typer.echo(SortWithStrService().bubble_sort(cast(list[int | str], numbers)))
        case 'str':
            typer.echo(SortWithStrService().bubble_sort(cast(list[int | str], a)))
        case 'mixed':
            console.print("[red]Все элементы списка должны быть одного типа (int или str)")


@app.command()
def quick_sort(a: list[str]) -> None:
    """
    Быстрая сортировка, принимающая список строк, а далее проверяет тип
    :param a: список строк
    :return: None
    """
    match get_list_type(a):
        case 'int':
            numbers: list[int] = [int(x) for x in a]
            typer.echo(SortWithStrService().quick_sort(cast(list[int | str], numbers)))
        case 'str':
            typer.echo(SortWithStrService().quick_sort(cast(list[int | str], a)))
        case 'mixed':
            console.print("[red]Все элементы списка должны быть одного типа (int или str)")


@app.command()
def heap_sort(a: list[str]) -> None:
    """
    Пирамидальная сортировка, принимающая список строк, а далее проверяет тип
    :param a: список строк
    :return: None
    """
    match get_list_type(a):
        case 'int':
            numbers: list[int] = [int(x) for x in a]
            typer.echo(SortWithStrService().heap_sort(cast(list[int | str], numbers)))
        case 'str':
            typer.echo(SortWithStrService().heap_sort(cast(list[int | str], a)))
        case 'mixed':
            console.print("[red]Все элементы списка должны быть одного типа (int или str)")

@app.command()
def stack() -> None:
    """
    Интерактивная работа со стеком
    :return: None
    """
    stack_service = StackService()
    stack_type = None

    typer.echo("Интерактивная работа со стеком")
    while (cmd := typer.prompt("Введите команду для стека", default="qui3232t").lower()) != "quit":
        match cmd:
            case 'info':
                typer.echo("push - добавить элемент\n pop - получить и удалить верхний элемент\n peek - получить верхний элемент\n"
                           "is_empty - проверить стек на пустоту\n min - минимальный элемент стека\n quit - выйти из интерактива")

            case 'push':
                item_input = typer.prompt("Элемент (число или строка)")
                item: int | float | str
                try:
                    try:
                        item = int(item_input)
                        item_type = 'number'
                    except ValueError:
                        item = float(item_input)
                        item_type = 'number'
                except ValueError:
                    item = item_input
                    item_type = 'str'

                if stack_type is None:
                    stack_type = item_type
                    stack_service.push(item)
                    typer.echo(f"Элемент {item} добавлен. Тип данных в стеке: {item_type}")
                elif item_type == stack_type:
                    stack_service.push(item)
                    typer.echo(f"Элемент {item} добавлен")
                else:
                    console.print(f"[red]Ошибка: ожидается элемент типа {stack_type}, получен {item_type}")
            case 'pop':
                try:
                    result = stack_service.pop()
                    typer.echo(result)
                    if stack_service.is_empty():
                        stack_type = None
                except IndexError as e:
                    console.print(f"[red]{e}")

            case 'peek':
                try:
                    typer.echo(stack_service.peek())
                except IndexError as e:
                    console.print(f"[red]{e}")

            case 'is_empty':
                typer.echo(stack_service.is_empty())

            case 'min':
                try:
                    typer.echo(stack_service.min())
                except IndexError as e:
                    console.print(f"[red]{e}")
            case 'len':
                typer.echo(len(stack_service))


@app.command()
def queue() -> None:
    """
    Интерактивная работа с очередью
    :return: None
    """
    queue_service = QueueService()
    queue_type = None

    typer.echo("Интерактивная работа с очередью")
    while (cmd := typer.prompt("Введите команду для очереди ", default="quit").lower()) != "quit":
        match cmd:
            case 'info':
                typer.echo("enqueue - добавить элемент в очередь\n dequeue - получить и удалить нижний элемент в очереди\n"
                           "front - получить нижний элемент\n is_empty - проверить очередь на пустоту")
            case 'enqueue':
                item_input = typer.prompt("Элемент (число или строка)")
                item: int | float | str
                try:
                    try:
                        item = int(item_input)
                        item_type = 'number'
                    except ValueError:
                        item = float(item_input)
                        item_type = 'number'
                except ValueError:
                    item = item_input
                    item_type = 'str'
                if queue_type is None:
                    queue_type = item_type
                    queue_service.enqueue(item)
                    console.print(f"Элемент {item} добавлен. Тип данных в очереди: {item_type}")
                elif item_type == queue_type:
                    queue_service.enqueue(item)
                    typer.echo(f"Элемент {item} добавлен")
                else:
                    console.print(f"[red]Ошибка: ожидается {queue_type}, получен {item_type}")

            case 'dequeue':
                try:
                    typer.echo(queue_service.dequeue())
                    if queue_service.is_empty():
                        queue_type = None
                except IndexError as e:
                    console.print(f"[red]{e}")
            case 'front':
                try:
                    typer.echo(queue_service.front())
                except IndexError as e:
                    console.print(f"[red]{e}")
            case 'is_empty':
                typer.echo(queue_service.is_empty())


if __name__ == "__main__":
    app()
