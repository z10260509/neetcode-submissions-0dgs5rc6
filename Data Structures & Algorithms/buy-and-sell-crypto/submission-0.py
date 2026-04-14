class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        dp[0] = prices[0]
        res = float('-inf')

        for i in range(1, n):
            dp[i] = min(dp[i - 1], prices[i-1])
            res = max(prices[i] - dp[i], res)
        
        return res if res >= 0 else 0