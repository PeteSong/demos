import copy

import pytest

from leetcode_solutions.lc80 import Solution


class TestSolution:
    test_data = [
        # edge cases
        (None, -1),
        ("string", -1),
        ([], -1),
        ([1], 1),
        ([1, 2], 2),
        # regular cases
        ([1, 1, 1, 2, 2, 3], 5),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7),
        ([4, 4, 4, 4, 4, 4, 4, 4], 2),
    ]

    @pytest.mark.parametrize("nums,expected", copy.deepcopy(test_data))
    def test_removeDuplicate(self, nums, expected):
        assert Solution().removeDuplicates(nums) == expected

    @pytest.mark.parametrize("nums,expected", copy.deepcopy(test_data))
    def test_removeDuplicate2(self, nums, expected):
        assert Solution().removeDuplicates2(nums) == expected
