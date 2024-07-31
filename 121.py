class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                maxprofit = max(maxprofit, (prices[r]-prices[l]))
            else:
                l += 1
            r += 1
        return maxprofit

