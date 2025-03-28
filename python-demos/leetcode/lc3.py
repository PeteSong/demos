"""
# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def valid_args(self, s: str) -> bool:
        if s is None or (not isinstance(s, str)) or len(s) == 0:
            return False
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not self.valid_args(s):
            return 0
        char_index: dict[str, int] = {}
        left = 0
        max_length = 0
        for i, c in enumerate(s):
            if c in char_index:
                left = max(left, char_index[c] + 1)
            char_index[c] = i
            max_length = max(max_length, i - left + 1)
        return max_length

    def lengthOfLongestSubstring2(self, s: str) -> int:
        if not self.valid_args(s):
            return 0
        left = 0
        max_length = 0
        longest_substring_set: set[str] = set()
        for c in s:
            while c in longest_substring_set:
                longest_substring_set.remove(s[left])
                left += 1
            longest_substring_set.add(c)
            max_length = max(max_length, len(longest_substring_set))
        return max_length


def main() -> None:  # pragma: no cover
    inputs = ("abcabcbb", "bbbbb", "pwwkew", "aab", "dvdf")
    solution = Solution()
    for s in inputs:
        result = solution.lengthOfLongestSubstring(s)
        result2 = solution.lengthOfLongestSubstring2(s)
        print(f"Input: {s}, Length of Longest Substring: {result} , {result2}")


if __name__ == "__main__":
    main()
