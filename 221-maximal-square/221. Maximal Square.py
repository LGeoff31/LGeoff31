class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        maxCount = 0
        for c in range(cols):
            if matrix[-1][c] == "0": 
                dp[-1][c] = 0
            else: 
                dp[-1][c] = 1
            maxCount = max(maxCount, dp[-1][c])
            
        for r in range(rows):
            if matrix[r][-1] == "0": 
                dp[r][-1] = 0
            else: 
                dp[r][-1] = 1
            maxCount = max(maxCount, dp[r][-1])
            
        print(dp)
        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                if dp[r+1][c] != 0 and dp[r+1][c+1] != 0 and dp[r][c+1] != 0 and matrix[r][c] != "0":
                    dp[r][c] = 1+ min(dp[r+1][c], dp[r+1][c+1], dp[r][c+1])
                else:
                    if matrix[r][c] == "1": 
                        dp[r][c] = 1
                    else: 
                        dp[r][c] = 0 
                maxCount = max(maxCount, dp[r][c])
        print(dp)
        return maxCount * maxCount
        