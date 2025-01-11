"""
* 123. Best Time to Buy and Sell Stock III
* https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
"""

import math


class Solution:
    def _valid_args(self, prices: list[int]) -> bool:
        if prices is None or not isinstance(prices, list) or len(prices) == 0:
            return False
        return True

    def maxProfit(self, prices: list[int]) -> int:
        if not self._valid_args(prices):
            return 0
        max_profit_when_buy_one = 0
        max_profit_when_buy_two = 0
        min_cost_when_buy_one = math.inf
        min_cost_when_buy_two = math.inf
        # print(f"price,,,min_cost_when_buy_one,max_profit_when_buy_one,min_cost_when_buy_two,max_profit_when_buy_two")
        for price in prices:
            min_cost_when_buy_one = min(min_cost_when_buy_one, price)
            max_profit_when_buy_one = max(max_profit_when_buy_one, price - min_cost_when_buy_one)
            min_cost_when_buy_two = min(min_cost_when_buy_two, price - max_profit_when_buy_one)
            max_profit_when_buy_two = max(max_profit_when_buy_two, price - min_cost_when_buy_two)
            # print(
            #     f"{price:^5},,,"
            #     f"{min_cost_when_buy_one:^21},"
            #     f"{max_profit_when_buy_one:^23},"
            #     f"{min_cost_when_buy_two:^21},"
            #     f"{max_profit_when_buy_two:^23}"
            # )
        return max_profit_when_buy_two

    def maxProfit2(self, prices: list[int]) -> int:
        def _left_profits():
            min_price = prices[0]
            for i, v in enumerate(prices[1:], 1):
                min_price = min(min_price, v)
                left_profits[i] = max(left_profits[i - 1], v - min_price)

        def _right_profits():
            max_price = prices[-1]
            for i in range(prices_len - 2, -1, -1):
                v = prices[i]
                max_price = max(max_price, v)
                right_profits[i] = max(right_profits[i + 1], max_price - v)

        if not self._valid_args(prices):
            return 0
        prices_len = len(prices)
        left_profits = [0] * prices_len
        _left_profits()

        right_profits = [0] * prices_len
        _right_profits()

        max_profit = 0
        for i in range(prices_len):
            lp = left_profits[i]
            if i + 1 < prices_len:
                rp = right_profits[i + 1]
            else:
                rp = 0
            max_profit = max(max_profit, lp + rp)
        return max_profit


def main() -> None:  # pragma: no cover
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(Solution().maxProfit(prices))
    print(Solution().maxProfit2(prices))


if __name__ == "__main__":
    main()
