import pytest

from algorithms_learning.prime_numbers import is_prime, prime_generator, prime_numbers, prime_numbers_in_parallel


def test_prime_number():
    assert is_prime(7) is True


def test_non_prime_number():
    assert is_prime(4) is False


def test_one_is_not_valid():
    with pytest.raises(ValueError):
        is_prime(1)


def test_negative_number_is_not_valid():
    with pytest.raises(ValueError):
        is_prime(-5)


def test_large_prime_number():
    assert is_prime(7919) is True


def test_large_non_prime_number():
    assert is_prime(81) is False
    assert is_prime(8000) is False


expected_primes_less_than_102 = [
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
    101,
]


def test_prime_numbers():
    with pytest.raises(ValueError):
        prime_numbers(0)
    assert prime_numbers(10) == [2, 3, 5, 7]
    assert prime_numbers(102) == expected_primes_less_than_102


def test_prime_generator():
    with pytest.raises(ValueError):
        next(prime_generator(1))
    assert list(prime_generator(102)) == expected_primes_less_than_102


def test_prime_numbers_in_parallel():
    with pytest.raises(ValueError):
        prime_numbers_in_parallel(0)
    assert prime_numbers_in_parallel(102) == expected_primes_less_than_102
