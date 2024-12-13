import pytest

from leetcode_solutions.lc2235 import Solution


class TestSolution:
    test_data = [
        (0, 0, 0),
        (0.1, 1, 0),
        (1, 1.1, 0),
        (1, 2, 3),
        (-9, 9, 0),
        (9, 9, 18),
        (-9, -9, -18),
    ]

    @pytest.mark.parametrize("num1,num2,expected", test_data)
    def test_maximumWealth(self, num1, num2, expected):
        assert Solution().sum(num1, num2) == expected
