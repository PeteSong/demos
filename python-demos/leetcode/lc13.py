"""
# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/
"""

import re


class Solution:
    def valid_arg(self, s: str) -> bool:
        if s is None or (not isinstance(s, str)) or len(s) == 0:
            return False
        re_pattern = r"^[IVXLCDM]+$"
        if not re.match(re_pattern, s):
            return False
        return True

    def romanToInt(self, s: str) -> int:
        if not self.valid_arg(s):
            return 0
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        prev = 0
        n = 0
        for idx in reversed(s):
            curr = symbols[idx]
            if prev > curr:
                n -= curr
            else:
                n += curr
                prev = curr
        return n

    def romanToInt2(self, s: str) -> int:
        if not self.valid_arg(s):
            return 0
        symbols = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        n = 0
        right = len(s)
        while right > 0:
            w = 1
            if right >= 2:
                w = 2
            k = s[right - w : right]
            n += symbols[k]
            right -= w
        return n


def main() -> None:  # pragma: no cover
    s = "MCMXCIV"
    expected_result = 1994
    r = Solution().romanToInt2(s) == expected_result
    print(f"Is passed: {r}")
    assert r
    r = Solution().romanToInt(s) == expected_result
    print(f"Is passed: {r}")
    assert r


if __name__ == "__main__":
    main()
