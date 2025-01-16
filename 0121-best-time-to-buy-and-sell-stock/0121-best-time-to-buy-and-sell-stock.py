class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        buy = arr[0]
        profit = 0

        for price in arr[1:]:
            if buy > price:
                buy = price

            profit = max(profit, price - buy)

        return profit
