import pytest

from leetcode_solutions.lc121 import Solution


class TestSolution:
    test_data = [
        # edge cases
        (0, None),
        (0, "aabc"),
        (0, []),
        # regular cases
        (5, [7, 1, 5, 3, 6, 4]),
        (0, [7, 6, 4, 3, 1]),
    ]

    @pytest.mark.parametrize("expected, prices", test_data)
    def test_maxProfit(self, expected, prices):
        assert expected == Solution().maxProfit(prices)
