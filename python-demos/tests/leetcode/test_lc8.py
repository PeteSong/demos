import pytest

from leetcode.lc8 import Solution


class TestSolution:
    invalid_test_data = [(None), (8.8)]
    test_data = [
        (0, ""),
        (0, "  "),
        (0, "  -0"),
        (0, "  +0"),
        (0, "  +a053"),
        (0, "  +a053"),
        (2147483647, "21474836488"),
        (-2147483648, "-21474836488"),
        (53, "  +053"),
        (-53, "  -053"),
    ]

    @pytest.mark.parametrize("s", invalid_test_data)
    def test_invalid(self, s):
        with pytest.raises(ValueError):
            Solution().myAtoi(s)

    @pytest.mark.parametrize("expected, s", test_data)
    def test_lengthOfLongestSubstring(self, expected, s):
        assert Solution().myAtoi(s) == expected
