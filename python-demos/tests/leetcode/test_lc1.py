import pytest

from leetcode.lc1 import Solution


class TestSolution:
    test_data = [
        # edge cases
        (None, None, None),
        (None, "SSS", None),
        (None, [], None),
        (None, [1], None),
        (None, list(range(10**4 + 1)), None),
        (None, [3, 3], None),
        (None, [3, 3], "SSS"),
        (None, [3, 3], -(10**9) - 1),
        (None, [3, 3], 10**9 + 1),
        (None, [3, 3.3], 6),
        (None, [-(10**9) - 1, 3], 6),
        (None, [1, 10**9 + 1], 6),
        # normal cases
        ([0, 1], [2, 7, 11, 15], 9),
        ([1, 2], [3, 2, 4], 6),
        ([0, 1], [3, 3], 6),
    ]

    @pytest.mark.parametrize("expected, nums, target", test_data)
    def test_addSum(self, expected, nums, target):
        assert Solution().twoSum(nums, target) == expected
        assert Solution().twoSum2(nums, target) == expected
