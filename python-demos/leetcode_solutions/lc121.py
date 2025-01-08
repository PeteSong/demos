"""
# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if prices is None or not isinstance(prices, list) or len(prices) == 0:
            return 0
        low = prices[0]
        profit = 0
        for p in prices[1:]:
            low = min(low, p)
            profit = max(profit, p - low)
        return profit


def main() -> None:  # pragma: no cover
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))


if __name__ == "__main__":
    main()
