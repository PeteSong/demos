import pytest

from algorithms_learning.arrays import binary_search

test_data = [
    # edge cases
    (-1, None, 0),
    (-1, [], 0),
    (-1, [1], 0),
    # regular cases
    (0, [1], 1),
    (0, [1, 2], 1),
    (1, [1, 2], 2),
    (-1, [1, 2], 3),
]


@pytest.mark.parametrize("expected, nums, target", test_data)
def test_binary_search(expected, nums, target):
    assert expected == binary_search(nums, target)


test_data2 = [
    # regular cases
    (0, [1, 2, 3], 1, 0, 2),
    # edge cases
    (-1, [1, 2, 3], 1, 1, 2),
    (-1, [1, 2, 3], 1, 1, 1),
]


@pytest.mark.parametrize("expected, nums, target, left, right", test_data2)
def test_binary_search_with_left_right(expected, nums, target, left, right):
    assert expected == binary_search(nums, target, left, right)


test_data3 = [
    ([1, 2, 3], 1, -10, 2),
    ([1, 2, 3], 1, 0, 10),
]


@pytest.mark.parametrize("nums, target, left, right", test_data3)
# @pytest.mark.xfail(raises=IndexError)
def test_binary_search_with_error(nums, target, left, right):
    with pytest.raises(IndexError):
        binary_search(nums, target, left, right)
