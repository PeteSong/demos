"""
# 344. Reverse String
# https://leetcode.com/problems/reverse-string/description/
"""


class Solution:
    def valid_arg(self, s: list[str]) -> bool:
        if s is None or not isinstance(s, list) or (s_len := len(s)) == 0 or s_len > 10**5:
            return False
        return True

    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not self.valid_arg(s):
            raise ValueError("Invalid arguments")

        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1


def main() -> None:  # pragma: no cover
    s = ["h", "e", "l", "l", "o"]
    print(s)
    solu = Solution()
    solu.reverseString(s)
    print(s)
    solu.reverseString(s)
    print(s)


if __name__ == "__main__":
    main()
