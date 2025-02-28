import pytest

from algorithms_learning.prime_numbers import is_prime, prime_numbers


def test_prime_number():
    assert is_prime(7) is True


def test_non_prime_number():
    assert is_prime(4) is False


def test_one_is_not_prime():
    assert is_prime(1) is False


def test_zero_is_not_prime():
    assert is_prime(0) is False


def test_negative_number_is_not_prime():
    assert is_prime(-5) is False


def test_large_prime_number():
    assert is_prime(7919) is True


def test_large_non_prime_number():
    assert is_prime(8000) is False


def test_prime_numbers():
    with pytest.raises(ValueError):
        prime_numbers(0)
    assert prime_numbers(10) == [2, 3, 5, 7]
