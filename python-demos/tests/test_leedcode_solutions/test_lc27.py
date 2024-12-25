import pytest

from leetcode_solutions.lc27 import Solution


class TestSolution:
    test_data = [
        # edge cases
        (None, 0, 0),
        ([], 0, 0),
        ("string", 0, 0),
        ([1], -1, 0),
        ([1], 101, 0),
        # regular cases
        ([3, 2, 2, 3], 3, 2),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
        ([0, 1, 2, 2, 3, 0, 4, 2], 99, 8),
    ]

    @pytest.mark.parametrize("nums,val,expected", test_data)
    def test_removeElement(self, nums, val, expected):
        assert Solution().removeElement(nums, val) == expected
