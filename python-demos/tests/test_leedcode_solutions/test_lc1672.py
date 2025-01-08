import pytest

from leetcode.lc1672 import Solution


class TestSolution:
    test_data = [
        (None, 0),
        (1.2, 0),
        ([], 0),
        ([1], 0),
        ([[]], 0),
        ([[10]], 10),
        ([[1, 5], [7, 3], [3, 5]], 10),
    ]

    @pytest.mark.parametrize("accounts,expected", test_data)
    def test_maximumWealth(self, accounts, expected):
        assert Solution().maximumWealth(accounts) == expected
