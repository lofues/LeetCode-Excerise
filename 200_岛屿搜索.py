class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 对'1'的位置进行搜索遍历，将周围为'1'的位置都置0
        if not grid:return 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i,j):
            grid[i][j] = '0'
            for x,y in [[-1,0],[1,0],[0,1],[0,-1]]:
                temp_x = i + x
                temp_y = j + y
                if 0 <= temp_x < rows and 0 <= temp_y < cols and grid[temp_x][temp_y] == '1':
                    dfs(temp_x,temp_y)
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i,j)
                    cnt += 1
        return cnt