class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows-2):
            a = 0
            for c in range(cols-2):
                print(grid[r][c])
                res=max(res, grid[r][c] + grid[r][c+1] + grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2])
        return res


        