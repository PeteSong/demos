# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/description/


class Solution:
    def valid_arg(self, accounts: list[list[int]]) -> bool:
        if (
            accounts is None
            or (not isinstance(accounts, list))
            or len(accounts) < 1
            or (not isinstance(accounts[0], list))
            or (len(accounts[0]) < 1)
        ):
            return False
        return True

    def maximumWealth(self, accounts: list[list[int]]) -> int:
        if not self.valid_arg(accounts):
            return 0

        max_amount = 0
        for p in accounts:
            t = sum(p)
            if t > max_amount:
                max_amount = t
        return max_amount


def main() -> None:  # pragma: no cover
    accounts = [[1, 5], [7, 3], [3, 5]]
    expected_result = 10
    r = Solution().maximumWealth(accounts) == expected_result
    print(f"Is passed: {r}")
    assert r


if __name__ == "__main__":
    main()
