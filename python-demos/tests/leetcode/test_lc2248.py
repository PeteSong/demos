from typing import Any

import pytest

from leetcode.lc2248 import Solution


class TestSolution:
    list_0_1001: list[int] = list(range(1002))
    list_0_500: list[int] = list(range(501))
    list_0_499: list[int] = list(range(500))
    invalid_test_data = [
        (None, []),
        ([], []),
        ([[]], []),
        ([None], []),
        ([[1], None], []),
        ([list_0_1001], []),
        ([["a", 1], [1]], []),
        ([[0, 1], [1]], []),
        ([[1], ["a", 1]], []),
        ([[1], [0, 1]], []),
        ([[1, 1, 2, 3], [1, 2, 3]], []),
        # Test total length > 1000
        ([list_0_500, list_0_499], []),
    ]

    valid_test_data = [
        ([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]], [3, 4]),
        ([[1, 2, 3], [2, 3], [3]], [3]),
        ([[1, 2, 3], [4, 5, 6]], []),
        ([[1]], [1]),
        ([[1], [1]], [1]),
        ([[1, 2], [2, 1]], [1, 2]),
    ]

    @pytest.mark.parametrize("nums, expected", invalid_test_data + valid_test_data)
    def test_intersection(self, nums: Any, expected: list[int]) -> None:
        assert Solution().intersection(nums) == expected

    @pytest.mark.parametrize("nums, expected", invalid_test_data + valid_test_data)
    def test_intersection2(self, nums: Any, expected: list[int]) -> None:
        assert Solution().intersection2(nums) == expected

    @pytest.mark.parametrize("nums, expected", invalid_test_data + valid_test_data)
    def test_intersection3(self, nums: Any, expected: list[int]) -> None:
        assert Solution().intersection3(nums) == expected

    @pytest.mark.parametrize("nums, expected", invalid_test_data + valid_test_data)
    def test_intersection4(self, nums: Any, expected: list[int]) -> None:
        assert Solution().intersection4(nums) == expected
