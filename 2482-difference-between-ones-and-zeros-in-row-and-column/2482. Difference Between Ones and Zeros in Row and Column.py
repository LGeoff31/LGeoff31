class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        rowLst = [] #[a,b] a = number zeros, b = number ones in ith row
        colLst = [] #[a,b] a = number zeros, b = number ones in the ith column
        for r in range(rows):
            rowLst.append([grid[r].count(0), grid[r].count(1)])
        for c in range(cols):
            zerosInCol = 0
            onesInCol = 0
            for r in range(rows):
                if grid[r][c] == 0: zerosInCol += 1
                else: onesInCol += 1
            colLst.append([zerosInCol, onesInCol])
        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                res[r][c] = rowLst[r][1] + colLst[c][1] - rowLst[r][0] - colLst[c][0]
        print(rowLst)
        print(colLst)
        return res

        res[1][2]


        
        