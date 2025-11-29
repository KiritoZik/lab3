def get_list_type(a: list[str]) -> str:
    """Определяет тип списка: int, str, mixed"""

    def is_int(s: str) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False

    lst = [is_int(x) for x in a]
    if all(lst):
        return 'int'
    elif not any(lst):
        return 'str'
    else:
        return 'mixed'
