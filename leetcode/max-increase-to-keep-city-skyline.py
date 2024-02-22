class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        horMax = []
        for gr in grid:
            horMax.append(max(gr))

        vertmax = []
        for x in range(len(grid[0])):
            maxNum = 0
            for y in range(len(grid)):
                maxNum = max(maxNum, grid[y][x])

            vertmax.append(maxNum)

        res = 0
        for y in range(len(grid)):
            for x in range(len(grid)):
                res += max(0 , min(vertmax[x], horMax[y]) - grid[y][x])

        return res