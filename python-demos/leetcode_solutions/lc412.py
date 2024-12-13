# 412. Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/


class Solution:
    FIZZ: str = "Fizz"
    BUZZ: str = "Buzz"
    FIZZBUZZ: str = FIZZ + BUZZ

    def valid_arg(self, n: int) -> bool:
        if n is None or (not isinstance(n, int)) or n <= 0:
            return False
        return True

    def fizzBuzz(self, n: int) -> list[str]:
        if not self.valid_arg(n):
            return []
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append(self.FIZZBUZZ)
            elif i % 3 == 0:
                ans.append(self.FIZZ)
            elif i % 5 == 0:
                ans.append(self.BUZZ)
            else:
                ans.append(str(i))
        return ans


def main() -> None:  # pragma: no cover
    n = 15
    expected_result = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]
    r = Solution().fizzBuzz(n) == expected_result
    print(f"Is passed: {r}")
    assert r


if __name__ == "__main__":
    main()
