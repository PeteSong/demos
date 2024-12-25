import pytest

from leetcode_solutions.lc33 import Solution


class TestSolution:
    test_data = [
        # edge cases
        (None, 0, -1),
        ("string", 0, -1),
        ([], 0, -1),
        ([1], 1.5, -1),
        ([4, 5, 6, 7, 0, 1, 2, 3], 101, -1),
        # regular cases
        ([4, 5, 6, 7, 0, 1, 2, 3], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2, 3], 1, 5),
        ([4, 5, 6, 7, 0, 1, 2, 3], 2, 6),
        ([4, 5, 6, 7, 0, 1, 2, 3], 3, 7),
        ([4, 5, 6, 7, 0, 1, 2, 3], 7, 3),
        ([4, 5, 6, 7, 0, 1, 2, 3], 6, 2),
        ([4, 5, 6, 7, 0, 1, 2, 3], 5, 1),
        ([4, 5, 6, 7, 0, 1, 2, 3], 4, 0),
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 1, 5),
        ([4, 5, 6, 7, 0, 1, 2], 2, 6),
        ([4, 5, 6, 7, 0, 1, 2], 7, 3),
        ([4, 5, 6, 7, 0, 1, 2], 6, 2),
        ([4, 5, 6, 7, 0, 1, 2], 5, 1),
        ([4, 5, 6, 7, 0, 1, 2], 4, 0),
        ([5, 6, 7, 0, 1, 2, 3], 0, 3),
        ([5, 6, 7, 0, 1, 2, 3], 1, 4),
        ([5, 6, 7, 0, 1, 2, 3], 2, 5),
        ([5, 6, 7, 0, 1, 2, 3], 3, 6),
        ([5, 6, 7, 0, 1, 2, 3], 7, 2),
        ([5, 6, 7, 0, 1, 2, 3], 6, 1),
        ([5, 6, 7, 0, 1, 2, 3], 5, 0),
    ]

    @pytest.mark.parametrize("nums,target,expected", test_data)
    def test_search(self, nums, target, expected):
        assert Solution().search(nums, target) == expected

    @pytest.mark.parametrize("nums,target,expected", test_data)
    def test_search2(self, nums, target, expected):
        assert Solution().search2(nums, target) == expected
