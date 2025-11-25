from src.services.Base import sortWithStrServiceBase

class SortWithStrService(sortWithStrServiceBase):
    def bubble_sort(self, a:list[int]) -> list[int]:
        i = 0
        t = True
        while t:
            t = False
            for j in range(len(a)-i-1):
                if a[j] > a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]
                    t = True
            i = i+1

        return a

    def quick_sort(self, a:list[int]) -> list[int]:
        if len(a) < 2:
            return a  # базовый случай

        pivot = a[len(a) // 2]  # выбираем средний элемент
        left = [x for x in a if x < pivot]
        middle = [x for x in a if x == pivot]
        right = [x for x in a if x > pivot]

        return self.quick_sort(left) + middle + self.quick_sort(right)

    def heap_sort(self, a:list[int]) -> list[int]:
        n = len(a)

        def sift_down(start: int, heap_size: int):
            while 2 * start + 1 < heap_size:
                left = 2 * start + 1
                right = 2 * start + 2
                j = left
                if right < heap_size and a[right] > a[left]:
                    j = right
                if a[start] >= a[j]:
                    break
                a[start], a[j] = a[j], a[start]
                start = j

        for i in range(n // 2 - 1, -1, -1):
            sift_down(i, n)

        for i in range(n - 1, 0, -1):
            a[0], a[i] = a[i], a[0]
            sift_down(0, i)

        return a

