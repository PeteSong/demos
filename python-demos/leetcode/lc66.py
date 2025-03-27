"""
# 66. Plus One
# https://leetcode.com/problems/plus-one/description/
"""


class Solution:
    def valid_args(self, digits: list[int]) -> bool:
        if digits is None or (not isinstance(digits, list)) or (n := len(digits)) == 0 or n > 100:
            return False
        if any(n is None or (not isinstance(n, int) or n < 0 or n > 9) for n in digits):
            return False
        if digits[0] == 0:
            return False
        return True

    def plusOne(self, digits: list[int]) -> list[int]:
        if not self.valid_args(digits):
            return []
        res = []
        should_plus_one = True
        for n in reversed(digits):
            if should_plus_one:
                n += 1
                should_plus_one = False
            if n >= 10:
                n = 0
                should_plus_one = True
            res.append(n)
        if should_plus_one:
            res.append(1)
        res.reverse()
        return res


def main() -> None:  # pragma: no cover
    inputs = (
        [1, 2, 3],
        [4, 3, 2, 1],
        [9],
    )
    solution = Solution()
    for digits in inputs:
        result = solution.plusOne(digits)
        print(f"{result}")


if __name__ == "__main__":
    main()
