import pytest

from leetcode.lc7 import Solution


class TestSolution:
    invalid_test_data = [(None), ("SSS"), (2**31), (-(2**31) - 1)]
    test_data = [
        (1, 1),
        (0, 0),
        (12, 21),
        (-21, -12),
        (12, 210),
        (-12, -210),
        (-2143847412, -2147483412),
        (0, 2009999999),
        # (0, -9463847412),
    ]

    @pytest.mark.parametrize("x", invalid_test_data)
    def test_invalid(self, x):
        with pytest.raises(ValueError):
            Solution().reverse(x)
        with pytest.raises(ValueError):
            Solution().reverse2(x)
        with pytest.raises(ValueError):
            Solution().reverse3(x)

    @pytest.mark.parametrize("expected, x", test_data)
    def test_reverse(self, expected, x):
        assert Solution().reverse(x) == expected
        assert Solution().reverse2(x) == expected
        assert Solution().reverse3(x) == expected
