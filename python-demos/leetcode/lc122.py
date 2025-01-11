"""
* 122. Best Time to Buy and Sell Stock II
* https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
"""


class Solution:
    def valid_args(self, prices: list[int]) -> bool:
        if prices is None or not isinstance(prices, list) or len(prices) == 0:
            return False
        return True

    def maxProfit(self, prices: list[int]) -> int:
        if not self.valid_args(prices):
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            if (profit := prices[i] - prices[i - 1]) > 0:
                max_profit += profit
        return max_profit


def main():  # pragma: no cover
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))


if __name__ == "__main__":
    main()
