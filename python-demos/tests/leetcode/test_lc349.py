import pytest

from leetcode.lc349 import Solution


class TestSolution:
    list_0_1001 = list(range(1002))
    invalid_test_data = [
        (None, None, []),
        ([], None, []),
        ([1], None, []),
        ([1], [], []),
        (list_0_1001, [1], []),
        ([1], list_0_1001, []),
        (["a", 1, 2], [1], []),
        ([1, 2, 0], [1], []),
        ([1], ["a", 1, 2], []),
        ([1], [1, 2, 0], []),
    ]
    valid_test_data = [
        ([1, 2, 2, 1], [2, 2], [2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]),
    ]

    @pytest.mark.parametrize("nums1, nums2, expected", invalid_test_data + valid_test_data)
    def test_intersection(self, nums1, nums2, expected):
        assert sorted(Solution().intersection(nums1, nums2)) == sorted(expected)

    @pytest.mark.parametrize("nums1, nums2, expected", invalid_test_data + valid_test_data)
    def test_intersection2(self, nums1, nums2, expected):
        assert sorted(Solution().intersection2(nums1, nums2)) == sorted(expected)
