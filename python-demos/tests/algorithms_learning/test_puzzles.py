import pytest

from algorithms_learning.puzzles import fibonacci, fibonacci_list


@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5)])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


@pytest.mark.parametrize(
    "n, expected", [(0, []), (1, [0]), (2, [0, 1]), (3, [0, 1, 1]), (4, [0, 1, 1, 2]), (5, [0, 1, 1, 2, 3])]
)
def test_fibonacci_list(n, expected):
    assert fibonacci_list(n) == expected


def test_fibonacci_list_negative():
    with pytest.raises(ValueError):
        fibonacci_list(-1)
