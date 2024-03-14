class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or not k: return 0

        rows, cols = k+1, len(prices)
        dp = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            dp[r][0] = 0
        for c in range(cols):
            dp[0][c] = 0
        #edge cases


        for r in range(1, rows):
            a = -1e9
            for c in range(1, cols):
                a = max(dp[r-1][c-1] - prices[c-1], a)
                dp[r][c] = max(dp[r][c-1], a + prices[c])
        print(dp)
        return dp[-1][-1]


        