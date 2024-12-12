# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/description/


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_amount = 0
        for p in accounts:
            t = 0
            for n in p:
                t += n
            if t > max_amount:
                max_amount = t
        return max_amount


def main() -> None:
    accounts = [[1, 5], [7, 3], [3, 5]]
    expected_result = 10
    r = Solution().maximumWealth(accounts) == expected_result
    print(f"Is passed: {r}")
    assert r


if __name__ == "__main__":
    main()
