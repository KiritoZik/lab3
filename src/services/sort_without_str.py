from src.services.Base import sortWithoutStrServiceBase

class SortWithoutStrService(sortWithoutStrServiceBase):
    def counting_sort(self, a:list[int]) -> list[int]:
        if not a:
            return []
        if any(x < 0 for x in a):
            raise ValueError("Сортировка подсчетом работает только с неотрицательными числами")
        result: list[int] = [0] * len(a)
        k = max(a) + 1
        lst: list[int] = [0] * k
        for i in a:
            lst[i] += 1

        carry = 0
        for i in range(k):
            temp = lst[i]
            lst[i] = carry
            carry += temp

        for i in a:
            result[lst[i]] = i
            lst[i] += 1

        return result

    def radix_sort(self, a:list[int]) -> list[int]:

        def digit(num: int, raz: int) -> int:
            return (num // (10 ** (raz - 1))) % 10

        if len(a) < 2:
            return a
        if any(x < 0 for x in a):
            raise ValueError("Поразрядная сортировка работает только с неотрицательными числами")
        base = 10
        pre_result: list[int] = [0] * len(a)
        max_raz: int = len( str(abs(max(a))) )
        for i in range(1, max_raz + 1 ):
            lst: list[int] = [0] * base

            for j in range(len(a)):
                d: int = digit(a[j], i)
                lst[d] += 1

            count: int = 0
            for j in range(base):
                tmp: int = lst[j]
                lst[j] = count
                count += tmp
            for j in range(len(a)):
                d = digit(a[j], i)
                pre_result[lst[d]] = a[j]
                lst[d] += 1
            a = pre_result.copy()

        return a

    def bucket_sort(self, a:list[float], buckets: int|None) -> list[float]:
        if len(a) < 2:
            return a
        maxi = max(a)
        mini = min(a)
        if mini == maxi:
            return a
        num_buckets: int = buckets if buckets is not None else len(a)
        bucket: list[list[float]] = [[] for _ in range(num_buckets)]
        rang = maxi - mini
        for i in range(len(a)):
            index = int((a[i] - mini) * num_buckets / rang)
            if index == num_buckets:
                index -= 1
            bucket[index].append(a[i])

        for i in range(num_buckets):
            if len(bucket[i]) > 1:
                bucket[i]= self.bucket_sort(bucket[i], buckets)

        result: list[float] = []
        for i in range(num_buckets):
            result.extend(bucket[i])

        return result
