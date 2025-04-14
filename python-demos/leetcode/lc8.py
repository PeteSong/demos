"""
# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi/description/
"""


class Solution:
    def valid_args(self, s: str) -> bool:
        if s is None or (not isinstance(s, str)):
            return False
        return True

    def myAtoi(self, s: str) -> int:
        if not self.valid_args(s):
            raise ValueError("Invalid argument")

        if len(s) == 0 or len((s1 := s.lstrip())) == 0:
            return 0

        sign = 1
        s2 = s1
        if s1[0] in ("-", "+"):
            s2 = s1[1:]
            if s1[0] == "-":
                sign = -1

        if len((s3 := s2.lstrip("0"))) == 0:
            return 0

        all_digits = "0123456789"
        digit_list = []
        for ch in s3:
            if ch in all_digits:
                digit_list.append(ch)
            else:
                break
        if len(digit_list) == 0:
            return 0
        s4 = "".join(digit_list)

        min_int = -(2**31)
        max_int = 2**31 - 1
        n = int(s4) * sign
        if n < min_int:
            return min_int
        if n > max_int:
            return max_int
        return n


def main() -> None:  # pragma: no cover
    s = "   -042"
    print(Solution().myAtoi(s))


if __name__ == "__main__":
    main()
