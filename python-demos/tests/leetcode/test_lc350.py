from typing import Any

import pytest

from leetcode.lc350 import Solution


class TestSolution:
    list_0_1001: list[int] = list(range(1002))
    invalid_test_data: list[tuple[Any, Any, list[int]]] = [
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
    valid_test_data: list[tuple[list[int], list[int], list[int]]] = [
        ([1, 2, 2, 1], [2, 2], [2, 2]),  # Multiple occurrences
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),  # Different order
        ([1, 1, 1], [1], [1]),  # Single match
        ([1], [1, 1, 1], [1]),  # Single match reverse
        ([1, 2, 3], [4, 5, 6], []),  # No intersection
        ([1, 1, 2, 2], [2, 2, 1, 1], [1, 1, 2, 2]),  # All elements match
    ]

    @pytest.mark.parametrize("nums1, nums2, expected", invalid_test_data + valid_test_data)
    def test_intersection(self, nums1: Any, nums2: Any, expected: list[int]) -> None:
        result = Solution().intersection(nums1, nums2)
        assert sorted(result) == sorted(expected)
