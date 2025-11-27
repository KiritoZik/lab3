import pytest
from src.services.stack import StackService
from src.services.queue import QueueService
from src.services.factorial import FactorialService
from src.services.fibonacci import FibonacciService
from src.services.sort_with_str import SortWithStrService
from src.services.sort_without_str import SortWithoutStrService


class TestStackService:
    def test_push_pop(self):
        stack = StackService()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1

    def test_peek(self):
        stack = StackService()
        stack.push(10)
        assert stack.peek() == 10
        assert len(stack) == 1

    def test_is_empty(self):
        stack = StackService()
        assert stack.is_empty() is True
        stack.push(1)
        assert stack.is_empty() is False

    def test_min(self):
        stack = StackService()
        stack.push(5)
        stack.push(2)
        stack.push(8)
        stack.push(1)
        assert stack.min() == 1
        stack.pop()
        assert stack.min() == 2
        stack.pop()
        assert stack.min() == 2

    def test_empty_stack_errors(self):
        stack = StackService()
        with pytest.raises(IndexError):
            stack.pop()
        with pytest.raises(IndexError):
            stack.peek()
        with pytest.raises(IndexError):
            stack.min()


class TestQueueService:
    def test_enqueue_dequeue(self):
        queue = QueueService()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3

    def test_front(self):
        queue = QueueService()
        queue.enqueue(10)
        assert queue.front() == 10
        assert len(queue) == 1

    def test_is_empty(self):
        queue = QueueService()
        assert queue.is_empty() is True
        queue.enqueue(1)
        assert queue.is_empty() is False

    def test_empty_queue_errors(self):
        queue = QueueService()
        with pytest.raises(IndexError):
            queue.dequeue()
        with pytest.raises(IndexError):
            queue.front()


class TestFactorialService:
    def test_factorial_iterative(self):
        service = FactorialService()
        assert service.factorial(0, False) == 1
        assert service.factorial(1, False) == 1
        assert service.factorial(5, False) == 120
        assert service.factorial(10, False) == 3628800

    def test_factorial_recursive(self):
        service = FactorialService()
        assert service.factorial(0, True) == 1
        assert service.factorial(1, True) == 1
        assert service.factorial(5, True) == 120
        assert service.factorial(10, True) == 3628800

    def test_factorial_negative(self):
        service = FactorialService()
        with pytest.raises(ValueError):
            service.factorial(-1, False)


class TestFibonacciService:
    def test_fibonacci_iterative(self):
        service = FibonacciService()
        assert service.fibonacci(0, False) == 0
        assert service.fibonacci(1, False) == 1
        assert service.fibonacci(2, False) == 1
        assert service.fibonacci(5, False) == 5
        assert service.fibonacci(10, False) == 55

    def test_fibonacci_recursive(self):
        service = FibonacciService()
        assert service.fibonacci(0, True) == 0
        assert service.fibonacci(1, True) == 1
        assert service.fibonacci(2, True) == 1
        assert service.fibonacci(5, True) == 5
        assert service.fibonacci(10, True) == 55

    def test_fibonacci_negative(self):
        service = FibonacciService()
        with pytest.raises(ValueError):
            service.fibonacci(-1, False)


class TestSortWithStrService:
    def test_bubble_sort(self):
        service = SortWithStrService()
        assert service.bubble_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
        assert service.bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert service.bubble_sort([1]) == [1]
        assert service.bubble_sort([]) == []

    def test_bubble_sort_strings(self):
        service = SortWithStrService()
        assert service.bubble_sort(['banana', 'apple', 'cherry']) == ['apple', 'banana', 'cherry']
        assert service.bubble_sort(['zebra', 'apple', 'banana']) == ['apple', 'banana', 'zebra']
        assert service.bubble_sort(['dog', 'cat', 'bird']) == ['bird', 'cat', 'dog']

    def test_quick_sort(self):
        service = SortWithStrService()
        assert service.quick_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
        assert service.quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert service.quick_sort([1]) == [1]
        assert service.quick_sort([]) == []

    def test_quick_sort_strings(self):
        service = SortWithStrService()
        assert service.quick_sort(['banana', 'apple', 'cherry']) == ['apple', 'banana', 'cherry']
        assert service.quick_sort(['zebra', 'apple', 'banana']) == ['apple', 'banana', 'zebra']
        assert service.quick_sort(['dog', 'cat', 'bird']) == ['bird', 'cat', 'dog']

    def test_heap_sort(self):
        service = SortWithStrService()
        assert service.heap_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
        assert service.heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert service.heap_sort([1]) == [1]
        assert service.heap_sort([]) == []

    def test_heap_sort_strings(self):
        service = SortWithStrService()
        assert service.heap_sort(['banana', 'apple', 'cherry']) == ['apple', 'banana', 'cherry']
        assert service.heap_sort(['zebra', 'apple', 'banana']) == ['apple', 'banana', 'zebra']
        assert service.heap_sort(['dog', 'cat', 'bird']) == ['bird', 'cat', 'dog']


class TestSortWithoutStrService:
    def test_counting_sort(self):
        service = SortWithoutStrService()
        assert service.counting_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
        assert service.counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert service.counting_sort([1]) == [1]
        assert service.counting_sort([]) == []

    def test_radix_sort(self):
        service = SortWithoutStrService()
        assert service.radix_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
        assert service.radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert service.radix_sort([1]) == [1]
        assert service.radix_sort([]) == []
        assert service.radix_sort([170, 45, 75, 90, 2, 802, 24, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]

    def test_bucket_sort(self):
        service = SortWithoutStrService()
        result = service.bucket_sort([0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51], None)
        assert result == [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]
        assert service.bucket_sort([0.5], None) == [0.5]
        assert service.bucket_sort([], None) == []
