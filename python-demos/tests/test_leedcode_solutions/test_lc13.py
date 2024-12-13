import pytest

from leetcode_solutions.lc13 import Solution


class TestSolution:
    test_data = [(None, 0), (1, 0), ("", 0), ("abc", 0), ("MCMXCIV", 1994)]

    @pytest.mark.parametrize("s,expected", test_data)
    def test_romanToInt(self, s, expected):
        assert Solution().romanToInt(s) == expected

    @pytest.mark.parametrize("s,expected", test_data)
    def test_romanToInt2(self, s, expected):
        assert Solution().romanToInt2(s) == expected
