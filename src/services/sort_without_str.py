from src.services.Base import sortWithoutStrServiceBase

class SortWithoutStrService(sortWithoutStrServiceBase):
    def counting_sort(self, a:list[int]) -> list[int]:
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
            num = str(num)
            if len(num) < raz:
                return 0
            return int(num[-raz])
        pre_result: list[int] = [0] * len(a)
        max_raz: int = len( str(abs(max(a))) )
        for i in range(1, max_raz + 1 ):
            k: int = 10
            lst: list[int] = [0] * k

            for j in range(len(a)):
                d: int = digit(a[j], i)
                lst[d] += 1

            count: int = 0
            for j in range(k):
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
        maxi = max(a)
        mini = min(a)
        if len(a) < 2 or mini == maxi:
            return a
        num_buckets: int = buckets if buckets is not None else len(a)
        bucket: list[list[float]] = [[] for _ in range(num_buckets)]
        min_buckets: list[float|None] = [None] * num_buckets
        max_buckets: list[float|None] = [None] * num_buckets
        rang = maxi - mini
        for i in range(len(a)):
            index = int((a[i] - mini) * num_buckets / rang)
            if index == num_buckets:
                index -= 1
            bucket[index].append(a[i])
            if min_buckets[index] is None or a[i] < min_buckets[index]:
                min_buckets[index] = a[i]
            if max_buckets[index] is None or a[i] > max_buckets[index]:
                max_buckets[index] = a[i]


        for i in range(num_buckets):
            if len(bucket[i]) > 1:
                bucket[i]= self.bucket_sort(bucket[i], buckets)

        result: list[float] = []
        for i in range(num_buckets):
            result.extend(bucket[i])

        return result

