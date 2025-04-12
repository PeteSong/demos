import pytest

from leetcode.lc347 import Solution


class TestSolution:
    list_0_100001 = list(range(10**5 + 1))
    invalid_test_data = [
        (None, None),
        ("SSS", None),
        ([], None),
        (list_0_100001, None),
        ([1, 1, 2, 2, 3], None),
        ([1, 1, 2, 2, 3], "SSS"),
        ([1, 1, 2, 2, 3], 0),
        ([1, 1, 2, 2, 3], 5),
        ([1, "1", "2", 2, 3], 2),
        ([10**4 + 1, 1, 2, 2, 3], 2),
        ([-(10**4) - 1, 2, 2, 3, 3, 1], 2),
    ]
    valid_test_data = [([1, 2], [1, 1, 1, 2, 2, 3], 2), ([1], [1, 1, 1, 2, 2, 3], 1), ([1], [1], 1)]

    @pytest.mark.parametrize("nums, k", invalid_test_data)
    def test_invalid_input(self, nums, k):
        with pytest.raises(ValueError):
            Solution().topKFrequent(nums, k)

    @pytest.mark.parametrize("expected, nums, k", valid_test_data)
    def test_topKFrequent(self, expected, nums, k):
        assert sorted(Solution().topKFrequent(nums, k)) == sorted(expected)
