import pytest

from leetcode.lc123 import Solution


class TestSolution:
    test_data = [
        # edge cases
        (0, None),
        (0, "aabc"),
        (0, []),
        # regular cases
        (7, [7, 1, 5, 3, 6, 4]),
        (6, [3, 3, 5, 0, 0, 3, 1, 4]),
        (4, [1, 2, 3, 4, 5]),
        (0, [7, 6, 4, 3, 1]),
    ]

    @pytest.mark.parametrize("expected, prices", test_data)
    def test_maxProfit(self, expected, prices):
        assert expected == Solution().maxProfit(prices)
        assert expected == Solution().maxProfit2(prices)
