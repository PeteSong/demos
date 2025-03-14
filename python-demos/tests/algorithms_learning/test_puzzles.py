import pytest

from algorithms_learning.puzzles import fibonacci, fibonacci_generator, fibonacci_in_recursion, fibonacci_list


@pytest.mark.parametrize("n, expected", [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5)])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


@pytest.mark.parametrize("n, expected", [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5)])
def test_fibonacci_in_recursion(n, expected):
    assert fibonacci_in_recursion(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(1, [1]), (2, [1, 1]), (3, [1, 1, 2]), (4, [1, 1, 2, 3]), (5, [1, 1, 2, 3, 5])],
)
def test_fibonacci_list(n, expected):
    assert fibonacci_list(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [(1, [1]), (2, [1, 1]), (3, [1, 1, 2]), (4, [1, 1, 2, 3]), (5, [1, 1, 2, 3, 5])],
)
def test_fibonacci_generator_with_stop_n(n, expected):
    assert list(fibonacci_generator(5)) == [1, 1, 2, 3, 5]


def test_fibonacci_generator():
    gen = fibonacci_generator()
    assert next(gen) == 1
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 5
    gen.close()


def test_fibonacci_list_negative():
    with pytest.raises(ValueError):
        fibonacci_list(-1)
    with pytest.raises(ValueError):
        fibonacci_list(0)
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci(0)
    with pytest.raises(ValueError):
        fibonacci_in_recursion(-1)
    with pytest.raises(ValueError):
        fibonacci_in_recursion(0)
    with pytest.raises(ValueError):
        next(fibonacci_generator(-1))
    with pytest.raises(ValueError):
        next(fibonacci_generator(0))
