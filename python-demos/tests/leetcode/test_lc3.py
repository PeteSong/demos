import pytest

from leetcode.lc3 import Solution


class TestSolution:
    test_data = [
        # edge cases
        (0, None),
        (0, 3),
        (0, ""),
        # normal cases
        (3, "abcabcbb"),
        (1, "bbbbb"),
        (3, "pwwkew"),
        (2, "aab"),
        (3, "dvdf"),
        (1, " "),
        (1, "a"),
        (1, "aa"),
        (3, "aabcb"),
        (2, "aabbccddeeffgghhii"),
    ]

    @pytest.mark.parametrize("expected, s", test_data)
    def test_lengthOfLongestSubstring(self, expected, s):
        assert Solution().lengthOfLongestSubstring(s) == expected

    @pytest.mark.parametrize("expected, s", test_data)
    def test_lengthOfLongestSubstring2(self, s, expected):
        assert Solution().lengthOfLongestSubstring2(s) == expected
