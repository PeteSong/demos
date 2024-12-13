import pytest

from leetcode_solutions.lc1480 import Solution


class TestSolution:
    test_data = [
        (None, []),
        (1.2, []),
        ("", []),
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 3]),
        ([1, 2, 3, 4], [1, 3, 6, 10]),
    ]

    @pytest.mark.parametrize("nums,expected", test_data)
    def test_runningSum(self, nums, expected):
        assert Solution().runningSum(nums) == expected

    @pytest.mark.parametrize("nums,expected", test_data)
    def test_runningSum2(self, nums, expected):
        assert Solution().runningSum2(nums) == expected
