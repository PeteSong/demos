import pytest

from algorithms_learning.binary_tree import array_to_tree
from leetcode.lc101 import Solution


class TestSolution:
    test_data = [
        # edge cases
        (True, None),
        (True, []),
        # regular cases
        (True, [1, 2, 2, 3, 4, 4, 3]),
        (False, [1, 2, 1, 3, 4, 4, 3]),
        (False, [1, 2, 2, None, 3, None, 3]),
    ]

    @pytest.mark.parametrize("expected, a", test_data)
    def test_isSymmetric(self, expected, a):
        root = array_to_tree(a)
        assert Solution().isSymmetric(root) == expected

    @pytest.mark.parametrize("expected, a", test_data)
    def test_isSymmetric2(self, expected, a):
        root = array_to_tree(a)
        assert Solution().isSymmetric2(root) == expected
