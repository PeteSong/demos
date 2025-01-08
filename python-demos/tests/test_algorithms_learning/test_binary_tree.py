import pytest

import algorithms_learning.binary_tree as bs

test_data_edge_1 = [
    (None, None),
    (None, []),
]
test_data_edge_2 = [
    ([4, 2, None], [4, 2, None, None, None, None, None, None]),
]
test_data_normal = [
    ([4], [4]),
    ([4, 2, None], [4, 2, None]),
    ([4, None, 6], [4, None, 6]),
    ([4, 4, 6], [4, 4, 6]),
    ([4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
    ([4, 2, 6, 1, None, 5, None], [4, 2, 6, 1, None, 5, None]),
    ([4, 2, 6, None, 3, None, 7], [4, 2, 6, None, 3, None, 7]),
    ([4, 2, 6, 1, None, None, None], [4, 2, 6, 1, None, None, None]),
    ([4, 2, 6, None, 3, None, None], [4, 2, 6, None, 3, None, None]),
    ([4, 2, 6, None, None, 5, None], [4, 2, 6, None, None, 5, None]),
    ([4, 2, 6, None, None, None, 7], [4, 2, 6, None, None, None, 7]),
]


@pytest.mark.parametrize("expected, a", test_data_normal)
def test_binary_tree(expected, a: list):
    root = bs.array_to_tree(a)
    bs.print_tree(root)
    result = bs.tree_to_array(root)
    print(result)
    # assert a1 == a
    assert bs.arrays_equal(expected, result)


@pytest.mark.parametrize("expected, a", test_data_edge_1)
def test_array_to_tree_edge_cases_1(expected, a: list):
    r = bs.array_to_tree(a)
    assert expected == r


@pytest.mark.parametrize("expected, a", test_data_edge_2)
def test_array_to_tree_edge_cases_2(expected, a: list):
    r = bs.tree_to_array(bs.array_to_tree(a))
    assert bs.arrays_equal(expected, r)
    r = bs.tree_to_array(bs.array_to_tree(a), True)
    assert bs.arrays_equal(expected, r)


def test_tree_to_array():
    r = bs.tree_to_array(None)
    assert r is None


def test_same_arrays():
    r = bs.arrays_equal(None, [])
    assert not r
    r = bs.arrays_equal([], None)
    assert not r
    r = bs.arrays_equal([], [])
    assert r
    r = bs.arrays_equal(None, None)
    assert r


test_symmetric_tree_data = [
    # edge cases
    (True, None),
    (True, []),
    # regular cases
    (True, [1, 2, 2, 3, 4, 4, 3]),
    (False, [1, 2, 1, 3, 4, 4, 3]),
    (False, [1, 2, 2, None, 3, None, 3]),
]


@pytest.mark.parametrize("expected, a", test_symmetric_tree_data)
def test_symmetric_tree(expected, a: list):
    actual_result = bs.symmetric_tree(bs.array_to_tree(a))
    assert expected == actual_result
    actual_result = bs.symmetric_tree2(bs.array_to_tree(a))
    assert expected == actual_result
