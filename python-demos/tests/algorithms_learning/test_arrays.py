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
    # edge cases
    (-1, [1, 2, 3], 1, 1, 2),
    (-1, [1, 2, 3], 1, 1, 1),
    # regular cases
    (0, [1, 2, 3], 1, 0, 2),
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


@pytest.mark.parametrize("expected, nums", copy.deepcopy(test_sort_data))
def test_quick_sort(expected, nums):
    assert expected == arrays.quick_sort(nums)


test_nested_list_invalid = [
    # edge cases
    (None),
    (dict()),
    (set()),
    ([dict()]),
    ([set()]),
    ([None]),
]

test_nested_list = [
    # expected, input
    ([3], 3),
    (["a"], "a"),
    ([5.5], 5.5),
    ([True], True),
    ([False], False),
    ([], []),
    ([1, 2, 3], [1, 2, 3]),
    ([1, "2", 3.3, False], [1, "2", 3.3, False]),
    ([1, True, 2, 3.3, "4", 5], [1, [True, 2], 3.3, ["4", 5]]),
    ([1, True, 1, 3.3, "4", 3.3], [1, [True, 1], 3.3, ["4", 3.3]]),
    ([1, 2, 3, 4, False, 5, True, 5.5, 6], [1, 2, 3, [[4, False], [5, True, 5.5]], [6]]),
]


@pytest.mark.parametrize("intput", test_nested_list_invalid)
def test_flatten_invalid(intput):
    with pytest.raises(ValueError):
        arrays.flatten_list_recurision(intput)
    with pytest.raises(ValueError):
        arrays.flatten_list(intput)
    with pytest.raises(ValueError):
        next(arrays.flatten_list_generator(input))


@pytest.mark.parametrize("expected, input", test_nested_list)
def test_flatten(expected, input):
    assert expected == arrays.flatten_list_recurision(input)
    assert expected == arrays.flatten_list(input)
    assert expected == list(arrays.flatten_list_generator(input))


@pytest.mark.parametrize(
    "matrix",
    [
        (None),
        ("SSS"),
        ([]),
        ([None, None]),
        (["None", "None"]),
        ([[], []]),
        ([[None, None], [None, None]]),
        ([["None", "None"], ["None", "None"]]),
    ],
)
def test_rotate90_with_invalid_matrix(matrix):
    with pytest.raises(ValueError):
        arrays.rotate90(matrix)


def test_rotate90():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_copy = copy.deepcopy(matrix)
    expected_roate90 = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    arrays.rotate90(matrix)
    assert expected_roate90 == matrix
    arrays.rotate90(matrix, False)
    assert matrix == matrix_copy
