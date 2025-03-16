import pytest

from leetcode.lc219 import Solution


class TestSolution:
    test_data_edge = [
        (False, None, 1),
        (False, [], 0),
        (False, "abc", 1),
        (False, [], 1),
        (False, [1], 1),
        (False, [1, 2], 1),
    ]
    test_data = [
        # regular cases
        (False, [1, 2, 3, 4, 5], 1),
        (False, [1, 2, 3, 4, 5], 2),
        (False, [1, 2, 3, 4, 5], 3),
        (False, [1, 2, 3, 4, 5], 4),
        (False, [1, 2, 3, 4, 5], 5),
        (False, [1, 2, 3, 4, 5], 6),
        (True, [1, 1, 2, 3, 4], 1),
        (True, [2, 3, 4, 1, 1], 1),
        (True, [1, 1, 2, 3, 4], 2),
        (True, [2, 3, 4, 1, 1], 2),
        (False, [1, 2, 1, 3, 4], 1),
        (True, [1, 2, 1, 3, 4], 2),
        (False, [1, 2, 3, 1, 4], 2),
        (True, [1, 2, 3, 1, 4], 3),
        (False, [1, 2, 3, 4, 1], 3),
        (True, [1, 2, 3, 4, 1], 4),
        (True, [1, 2, 3, 4, 1], 5),
    ]

    @pytest.mark.parametrize("expected, nums, k", test_data_edge + test_data)
    def test_containsNearbyDuplicate(self, expected, nums, k):
        assert expected == Solution().containsNearbyDuplicate(nums, k)
        assert expected == Solution().containsNearbyDuplicate2(nums, k)
