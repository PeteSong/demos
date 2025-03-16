import copy

import pytest

from leetcode.lc189 import Solution


class TestSolution:
    test_data_edge = [
        (None, None, 1),
        ([], [], 1),
        ("abc", "abc", 1),
        ([1, 2, 3], [1, 2, 3], 0),
        ([1, 2, 3], [1, 2, 3], -1),
    ]
    test_data = [
        # regular cases
        ([5, 1, 2, 3, 4], [1, 2, 3, 4, 5], 1),
        ([4, 5, 1, 2, 3], [1, 2, 3, 4, 5], 2),
        ([3, 4, 5, 1, 2], [1, 2, 3, 4, 5], 3),
        ([2, 3, 4, 5, 1], [1, 2, 3, 4, 5], 4),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5),
        ([5, 1, 2, 3, 4], [1, 2, 3, 4, 5], 6),
    ]

    @pytest.mark.parametrize("expected, nums, k", test_data_edge)
    def test_edge_cases(self, expected, nums, k):
        Solution().rotate(nums, k)
        assert expected == nums
        Solution().rotate2(nums, k)
        assert expected == nums
        Solution().rotate3(nums, k)
        assert expected == nums
        Solution().rotate4(nums, k)
        assert expected == nums

    @pytest.mark.parametrize("expected, nums, k", copy.deepcopy(test_data))
    def test_rotate_01(self, expected, nums, k):
        Solution().rotate(nums, k)
        assert expected == nums

    @pytest.mark.parametrize("expected, nums, k", copy.deepcopy(test_data))
    def test_rotate_02(self, expected, nums, k):
        Solution().rotate2(nums, k)
        assert expected == nums

    @pytest.mark.parametrize("expected, nums, k", copy.deepcopy(test_data))
    def test_rotate_03(self, expected, nums, k):
        Solution().rotate3(nums, k)
        assert expected == nums

    @pytest.mark.parametrize("expected, nums, k", copy.deepcopy(test_data))
    def test_rotate_04(self, expected, nums, k):
        Solution().rotate4(nums, k)
        assert expected == nums
