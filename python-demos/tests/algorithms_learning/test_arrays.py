import copy

import pytest

import algorithms_learning.arrays as arrays

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
    assert expected == arrays.binary_search(nums, target)


test_data2 = [
    # regular cases
    (0, [1, 2, 3], 1, 0, 2),
    # edge cases
    (-1, [1, 2, 3], 1, 1, 2),
    (-1, [1, 2, 3], 1, 1, 1),
]


@pytest.mark.parametrize("expected, nums, target, left, right", test_data2)
def test_binary_search_with_left_right(expected, nums, target, left, right):
    assert expected == arrays.binary_search(nums, target, left, right)


test_data3 = [
    ([1, 2, 3], 1, -10, 2),
    ([1, 2, 3], 1, 0, 10),
]


@pytest.mark.parametrize("nums, target, left, right", test_data3)
# @pytest.mark.xfail(raises=IndexError)
def test_binary_search_with_error(nums, target, left, right):
    with pytest.raises(IndexError):
        arrays.binary_search(nums, target, left, right)


test_reverse_data = [
    # edge cases
    (None, None, 0, 0),
    ("abc", "abc", 0, 0),
    ([], [], 0, 0),
    ([1], [1], 0, 0),
    # normal cases
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], 0, 0),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], -1, -1),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], -1, None),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], -1, 6),
    ([2, 1, 3, 4, 5], [1, 2, 3, 4, 5], 0, 1),
    ([3, 2, 1, 4, 5], [1, 2, 3, 4, 5], 0, 2),
    ([4, 3, 2, 1, 5], [1, 2, 3, 4, 5], 0, 3),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], 0, 4),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], 0, 5),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 1, 1),
    ([1, 3, 2, 4, 5], [1, 2, 3, 4, 5], 1, 2),
    ([1, 4, 3, 2, 5], [1, 2, 3, 4, 5], 1, 3),
    ([1, 5, 4, 3, 2], [1, 2, 3, 4, 5], 1, 4),
]


@pytest.mark.parametrize("expected, nums, p1, p2", copy.deepcopy(test_reverse_data))
def test_reverse(expected, nums, p1, p2):
    arrays.reverse(nums, p1, p2)
    assert expected == nums


test_sort_data = [
    # edge cases
    (None, None),
    ([], []),
    ("dde", "dde"),
    # normal cases
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]),
    ([1, 2, 3, 4, 5], [3, 4, 5, 2, 1]),
    ([1, 2, 3, 4, 5], [2, 3, 4, 5, 1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
]


@pytest.mark.parametrize("expected, nums", copy.deepcopy(test_sort_data))
def test_bubble_sort(expected, nums):
    assert expected == arrays.bubble_sort(nums)


@pytest.mark.parametrize("expected, nums", copy.deepcopy(test_sort_data))
def test_insertion_sort(expected, nums):
    assert expected == arrays.insertion_sort(nums)


@pytest.mark.parametrize("expected, nums", copy.deepcopy(test_sort_data))
def test_selection_sort(expected, nums):
    assert expected == arrays.selection_sort(nums)
