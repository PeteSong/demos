import pytest

from leetcode.lc66 import Solution


class TestSolution:
    test_data = [
        # edge cases
        ([], None),
        ([], ""),
        ([], []),
        ([], list(range(1, 102))),
        ([], [None, "1"]),
        ([], ["1", None]),
        ([], [0, 1]),
        # regular cases
        ([1, 0], [9]),
        ([1, 2, 4], [1, 2, 3]),
        ([4, 3, 2, 2], [4, 3, 2, 1]),
    ]

    @pytest.mark.parametrize("expected,digits", test_data)
    def test_plusone(self, expected, digits):
        assert Solution().plusOne(digits) == expected
