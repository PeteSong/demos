from demos.func_demo import trace


@trace
def fibonacci(n):
    """return the n-th Fibonacci number"""
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@trace
def fibonacci_list(n):
    """return the first n Fibonacci numbers"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list


def main() -> None:  # pragma: no cover
    # print(fibonacci(0))
    # print(fibonacci(1))
    # print(fibonacci(2))
    # print(fibonacci(3))
    # print(fibonacci(4))
    # print(fibonacci(5))

    print(fibonacci_list(5))


if __name__ == "__main__":
    main()
