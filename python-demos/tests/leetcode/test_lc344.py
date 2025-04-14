import copy

import pytest

from leetcode.lc344 import Solution


class TestSolution:
    list_0_100001 = list(range(10**5 + 1))
    invalid_test_data = [
        (None),
        (""),
        ([]),
        ([0] * (10**5 + 1)),
    ]
    valid_test_data = [
        (["o", "l", "l", "e", "h"], ["h", "e", "l", "l", "o"]),
        (["h", "a", "n", "n", "a", "H"], ["H", "a", "n", "n", "a", "h"]),
    ]

    @pytest.mark.parametrize("s", invalid_test_data)
    def test_invalid_input(self, s):
        with pytest.raises(ValueError):
            Solution().reverseString(s)

    @pytest.mark.parametrize("expected, s", valid_test_data)
    def test_topKFrequent(self, expected, s):
        s_copy = copy.deepcopy(s)
        solu = Solution()
        solu.reverseString(s)
        assert s == expected
        solu.reverseString(s)
        assert s == s_copy
