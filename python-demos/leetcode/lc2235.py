"""
# 2235. Add Two Integers
# https://leetcode.com/problems/add-two-integers/
"""


class Solution:
    def valid_arg(self, num1: int, num2: int) -> bool:
        if not isinstance(num1, int) or not isinstance(num2, int):
            return False
        return True

    def sum(self, num1: int, num2: int) -> int:
        if not self.valid_arg(num1, num2):
            return 0
        return num1 + num2


def main() -> None:
    num1 = 2
    num2 = 8
    expected_result = 10
    r = Solution().sum(num1, num2) == expected_result
    print(f"Is passed: {r}")
    assert r


if __name__ == "__main__":
    main()
