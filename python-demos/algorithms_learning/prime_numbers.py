import concurrent.futures as cf
import functools
import math
from collections.abc import Iterator

from demos.func_demo import ptimeit

_SMALL_PRIME_NUMBERS = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]
_STARTING_NUMBER = _SMALL_PRIME_NUMBERS[-1] + 2


def _small_primes(n: int) -> list[int]:
    if n <= 1:
        raise ValueError("n must be greater than 1")

    return [x for x in _SMALL_PRIME_NUMBERS if x <= n]


@functools.lru_cache
def is_prime(n: int) -> bool:
    if n <= 1:
        raise ValueError("n must be greater than 1")
    if n in _SMALL_PRIME_NUMBERS:
        return True
    if any(n % x == 0 for x in _SMALL_PRIME_NUMBERS):
        return False
    k = int(math.floor(math.sqrt(n))) + 1
    for x in range(_STARTING_NUMBER, k, 2):
        if n % x == 0:
            return False
    return True


def prime_generator(n: int) -> Iterator[int]:
    if n <= 1:
        raise ValueError("n must be greater than 1")
    yield from _small_primes(n)
    for i in range(_STARTING_NUMBER, n + 1, 2):
        if is_prime(i):
            yield i


@ptimeit
def prime_numbers(n: int) -> list[int]:
    prime_nums = _small_primes(n)
    for i in range(_STARTING_NUMBER, n + 1, 2):
        if is_prime(i):
            prime_nums.append(i)
    return prime_nums


@ptimeit
def prime_numbers_in_parallel(n: int) -> list[int]:
    if n <= 1:
        raise ValueError("n must be greater than 1")

    prime_nums = _small_primes(n)

    futures = {}
    with cf.ProcessPoolExecutor(10) as executor:
        for i in range(_STARTING_NUMBER, n + 1, 2):
            future = executor.submit(is_prime, i)
            futures[future] = i
    for future in cf.as_completed(futures):
        if future.result():
            prime_nums.append(futures[future])
    return prime_nums


def main() -> None:  # pragma: no cover
    prime_numbers(100)
    prime_numbers(1000)
    prime_numbers(10000)
    # prime_numbers(10 ** 6)
    # prime_numbers_in_parallel(10 ** 6)
    g = prime_generator(1)
    next(g)
    g = prime_generator(100)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    for i in g:
        print(i)


if __name__ == "__main__":
    main()
