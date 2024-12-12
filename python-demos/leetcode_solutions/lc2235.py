# 2235. Add Two Integers
# https://leetcode.com/problems/add-two-integers/


class Solution:
    def sum(self, num1: int, num2: int) -> int:
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
