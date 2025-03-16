import pytest

from leetcode.lc412 import Solution


class TestSolution:
    test_data = [
        (None, []),
        (1.2, []),
        ("", []),
        (0, []),
        (1, ["1"]),
        (3, ["1", "2", Solution.FIZZ]),
        (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]),
    ]

    @pytest.mark.parametrize("n,expected", test_data)
    def test_fizzBuzz(self, n, expected):
        assert Solution().fizzBuzz(n) == expected
