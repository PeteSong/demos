import pytest

from leetcode.lc283 import Solution


class TestSolution:
    test_invalid_data = [
        (None),
        (dict()),
        ("SSS"),
        ([]),
        (list(range(10**4 + 1))),
        (["a", "b"]),
        ([-0.1, 1.1]),
        ([2**31]),
        ([-(2**31) - 1]),
    ]
    test_data = [
        # regular cases
        ([1, 3, 12, 0, 0], [0, 1, 0, 3, 12]),
        ([0], [0]),
        ([1], [1]),
        ([1, 0], [1, 0]),
        ([1, 0], [0, 1]),
        ([1, 0, 0], [0, 1, 0]),
    ]

    test_data2 = [
        # regular cases
        ([0, 0, 1, 3, 12], [0, 1, 0, 3, 12]),
        ([0], [0]),
        ([1], [1]),
        ([0, 1], [1, 0]),
        ([0, 1], [0, 1]),
        ([0, 0, 1], [0, 1, 0]),
    ]

    @pytest.mark.parametrize("nums", test_invalid_data)
    def test_edge_cases(self, nums):
        with pytest.raises(ValueError):
            Solution().moveZeroes(nums)
        with pytest.raises(ValueError):
            Solution().move_zeros_to_head(nums)
        with pytest.raises(ValueError):
            Solution().moveZeroes2(nums)

    @pytest.mark.parametrize("expected, nums", test_data)
    def test_moveZeros(self, expected, nums):
        nums_copy = nums.copy()
        Solution().moveZeroes(nums_copy)
        assert expected == nums_copy

        nums_copy = nums.copy()
        Solution().moveZeroes2(nums_copy)
        assert expected == nums_copy

    @pytest.mark.parametrize("expected, nums", test_data2)
    def test_move_zeros_to_head(self, expected, nums):
        nums_copy = nums.copy()
        Solution().move_zeros_to_head(nums_copy)
        assert expected == nums_copy
