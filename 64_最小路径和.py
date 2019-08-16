class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        temp_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    temp_grid[i][j] = grid[i][j]
                elif i == 0:
                    temp_grid[i][j] = temp_grid[i][j-1] + grid[i][j]
                elif j == 0:
                    temp_grid[i][j] = temp_grid[i-1][j] + grid[i][j]
                else:
                    temp_grid[i][j] = min(temp_grid[i-1][j],temp_grid[i][j-1]) + grid[i][j]
        return temp_grid[-1][-1]