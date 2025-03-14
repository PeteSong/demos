import functools

from demos.func_demo import trace


@trace
@functools.lru_cache
def fibonacci_in_recursion(nth):
    """return the n-th(from 1st) Fibonacci number
    F(1) = 1, F(2) = 1
    F(n) = F(n-1) + F(n-2)
    """
    if nth <= 0:
        raise ValueError("n must be greater than 0")
    if nth in [1, 2]:
        return 1
    return fibonacci_in_recursion(nth - 1) + fibonacci_in_recursion(nth - 2)


@trace
def fibonacci(nth):
    """return the n-th(from 1st) Fibonacci number
    F(1) = 1, F(2) = 1
    F(n) = F(n-1) + F(n-2)
    """
    if nth <= 0:
        raise ValueError("n must be greater than 0")
    n1, n2 = 1, 1
    for _ in range(nth - 1):
        n1, n2 = n2, n1 + n2
    return n1


@trace
def fibonacci_generator(stop_n=None):
    """return the n-th(from 1st) Fibonacci number
    F(1) = 1, F(2) = 1
    F(n) = F(n-1) + F(n-2)
    """
    if stop_n is not None and stop_n <= 0:
        raise ValueError("stop n must be greater than 0")
    n1, n2 = 1, 1
    i = 0
    while True:
        if stop_n is not None:
            if i >= stop_n:
                break
            else:
                i += 1
        yield n1
        n1, n2 = n2, n1 + n2


@trace
def fibonacci_list(n):
    """return the first n Fibonacci numbers"""
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return [1]
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[1:]


def main() -> None:  # pragma: no cover
    # print(fibonacci(0))
    # print(fibonacci(1))
    # print(fibonacci(2))
    # print(fibonacci(3))
    # print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci_in_recursion(5))

    print(fibonacci_list(5))

    for v in fibonacci_generator(5):
        print(f"{v}", end=" ")
    print(list(fibonacci_generator(5)))
    # for i, v in enumerate(fibonacci_generator(5)):
    # print(f'{i}: {v}', end=' ')


if __name__ == "__main__":
    main()
