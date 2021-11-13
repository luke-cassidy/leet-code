from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit: int = 0

        for i in range(len(prices) - 1):
            today: int = prices[i]
            tomorrow: int = prices[i + 1]
            if tomorrow > today :
                profit = profit + tomorrow - today

        return profit


print("Solution: {}".format(Solution.maxProfit(Solution(), [])))
print("Solution: {}".format(Solution.maxProfit(Solution(), [1])))
print("Solution: {}".format(Solution.maxProfit(Solution(), [1, 2, 3, 4, 5])))
print("Solution: {}".format(Solution.maxProfit(Solution(), [7, 6, 4, 3, 1])))
print("Solution: {}".format(Solution.maxProfit(Solution(), [7, 1, 5, 3, 6, 4])))
