"""
# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/
"""


class Solution:
    def valid_args(self, x: int) -> bool:
        if x is None or (not isinstance(x, int)) or x < -(2**31) or x > 2**31 - 1:
            return False
        return True

    def reverse(self, x: int) -> int:
        if not self.valid_args(x):
            raise ValueError("Invalid arguments")

        if -10 < x < 10:
            return x
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        reversed_x = 0
        b1 = 2**31 // 10
        while x > 0:
            d = x % 10
            if reversed_x > b1:
                return 0
            # the x should be *463847412 , so the reversed_x would be 214748364*
            # the x should be less than 214748364(7/8),
            # so if reversed_x == b1, the x should be 1463847412,
            # after reversed, the last digit would never be greater than 2.
            """
            if reversed_x == b1:
                # lower bound: -2**31 (-2147483648)
                if sign == -1 and x > 8:
                    return 0
                # upper bound: 2**31-1 (2147483647)
                if sign == 1 and x > 7:
                    return 0
            """
            reversed_x = reversed_x * 10 + d
            x //= 10
        return sign * reversed_x

    def reverse2(self, x: int) -> int:
        if not self.valid_args(x):
            raise ValueError("Invalid arguments")

        if -10 < x < 10:
            return x
        sign = 1
        if x < 0:
            sign = -1
        s = str(abs(x))
        s = s[::-1]
        s = s.lstrip("0")
        if len(s) < 10:
            return sign * int(s)
        n1 = int(s[:-1])
        b1 = 2**31 // 10
        if n1 > b1:
            return 0
        return sign * int(s)

    def reverse3(self, x: int) -> int:
        if not self.valid_args(x):
            raise ValueError("Invalid arguments")

        if -10 < x < 10:
            return x

        sign = 1
        s = str(x)
        if x < 0:
            sign = -1
            s = s[1:]
        x_list = list(s)
        p1 = 0
        p2 = len(x_list) - 1
        while p1 < p2:
            x_list[p1], x_list[p2] = x_list[p2], x_list[p1]
            p1 += 1
            p2 -= 1
        s = "".join(x_list)
        s = s.lstrip("0")
        if len(s) < 10:
            return int(s) * sign
        n1 = int(s[:-1])

        upper_bound = 2**31 - 1  # 2147483647
        b1 = upper_bound // 10
        if n1 > b1:
            return 0
        n = int(s) * sign
        return n


def main() -> None:  # pragma: no cover
    x = 123
    solution = Solution()
    result = solution.reverse(x)
    print(f"Input: {x}, Reversed: {result}")
    x = -2147483412
    result = solution.reverse(x)
    print(f"Input: {x}, Reversed: {result}")


if __name__ == "__main__":
    main()
