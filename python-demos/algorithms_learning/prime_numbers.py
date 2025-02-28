import math

from demos.func_demo import ptimeit


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    k = int(math.sqrt(n)) + 1
    for x in range(2, k):
        if n % x == 0:
            return False
    return True


@ptimeit
def prime_numbers(n: int) -> list[int]:
    if n <= 1:
        raise ValueError("n must be greater than 1")
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def main() -> None:  # pragma: no cover
    print(prime_numbers(100))
    print(prime_numbers(1000))


if __name__ == "__main__":
    main()
